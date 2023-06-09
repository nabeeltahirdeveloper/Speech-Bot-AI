import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert audio input to text
def recognize_speech():
  # Use the microphone as the audio source
  with sr.Microphone() as source:
    # Listen for audio input
    audio = r.listen(source)

  # Try to recognize the spoken words
  try:
    # Return the recognized text
    return r.recognize_google(audio)
  except:
    # Return an error message if the recognition fails
    return "Error: Could not recognize speech"

# Test the speech recognition
print(recognize_speech())
