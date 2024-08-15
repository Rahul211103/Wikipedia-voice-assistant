import pyttsx3
import wikipedia
import speech_recognition as sr
import distutils


engine = pyttsx3.init()

# Initialize recognizer
recognizer = sr.Recognizer()


# Use microphone as audio source

with sr.Microphone() as source:

    print("Ask a Question")
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))

n=input("enter the number of sentence you want")

In = text
# to get the summary(details) on the question you have asked
result = wikipedia.summary(In, sentences=n)

# to print sentence line by line
sentences = result.split(". ")
for sentence in sentences:
    print(sentence)

engine.say(result)
engine.runAndWait()
