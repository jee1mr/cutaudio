#Simple audio cutter app created by jee1mr

from moviepy.editor import *
#For reading command line arguments
import sys

#Checking if there are fewer arguments 
#There should be 4 arguments
#1. filename: filename with path and extension
#2. start_time: Start time in seconds (eg:120)
#3. end_time: End time in seconds
#4. y_or_n: Need Preview- Y or N?

if(len(sys.argv)<5):
	print("Invalid Usage")
	print("Use as: python cutaudio.py filename start_time end_time y_or_n")

else:
	file_name=str(sys.argv[1])
	audio = AudioFileClip(file_name)

	start=int(sys.argv[2])
	end=int(sys.argv[3])
	cutaudio=audio.subclip(start,end)

	if(sys.argv[4]=="Y" or sys.argv[4]=="y"):
		cutaudio.preview()
	new_file_name="edit-"+file_name
	cutaudio.to_audiofile(new_file_name)

#Bug checks: Check what happens when end time is lesser than start time
#Bug 1: The audio saved doesn't play in any player

