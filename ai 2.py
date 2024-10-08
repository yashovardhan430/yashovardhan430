import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
import pyautogui as pg


engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level between 0 and 1

def speak(text):
    
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Request error from Google Speech Recognition service.")
        return ""

def open_whatsapp_and_send_message(contact, message):
    speak(f"Opening WhatsApp and sending message to {contact}.")
    pywhatkit.sendwhatmsg_instantly(contact, message)
    time.sleep(10)  # Wait for the browser and WhatsApp Web to load
    pg.press('enter')  # Press enter to send the message
    speak("Message sent successfully.")

def main():
    speak("Voice Assistant Activated. Say 'Hello Sajwan' to begin.")
    while True:
        command = listen()
        if "hello bro" in command:
            speak("Hello! How can I assist you?")
            while True:
                task = listen()
                if "send message" in task:
                    speak("Please say the 10-digit phone number of the recipient in India.")
                    contact_number = listen()

                    if contact_number:
                        contact_number = contact_number.replace(" ", "")  # Remove any spaces
                        contact = "+91" + contact_number

                        speak("What is the message?")
                        message = listen()

                        if message:
                            open_whatsapp_and_send_message(contact, message)
                        else:
                            speak("No message was detected.")
                elif "exit" in task or "close" in task:
                    speak("Goodbye!")
                    exit(0)
                else:
                    speak("Command not recognized, please try again.")

if __name__ == "__main__":
    main()


    

