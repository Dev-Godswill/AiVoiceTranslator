import gradio as gr
import assemblyai as ai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

def voice_to_voice(audio_file):

    #transcribe audio
    transcription_response= audio_transcription(audio_file)

    if transcription_response.status == aai.Transcriptions.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.txt

    es_translation, tr_translation= text_translation(text)



def audio_transcription(audio_file):

    aai.settings.api_key = ""

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(audio_file)

    return transcription



def text_transaltion():
    
    translator_es = Translator(from_lang="en", to_lang="es")
    es_text=translator_es.translate(text)

    translator_tr = Translator(from_lang="en", to_lang="tr")
    tr_text=translator_tr.translate(text)

    return es_text, tr_text


def text_to_speech():
    return True


audio_input= gr.Audio(
    sources=["microphone"],
    type="filepath"
)

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Spanish"), gr.Audio(label="Turkish"), gr.Audio(label="Japanese")]
)


if _name_=="_main_":
    demo.launch()