# <a name="ai-voicetranslator"></a> LinguaSpeak: Real-time Voice-to-Voice Translation in 6 Popular Languages

## Table of Contents
- [Detailed Breakdown of the Code](#detailed-breakdown) 
- [Technologies Used](#technologies-used)
- [How To Run the Code](#how-to-run-the-code)
- [Contributing](#contributing)

## <a name="detailed-breakdown"></a> Detailed Breakdown of the Code
The purpose of this Python script is to create an application that translates spoken English into six popular languages (Spanish, Turkish, Japanese, French, German, and Chinese) and plays back the translated text as speech. The program uses Gradio for creating the user interface, AssemblyAI for speech-to-text transcription, and ElevenLabs for text-to-speech generation.

**Skills Acquired:**
* API integration (AssemblyAI, ElevenLabs)
* File handling and text processing
* Real-time user interface creation using Gradio
* Error handling and exception management
* Text translation via the translate library

Here’s a breakdown of the major segments in the code:

**a. Importing Libraries**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/7699cd81615efc1e8d15a2cb6ba371f0dd2a6e2c/1.png">

* Gradio creates the interface, allowing users to upload audio.
* AssemblyAI handles the transcription of audio to text.
* Translator translates English text into different languages.
* ElevenLabs converts the translated text back into speech using various voices.

**b. Global Configuration and Supported Languages**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/2.png?raw=true">

API keys for external services (AssemblyAI and ElevenLabs) are globally defined here, and a dictionary of supported languages is set up, mapping language names to their respective language codes.

**c. Voice-to-Voice Functionality**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/3.png?raw=true">

This function is the core of the app, transcribing an uploaded audio file, translating the transcribed text into multiple languages, and then converting the translations into speech.

**d. Audio Transcription**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/4.png?raw=true">

This function uses the AssemblyAI API to convert audio files to text.

**e. Text Translation**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/5.png?raw=true">

This function translates the transcribed English text into the target language using the translate library.

**f. Text-to-Speech Conversion**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/6.png?raw=true">

The translated text is converted into speech using ElevenLabs' API, and the output is saved as an MP3 file.

**g. Gradio Interface**

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/7.png?raw=true">

This section creates the interactive interface using Gradio, allowing users to upload audio, view translations in text, and listen to them in the target language.

## Technologies Used
* **Gradio:** A framework for building easy-to-use user interfaces, especially for machine learning models.
* **AssemblyAI:** A speech-to-text service that converts spoken language into text.
* **Translate Library:** Handles the text translation from English to the supported languages.
* **ElevenLabs:** An API that converts text into speech with various voice options.
* **UUID and Pathlib:** For generating unique file names and managing file paths.

## How To Run the Code
Before running the code, ensure that the necessary dependencies are installed and API keys are correctly configured.

**Requirements:**
You'll need to download the requirements.txt file to install the necessary libraries. Below is an example content of the requirements.txt:

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/8.png?raw=true">

**Steps to Run the Code:**

1. **Install Dependencies:**
First, create a virtual environment and install the required packages by running:

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/9.png?raw=true">

2. **Add API Keys:**
* Replace ASSEMBLY_AI_API_KEY = "[]" with your actual AssemblyAI API key.
* Replace ELEVEN_LABS_API_KEY = "[]" with your ElevenLabs API key.
* For ElevenLabs, also provide a valid voice_id in the text_to_speech function. [SignUp on ElevenLabs](https://tinyurl.com/elevenlabs24)

3. **Run the Script:**
Launch the application using:

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/10.png?raw=true">

## Contributing
Contributions to this project is welcome! If you'd like to contribute, please follow these steps:
- Fork the project repository. 
- Create a new branch: git checkout -b feature/your-feature-name. 
- Make your changes and commit them: git commit -am 'Add your commit message'. 
- Push the changes to your branch: git push origin feature/your-feature-name. 
- Submit a pull request detailing your changes.

*Feel free to modify and adapt the project to your needs. If you have any questions or suggestions, please feel free to contact me: godswillodaudu@gmail.com*.
