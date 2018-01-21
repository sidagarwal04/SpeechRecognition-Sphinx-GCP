import speech_recognition as sr  
from time import time
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

  
 # obtain audio from the microphone  
r = sr.Recognizer()  
with sr.Microphone() as source:  
   print("Please wait. Calibrating microphone...")  
   # listen for 5 seconds and create the ambient noise energy level  
   r.adjust_for_ambient_noise(source, duration=5)  
   print("Say something!")  
   audio = r.listen(source)  

print("")
print("Speech Recognition:")


start_time = time()  
 # recognize speech using Sphinx  
try:  
   print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")  
except sr.UnknownValueError:  
   print("Sphinx could not understand audio")  
except sr.RequestError as e:  
   print("Sphinx error; {0}".format(e))  
end_time = time()
time_taken = end_time - start_time 
print ("Time required for Sphinx analysis: " + str(time_taken) + " sec")

start_time = time()
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said '" + r.recognize_google(audio) + "'")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
end_time = time()
time_taken = end_time - start_time 
print ("Time required for Google Speech Recognition: " + str(time_taken) + " sec")



# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = r.recognize_google(audio)


document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment
classify = client.analyze_sentiment(document=document).document_sentiment

# print('Text: {}'.format(text))
# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
print("")
print("Google ML API for Natural Language Processing:")
print sentiment


def classify_text(text):
    """Classifies content categories of the provided text."""
    client = language.LanguageServiceClient()


    document = types.Document(
        content=text.encode('utf-8'),
        type=enums.Document.Type.PLAIN_TEXT)

    categories = client.classify_text(document).categories

    for category in categories:        
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))
	print(u'=' * 20)


classify_text(text)
