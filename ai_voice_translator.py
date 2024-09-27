import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import uuid
from pathlib import Path

# Global configuration (Move API keys here for security and reuse)
ASSEMBLY_AI_API_KEY = "[]"  # Replace with your AssemblyAI API key
ELEVEN_LABS_API_KEY = "[]"  # Replace with your ElevenLabs API key

# Supported languages
SUPPORTED_LANGUAGES = {
    "Spanish": "es",
    "Turkish": "tr",
    "Japanese": "ja",
    "French": "fr",
    "German": "de",
    "Chinese": "zh"
}

def voice_to_voice(audio_file):
    """
    Main function to handle voice-to-voice translation and speech synthesis.
    Translates speech to 6 popular languages.
    
    :param audio_file: Path to the input audio file.
    :return: Paths to the generated audio files and translated texts.
    """
    try:
        # Step 1: Transcribe audio into text
        transcription_response = audio_transcription(audio_file)

        if transcription_response.status == aai.TranscriptStatus.error:
            raise gr.Error(f"Transcription Error: {transcription_response.error}")

        text = transcription_response.text

        # Step 2: Translate text to different languages
        translated_texts = {}
        translated_audio_paths = {}
        
        for lang_name, lang_code in SUPPORTED_LANGUAGES.items():
            translation = text_translation(text, lang_code)
            translated_texts[lang_name] = translation
            translated_audio_paths[lang_name] = text_to_speech(translation)

        return translated_audio_paths, translated_texts

    except Exception as e:
        raise gr.Error(f"An error occurred: {e}")


def audio_transcription(audio_file):
    """
    Transcribes audio to text using AssemblyAI.
    
    :param audio_file: Path to the input audio file.
    :return: Transcription object from AssemblyAI.
    """
    aai.settings.api_key = ASSEMBLY_AI_API_KEY
    transcriber = aai.Transcriber()

    try:
        transcription = transcriber.transcribe(audio_file)
        return transcription
    except Exception as e:
        raise RuntimeError(f"Error during transcription: {e}")


def text_translation(text, target_lang_code):
    """
    Translates English text to the target language.
    
    :param text: The original text in English.
    :param target_lang_code: The target language code (e.g., "es" for Spanish).
    :return: Translated text in the target language.
    """
    try:
        translator = Translator(from_lang="en", to_lang=target_lang_code)
        translated_text = translator.translate(text)
        return translated_text

    except Exception as e:
        raise RuntimeError(f"Error during translation: {e}")


def text_to_speech(text):
    """
    Converts text to speech using ElevenLabs API and saves the audio file.
    
    :param text: The text to be converted to speech.
    :return: Path to the generated audio file.
    """
    try:
        client = ElevenLabs(api_key=ELEVEN_LABS_API_KEY)

        # API call to generate speech from text
        response = client.text_to_speech.convert(
            voice_id="[]",  # Replace with valid Voice ID
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.8,
                style=0.5,
                use_speaker_boost=True,
            ),
        )

        # Generate a unique file name for the output MP3 file
        save_file_path = Path(f"{uuid.uuid4()}.mp3")

        # Write audio chunks to file
        with open(save_file_path, "wb") as audio_file:
            for chunk in response:
                if chunk:
                    audio_file.write(chunk)

        print(f"Audio saved at {save_file_path}")
        return save_file_path

    except Exception as e:
        raise RuntimeError(f"Error during text-to-speech conversion: {e}")


# Gradio Interface

def create_interface():
    """
    Creates a Gradio interface for the voice-to-voice translation app.
    """
    audio_input = gr.Audio(
        type="filepath",  # Removed the `source` argument, keeping `type` as `filepath`
        label="Record or Upload Audio"
    )

    # Now alternate audio outputs and their respective text outputs
    outputs = []
    for lang in SUPPORTED_LANGUAGES:
        outputs.append(gr.Audio(label=f"{lang} Translation Audio"))
        outputs.append(gr.Textbox(label=f"{lang} Translation Text", interactive=False))

    def translate_and_play(audio_file):
        """
        Function that handles the translation and playback, returns audio paths and translated texts.
        """
        translated_audio_paths, translated_texts = voice_to_voice(audio_file)

        # Flatten the list of outputs (alternate audio and text)
        output_values = []
        for lang in SUPPORTED_LANGUAGES:
            output_values.append(translated_audio_paths[lang])
            output_values.append(translated_texts[lang])

        return output_values

    # App Heading
    title = "LinguaSpeak: Record English and Hear Popular Translations"
    description = "Translates spoken English into 6 popular languages: Spanish, Turkish, Japanese, French, German, and Chinese."

    # Gradio layout
    demo = gr.Interface(
        fn=translate_and_play,
        inputs=audio_input,
        outputs=outputs,
        title=title,
        description=description,
        allow_flagging="never",
        live=True
    )

    return demo


if __name__ == "__main__":
    demo = create_interface()
    demo.launch()