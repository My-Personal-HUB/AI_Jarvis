# AI_Assistant
The AI Virtual Assistant works using an android app which is installed on the user's android phone. The user activates the agent using the wake up command, 'Listen up Jarvis'. The android app is connected to the Arduino 101 via Bluetooth which is inturn connected to the relay and hence the electrical appliances

https://github.com/My-Personal-HUB/AI_Jarvis/blob/master/jarvisai.jpg

# Assistant Skills
Opens a web page (e.g 'Jarvis open youtube')

Play music in Youtube (e.g 'Jarvis play mozart')

Increase/decrease the speakers master volume (also can set max/mute speakers volume) ** (e.g 'Jarvis volume up!')

Opens libreoffice suite applications (calc, writer, impress) (e.g 'Jarvis open calc')

Tells about something, by searching on the internet (e.g 'Jarvis tells me about oranges')

Tells the weather for a place (e.g 'Jarvis tell_the_skills me the weather in London')

Tells the current time and/or date (e.g 'Jarvis tells me time or date')

Set an alarm (e.g 'Jarvis create a new alarm')

Tells the internet speed (ping, uplink and downling) (e.g 'Jarvis tell_the_skills me the internet speed')

Tells the internet availability (e.g 'Jarvis is the internet connection ok?')

Tells the daily news (e.g 'Jarvis tell me today news')

Spells a word (e.g 'Jarvis spell me the word animal')


Jarvis is a personal assistant made using Python. It is coded in a structured way so that you can easily understaind and modify the code for your needs. I only tested Jarvis on windows, but it should run on other operating systems if the required modules are installed.

To use it:

Create a project folder
Put 'Jarvis.py' in that folder.
Create a new folder named 'music' inside you project folder, put some mp3 music files there, so that Jarvis can find and play it if you ask him to by saying 'play music' or just 'music'. speekmodule.py and Jarvis.py must be in the same folder. Install all requested modules (pyaudio, speech_recognition, pygame, socket, webbrowser, subprocess, glob, gtts, os, random,) some of these modules are preinstalled with Python. Jarvis uses Google for converting speech to text, so you need an internet connection.
Enjoy :D
