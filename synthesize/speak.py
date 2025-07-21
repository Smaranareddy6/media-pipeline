from gtts import gTTS

def text_to_speech(text, output_file="outputs/response.mp3"):
    tts = gTTS(text)
    tts.save(output_file)
    return output_file
