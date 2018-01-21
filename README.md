# SpeechRecognition-Sphinx-GCP
Speech Recognition on edge using OpenCV and on cloud using AWS Rekognition

# Overview
Here is the code for Speech Recognition using Sphinx and Google Cloud Speech API with input from micorphone. The text from speech recognition is then used as input to Google Cloud Natural Language API for Sentiment Analysis and Content Classification. We need a microphone to provide audio input to the program. 

# Dependencies
- Install Ubuntu 16.04, https://www.ubuntu.com/download/desktop
- Install Python 2.7.14, https://www.python.org/downloads/
- PyAdudio package,  `$ pip install pyaudio`
- Pocketsphinx package, `$ pip install pocketsphinx`  
- Speech recognition, `$ pip install SpeechRecognition`
- Install Google Speech API client, `$ pip install --upgrade google-cloud-speech`
- Install Google Natural Language API client, `$ pip install --upgrade google-cloud-language`
- Authenticating to the Cloud Speech API, `$ export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_KEY_FILE`, https://cloud.google.com/speech/docs/auth#using_a_service_account
- Authenticating to Google Cloud ML API, https://cloud.google.com/natural-language/docs/auth

# Note
Replace PATH_TO_KEY_FILE with the path to your JSON service account file. GOOGLE_APPLICATION_CREDENTIALS should be written out as-is (it's not a placeholder in the example above).
If Speech Recognition package fails, try `$ sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev` and `$ sudo apt-get install libpulse-dev`

# Usage
Run following code in the terminal,

`python speech_recognition_NL_processing.py`

Enjoy, Have Fun!
