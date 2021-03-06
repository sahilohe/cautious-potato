import tweepy
import os, time
import speech_recognition as sr

auth = tweepy.OAuthHandler("your_API_key", "your_API_secret")
auth.set_access_token("oauth_token",
                      "oauth_token_secret")

api = tweepy.API(auth)
user = api.get_user('your_username') # just for testing

recognizer = sr.Recognizer()

with sr.Microphone() as source_audio: # pip3 install pyaudio, sudo apt install jackd2
    audio_data = recognizer.record(source_audio, duration=10) # say your message in 10 seconds
    text = recognizer.recognize_google(audio_data)
    print(text)
    
    send_it_or_not = input("Do you want to post it? ")
    
    if send_it_or_not.lower() == 'yes':
      api.update_status(f'"{text}"\n\nVia Tweepy (Python Automation)')
      print("Let's check")
      time.sleep(1)
      print("Going to twitter.com")
      os.system("firefox twitter.com")
      
    elif send_it_or_not.lower() == 'no':
      print("Exiting the program")
      exit()      
    else:
      print("Something went wrong")
      exit()
 
