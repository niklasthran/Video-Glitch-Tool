##### Experimental Tools to Produce Glitches in Video

###### Why?
+ I like the idea of using video data as material that can be mixed and scrambled around, as it would be physical matter, and I tried to manifest that through the code as well.
+ Initially, I wanted to automate the process of messing with video data in a hexeditor (e.g. Hex Fiend) and in essence this is what the tools are doing.
+ I thought being able to use two (or more?) videos and mix them into each other would bring pretty interesting results.
+ My research in already existing tools might be poor (as it was not really the point of this project) but I have not yet seen other tools that work in the same way.

###### How does it work?
+ I tried to turn this into a commandline tool. It is far from perfect but my idea was that it would make the use easier for everybody, including myself.
+ I decided to make three sort of 'variants' of the tool because all three of them mix the data in different ways.
+ All three take the same input arguments:

`$ python one_of_the_tools.py file_a file_b frame_type`

Example:

`$ python remix_frames.py videoA.avi videoB.avi P`

As explained above, the tools use data from two videos and will mix a specified frame type (`I`-, `P`- or `B`-frame, specifying a single letter is enough) from those videos. I found that .avi works best but in theory you could use any format.
The video will be baked and filed into the repository you previously `cd`'d to.

###### Ideas for future iterations
+ These three tools could be combined into an all-in-one solution controlled via input arguments.
+ There could be an option that mixes different frame types and not just one for more **chaosss**.

Please feel free to use those tools as you like. Also, feel free to edit them – I consider them as 100% open source. It would be awesome to see improvements and/or variations that could produce other interesting glitches and other things that people would come up with.
I tried my best to comment everything that has been used within the code. Constructive feedback is very much welcome :heart:
