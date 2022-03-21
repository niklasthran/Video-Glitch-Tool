## Video Glitch Tool

### Disclaimer
This is very experimental and did not have the chance for tests on any systems other than macOS yet.

### Why?
+ I like the idea of using video data as material that can be mixed and scrambled around, as one could do it with physical matter. I tried to manifest that through the code as well.
+ Initially, I wanted to automate the process of messing with video data in a hex-editor (e.g. Hex Fiend) and in essence, this is what the tools are doing.
+ I was interested in being able to use two (or more?) videos and mixing them would bring pretty interesting results.
+ My research in already existing tools might be poor (as it was not the point of this project) but I have not seen other tools that work in the same way yet.

### How does it work?
+ I tried to turn this into a command-line tool. It is far from perfect but my idea was that it would make the use quick, easy and more fun for everybody, including myself.
+ I decided to make two sorts of *variants* of the tool because both mix the data in different ways.

Both take the same input arguments:
```bash
python one_of_the_tools.py video_file_a video_file_b frame_type
```
E.g.:
```bash
python remix_frames.py videoA.avi videoB.avi P
```
As explained above, the tools use data from two videos and will mix a specified frame type (`I`-, `P`- or `B`-frame, specifying a single letter is enough) from those videos. I found that .avi works best but in theory, you could use any format.
The video will be baked and filed into the repository you would previously `cd`'d to.

### Ideas for future iterations
+ The tools could be combined into an all-in-one solution controlled via input arguments.
+ There could be an option that mixes different frame types and not just one for more **chaosss**.

Please feel free to use and/or edit those tools as you like – I consider them as 100% open source. It would be awesome to see improvements and/or variations that could produce other interesting glitches and other things that people would come up with.
I tried my best to comment on everything that has been used within the code. Constructive feedback is very much welcome :heart:

Originated from experiments in the context of [Fabiola Hannah](http://fabiolahanna.com/)'s (Un)Coding Video class at The New School.
