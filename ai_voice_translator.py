import gradio as gr

def voice_to_voice():


def audio_transcription():
    return True



def text_transaltion():
    return True


def text_to_speech():
    return True

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=,
    outputs=[gr.Audio(label="Spanish"), gr.Audio(label="Turkish"), gr.Audio(label="Japanese")]
)


if _name_=="_main_":
    demo.launch()