import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
# Get the available voices
voices = engine.getProperty('voices')
# Check the number of available voices
print(len(voices))

# Iterate through the voices
for voice in voices:
    # Print the voice name and id
    print('voice:' ,voice.name)
    print(f'id: {voice.id}')
    print('')
import pyttsx3 as pyttsx

# Initialize the pyttsx engine
engine = pyttsx.init()  # inital engine
engine.save_to_file('独断万古荒天帝, 唯负罪州火桑女', 'pyttsx3/output.mp3')  # Save the text to a file and speak it
engine.runAndWait()  # run the file