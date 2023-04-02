import os
import openai
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

load_dotenv()

# Configure the languages you want to support
languages_config = {
    "es": {
        "language": "es-ES",
        "voice": "spanish-latin-am",
        "context": "eres mi asistente virtual",
        "greeting": "Hola, ¿cómo puedo ayudarte?"
    },
    "en": {
        "language": "en-US",
        "voice": "english",
        "context": "you are my virtual assistant",
        "greeting": "Hello, how can I help you?"
    }
}


# Get the language from the environment variable
language = os.getenv("LANGUAGE") or "en"
language_config = languages_config[language]


# Query OpenAI
def query_openai(prompt):
  api_key = os.getenv("OPENAI_API_KEY")
  openai.api_key = api_key

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", messages=[
          {"role": "system", "content": language_config["context"]},
          {"role": "user", "content": prompt}
      ]
  )
  return response.choices[0].message.content


# Get the prompt from the microphone
def get_prompt():
  print(language_config["greeting"])
  r = sr.Recognizer()
  with sr.Microphone() as source:
    audio = r.listen(source)
    prompt = r.recognize_google(audio, language=language_config["language"])
    return prompt


# Tell the response to the user
def tell_response(response):
  engine = pyttsx3.init()
  engine.setProperty('voice', language_config["voice"])
  engine.say(response)
  engine.runAndWait()


if __name__ == "__main__":
  prompt = get_prompt()
  response = query_openai(prompt)
  print(response)
  tell_response(response)
