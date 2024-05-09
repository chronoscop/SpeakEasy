from comtypes.client import CreateObject
from comtypes.gen import SpeechLib 
# Create a voice engine object
engine = CreateObject("SAPI.SpVoice")
# Create an audio stream object
stream = CreateObject("SAPI.SpFileStream") 
# Define the input file name
infile = 'demo.txt'
# Define the output file name
outfile = 'SpeechLib/demo_audio.wav'
# Open the output stream
stream.Open(outfile, SpeechLib.SSFMCreateForWrite) 
# Set the audio output stream
engine.AudioOutputStream = stream 
# Open the input file
f = open('SpeechLib/demo.txt', 'r', encoding='utf-8') 
# Read the text from the input file
TheText = f.read() 
# Close the input file
f.close()  
# Speak the text
engine.speak(TheText) 
# Close the output stream
stream.close() 
