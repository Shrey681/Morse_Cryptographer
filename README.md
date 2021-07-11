# Morse_Cryptographer

Team Members:
Shruti Jain
Nimit Jhunjhunwala
Shrey Kadam

Features:
Encoding Text to Morse Code
Decoding Morse Code to Text
Encoding Audio Text to Morse Code

Softwares:
Python
GUI - PyQT5
Audio -
Speech recognition (Speech to Text)
PyAudio
	
Overview:
This Python project ‘Morse Cryptographer’ is to better understand morse cryptography i.e. to encode and decode morse codes. 

Text to Morse involves conversion of texts into morse by two methods namely; typing the text & via audio text. 
To access the prior, user simply needs to type the text and click on ‘Submit’ to get the encoded morse code. While in the second case, the user needs to click on ‘Audio’, wait for 2 seconds and speak in the text (without using any microphone).

Morse to Text involves conversion of morse into text, simply by typing in the morse and clicking on ‘Submit’ to get the decoded morse text.
 

Description about Python Packages used:
PyQt - PyQt is a python binding of the open-source widget-toolkit Qt, which also functions as a cross-platform application development framework. Qt is a popular framework for writing GUI applications for all major desktop, mobile, and embedded platforms (supports Linux, Windows, MacOS, Android, iOS, Raspberry Pi, and more).
QtCore - Core non-GUI classes used by other modules<br>
QtGui - Graphical user interface components
QtWidgets - Classes for creating classic desktop-style UIs.
QLabel - A QLabel object acts as a placeholder to display non-editable text or image, or a movie of animated GIF. It can also be used as a mnemonic key for other widgets.
QPushButton: In PyQt API, the QPushButton class object presents a button which when clicked can be programmed to invoke a certain function.
QLineEdit - QLineEdit object is the most commonly used input field. It provides a box in which one line of text can be entered. In order to enter multi-line text, a QTextEdit object is required.


Speech_Recognition - Speech recognition, also known as automatic speech recognition (ASR), computer speech recognition, or speech-to-text, is a capability which enables a program to process human speech into a written format.
Adjust_for_ambient_noise() - An audio file can contain noise due to several reasons. Noise can actually affect the quality of speech to text translation. To reduce noise, the Recognizer class contains adjust_for_ambient_noise() method, which takes the AudioData object as a parameter.
Recognize_google(audio) - Recognize speech using Google Speech Recognition; to transcribe our audio files.
Listen - Take voice input from the microphone

PyAudio - PyAudio is a Python library which is an open - source and cross - platform audio input - output. It has a wide range of functionalities, which are audio - related and mainly focusing on segmentation, features extraction, classification and visualization issues.By using the pyaudio library, users can classify unknown sounds, perform supervised and unsupervised segmentation, extract audio features and representations, detect audio events and filter out silence periods from the long recordings, apply dimensionality reduction to visualize audio data and content similarities and much more.
device_index - It is an attribute of the library of PyAudio which is used to set the desired microphone of the system as the one to be used for executing the program. It has collection of all the microphones connected to the system as a list starting with the index of 0, but if you want to use the default microphone of the system like your bluetooth headsets or wire ones then set this attribute at None.





