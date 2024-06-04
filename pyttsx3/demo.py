import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Check the number of available voices
print(f'Number of available voices: {len(voices)}\n')

# Iterate through the voices and print their details
for voice in voices:
    print('Voice:')
    print(f'  Name: {voice.name}')
    print(f'  ID: {voice.id}')
    print(f'  Languages: {voice.languages}')
    print(f'  Gender: {voice.gender}')
    print(f'  Age: {voice.age}\n')

# Set properties for speech
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
engine.setProperty('voice', voices[0].id)  # Set a specific voice by id

# Print current settings
print(f'Current speech rate: {engine.getProperty("rate")}')
print(f'Current volume level: {engine.getProperty("volume")}')
print(f'Current voice: {engine.getProperty("voice")}\n')

# Save text to an audio file
text_to_save = '独断万古荒天帝, 唯负罪州火桑女'
output_file_path = 'output.mp3'

engine.save_to_file(text_to_save, output_file_path)  # Save the text to a file
print(f'Text has been saved to {output_file_path}')

# Speak text directly
engine.say('Hello, this is a test of the text-to-speech functionality.')
engine.say('Here is some Chinese text: 独断万古荒天帝, 唯负罪州火桑女')

# Run the engine to process all commands
engine.runAndWait()

# Additional Methods
def on_start(name):
    print(f'Starting: {name}')

def on_word(name, location, length):
    print(f'Word: {name}, {location}, {length}')

def on_end(name, completed):
    print(f'Finished: {name}, {completed}')

# Connect callback methods
engine.connect('started-utterance', on_start)
engine.connect('started-word', on_word)
engine.connect('finished-utterance', on_end)

# Speak another text with callbacks
engine.say('This is a callback demonstration.')
engine.runAndWait()

# List of additional methods and their usage
# engine.stop()  # Stops the current speech
# engine.isBusy()  # Returns True if the engine is currently speaking

# Example of changing voice properties dynamically
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say(f'This is a test of voice: {voice.name}')
    engine.runAndWait()

# Example of changing speech rate and volume dynamically
engine.setProperty('rate', 100)  # Slow speech
engine.say('This is slow speech.')
engine.setProperty('rate', 200)  # Fast speech
engine.say('This is fast speech.')
engine.setProperty('volume', 0.5)  # Half volume
engine.say('This is half volume.')
engine.setProperty('volume', 1.0)  # Full volume
engine.say('This is full volume.')

engine.runAndWait()
