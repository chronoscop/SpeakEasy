from win32com.client import Dispatch

def list_voices():
    """List all available voices."""
    speaker = Dispatch('SAPI.SpVoice')
    voices = speaker.GetVoices()
    voice_list = [voice.GetDescription() for voice in voices]
    del speaker
    return voice_list

def text_to_speech(message, voice_name=None, rate=0, volume=100):
    """
    Convert text to speech.

    :param message: The text to be spoken.
    :param voice_name: The name of the voice to use. If None, the default voice is used.
    :param rate: The rate of speech (-10 to 10, where 0 is the default rate).
    :param volume: The volume of the speech (0 to 100, where 100 is the default volume).
    """
    # Set up SAPI
    speaker = Dispatch('SAPI.SpVoice')

    # Set the voice if specified
    if voice_name:
        for voice in speaker.GetVoices():
            if voice_name in voice.GetDescription():
                speaker.Voice = voice
                break

    # Set the rate of speech
    speaker.Rate = rate

    # Set the volume of the speech
    speaker.Volume = volume

    # Speak the message
    speaker.Speak(message)

    # Delete the speaker object
    del speaker

# Example usage
msg = " 独断万古荒天帝, 唯负罪州火桑女" #you can change the text here
voice_name = "Microsoft David Desktop"  # Specify the voice name if desired
rate = 1  # Set the rate of speech (-10 to 10)
volume = 90  # Set the volume of the speech (0 to 100)

# List available voices
available_voices = list_voices()
print("Available voices:")
for voice in available_voices:
    print(voice)

# Convert text to speech with the specified settings
text_to_speech(msg, voice_name, rate, volume)
