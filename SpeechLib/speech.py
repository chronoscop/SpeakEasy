from comtypes.client import CreateObject
from comtypes.gen import SpeechLib

def text_to_speech(infile, outfile):
    # Create a voice engine object
    engine = CreateObject("SAPI.SpVoice")

    # Create an audio stream object
    stream = CreateObject("SAPI.SpFileStream")

    # Open the output stream
    stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
    
    # Set the audio output stream
    engine.AudioOutputStream = stream

    # Open the input file and read the text
    with open(infile, 'r', encoding='utf-8') as f:
        TheText = f.read()

    # Speak the text
    engine.speak(TheText)

    # Close the output stream
    stream.close()

# Additional methods and functionalities

def set_voice(engine, voice_name):
    """Set the voice of the speech engine."""
    voices = engine.GetVoices()
    for voice in voices:
        if voice_name in voice.GetDescription():
            engine.Voice = voice
            break

def set_rate(engine, rate):
    """Set the rate of the speech."""
    engine.Rate = rate

def set_volume(engine, volume):
    """Set the volume of the speech."""
    engine.Volume = volume

# Usage examples

# Define the input and output file names
input_file = 'SpeechLib/demo.txt'
output_file = 'SpeechLib/demo_audio.wav'

# Create a voice engine object
engine = CreateObject("SAPI.SpVoice")

# Set the voice to a specific voice (e.g., "Microsoft David Desktop")
set_voice(engine, "Microsoft David Desktop")

# Set the rate of speech (-10 to 10, where 0 is the default rate)
set_rate(engine, 1)

# Set the volume of the speech (0 to 100, where 100 is the default volume)
set_volume(engine, 90)

# Convert text to speech with the specified settings
text_to_speech(input_file, output_file)
