# 🗣️ offline-tts-natural-voices

Use **Microsoft Natural Voices** (offline) in Python projects with `pyttsx3`.

---

## 📌 Description

This project allows you to use **Microsoft Natural Voices** offline in Python programs for speech synthesis via the `pyttsx3` library.

---

## 🚀 Installation and Setup

### 1. Install the Voice Adapter (required once)

Download and install **NaturalVoiceSAPIAdapter**:

🔗 [Download NaturalVoiceSAPIAdapter (GitHub Releases)](https://github.com/gexgd0419/NaturalVoiceSAPIAdapter/releases)

> This application provides access to Natural Voices for your system.

---

### 2. Install Offline Voice Packages (MSIX)

Go to the website and download the required voices:

🗂 [List of Natural Voices (MSIX)](https://sensoryreadable.com/microsoft-natural-voice-download/)

- Support for both male and female voices
- Multiple languages (including English, Chinese, Korean, etc.)
- After installation, restart the system (if required)

---

### 3. Install Python Dependencies

Install `pyttsx3`:

```bash
pip install pyttsx3
```

---

## 🧪 Example Usage

```python
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
```

---

## 🛠️ Possible Issues

- If the voice is not working, make sure:
  - You have installed the SAPI adapter
  - The voices are correctly installed (MSIX)
  - You have restarted your system
- On some systems, you may need to run Python as administrator

## 💡 Author

Created with ❤️ by **SMILE-NM** 😊

Check out my GitHub: [github.com/SMILE-NM](https://github.com/SMILE-NM)

If you found this project useful, please ⭐️ it on GitHub!
