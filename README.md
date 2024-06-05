# Text To Speech


## pyttsx3

**pyttsx3** is a Python library for text-to-speech conversion. It allows developers to add speech synthesis capabilities to their Python applications easily. 

### Feature

1. **Cross-Platform Compatibility:** It works on multiple platforms including Windows, macOS, and Linux, making it suitable for developing applications that need text-to-speech functionality across different operating systems.
2. **Simple API:** The library provides a straightforward API for converting text to speech, making it easy to integrate into Python projects. Developers can quickly add speech synthesis capabilities without extensive configuration.
3. **Customizable Speech Output:** pyttsx3 allows customization of speech output such as voice selection, speech rate, and volume adjustment. This enables developers to tailor the speech synthesis to suit their application requirements.

###  Installation

```shell
pip install pyttsx3
```

### Usage

 In pyttsx3 folder

### Documentation

more using **API** please visit https://pyttsx3.readthedocs.io/en/latest/engine.html



## SAPI

**SAPI (Speech Application Programming Interface)** is a Microsoft Windows API that enables developers to integrate speech recognition and speech synthesis capabilities into their applications. It provides a standardized interface for accessing speech services and is widely used for developing applications that interact with users through speech.

For SAPI (Speech Application Programming Interface), its functionality can be accessed through the win32com library, which enables text-to-speech (TTS) and speech recognition.

### Installation

You need to install the `pywin32` library to use SAPI's functionalities:

```shell
pip install pywin32
```

### Usage

please see SAPI folder

### Documentation

For more installation information, visit https://pypi.org/project/pywin32/ and https://github.com/mhammond/pywin32



##  SpeechLib

**SpeechLib**, also known as the Microsoft Speech Object Library, is a component of the Microsoft Speech API (SAPI) that provides a COM-based interface for text-to-speech (TTS) and speech recognition (SR) functionality on Windows platforms.


### Installation

**To use SpeechLib you need to install third-party libraries : comtypes**

```shell
pip install comtypes
```

### Usage

example in SpeechLib folder

### Documentation

The documentation is currently hosted on pythonhosted at: https://pythonhosted.org/comtypes
