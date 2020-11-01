import tweepy
import speech_recognition as sr

auth = tweepy.OAuthHandler("your_API_key", "your_API_secret")
auth.set_access_token("oauth_token",
                      "oauth_token_secret")

api = tweepy.API(auth)
user = api.get_user('your_username') # just for testing


recognizer = sr.Recognizer()

with sr.Microphone() as source_audio:
    audio_data = recognizer.record(source_audio, duration=10)
 
    text = recognizer.recognize_google(audio_data)
    print(text)
    
    send_it_or_not = input("Do you want to send it? ")
    
    if send_it_or_not.lower() == 'yes':
      api.update_status(f'"{text}"\n\nVia Tweepy (Python Automation)')
    elif send_it_or_not.lower() == 'no':
      print("Exiting the program")
      exit()      
    else:
      print("Something went wrong")
      exit()
 
