import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Print the list of available voices
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name} — {voice.id}")

# Set the desired voice (e.g., with index 1)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

engine.say("Hello! This is the Microsoft Natural Voice.")
engine.runAndWait()