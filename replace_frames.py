import os, sys, subprocess, shlex, re
from subprocess import call
import json
import pandas as pd
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_a", help="Add a file for frame mixing")
parser.add_argument("file_b", help="Add another file for frame mixing")
parser.add_argument("frame_type", help="Specify the frame type")
args = parser.parse_args()

file_a = args.file_a
file_b = args.file_b
file_out = 'vid_processed.mp4'

# 1) Importing information about video frames:
#    type      (pict_type):  I, P or B
#    position  (pkt_pos):    in bytes
#    size      (pkt_size):   in bytes

def get_video_info(file_in):
  # using ffprobe (part of ffmpeg) to read in given video files and print information specified in the command
  command = ['ffprobe', '-i', file_in, '-show_entries', 'frame=pict_type,pkt_pos,pkt_size', '-of', 'json']
  output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  data_out, _ = output.communicate()
  # returning a json formatted dictionary
  data_out = json.loads(data_out)
  return data_out

# 2) Reading video files into byte string

def read_in(file_in):
  # reading file as binary string (r = read, b = binary)
  with open(file_in, 'rb') as fd_in:
    data_out = fd_in.read()
  return data_out

# 3) Mix frames ...
# 3.1) Put frame data in DFs

def get_frame_dimensions(data_in, frame_type):
  # for convenience frame information will be stored in pandas data frames (DF)
  df = pd.DataFrame(columns=['start', 'size'])
  size_list = []
  start_list = []

  for i in range(len(data_in['frames'])):
    if 'pict_type' in data_in['frames'][i]:
      if data_in['frames'][i]['pict_type']:
        # Not every frame in the data set has a specified picture type (or frame type)
        # so there needs to be this if condition to make sure the right information
        # is being stored in the DF later on
        if data_in['frames'][i]['pict_type'] == frame_type:
          i_frame_size_a = int(data_in['frames'][i]['pkt_size'])
          i_frame_start_a = int(data_in['frames'][i]['pkt_pos'])
          # This might not be the most efficient way but its definitely a clean
          # flow: data -> list -> DF
          size_list.append(i_frame_size_a)
          start_list.append(i_frame_start_a)

  df['size'] = size_list
  df['start'] = start_list

  return df

# 3.2) Mix it up

def mix_data(data_a, data_b, df_a, df_b, padding):
  # There seems to be a padding in the iframe container. 50 bytes work

  a = abs(len(df_a) - len(df_b))
  b = (len(df_a) + len(df_b)) - a
  c = int(b / 2)

  for i in range(0, c):

    frame_start_a = df_a['start'][i] + padding
    frame_size_a = df_a['size'][i]
    frame_start_b = df_b['start'][i] + padding
    frame_size_b = df_b['size'][i]
    # This takes a specified location in the byte string of a file and *replaces*
    # it with another specified sequence from another file
    # The specification is being determined by the DF's data
    data_a = data_a.replace(data_a[frame_start_a : frame_start_a + frame_size_a],
                                    data_b[frame_start_b : frame_start_b + frame_size_a])
  
  return data_a

# 4) Writing video files

def write_out(file_out, data_in):
  # w = write, b = byte
  # This writed the manipulated byte string into a readable data format (e.g. MPEG or MOV)
  with open(file_out, "wb") as fd_out:
    fd_out.write(data_in)

# 5) Bake the video
# This step is super important since media players such as Quicktime or even the built-in Preview
# on macOS will try to conceil or repair the "glitches"
# This function "bakes" the video and makes the artifacts permanent, as if there are intentional.
# Well, they are.
def bake_video(file_out):
  file_bake = f"{file_out[:-4]}_baked.mp4"
  command = ['ffmpeg', '-y', '-i', file_out, file_bake]
  output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output = output.communicate()
  return output

print(f"Reading video data ...")
video_frames_a = get_video_info(file_a)
video_frames_b = get_video_info(file_b)

video_data_a = read_in(file_a)
video_data_b = read_in(file_b)

frame_type = args.frame_type

video_df_a = get_frame_dimensions(video_frames_a, frame_type)
video_df_b = get_frame_dimensions(video_frames_b, frame_type)

print(f"Frame replacing ...")
video_data_mix = mix_data(video_data_a, video_data_b, video_df_a, video_df_b, 50)

print(f"Writing video data ...")
write_out(file_out, video_data_mix)

print(f"Baking video data ...")
bake_video(file_out)

print(f"Done!")