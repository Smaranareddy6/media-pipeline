import os
import json
from transcribe.transcribe import transcribe_audio
from interpret.interpret import interpret_text
from synthesize.speak import text_to_speech
from extract.extract import extract_fields

def process(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    output = {}

    abs_path = os.path.abspath(file_path)  # Ensure full path for subprocesses

    if ext in ['.wav', '.mp3', '.m4a']:
        print(f"🔍 Transcribing {abs_path}")
        transcription = transcribe_audio(abs_path)
        intent_data = interpret_text(transcription["transcription"])

        # Handle multiple intents and parameters
        intents = intent_data.get("intents", [])
        parameters = intent_data.get("parameters", {})

        # Choose one intent to speak (or fallback)
        if intents:
            spoken_intent = intents[0]
        else:
            spoken_intent = "No clear intent detected"

        base_name = os.path.basename(file_path).split('.')[0]
        response_filename = f"outputs/response_{base_name}.mp3"
        text_to_speech(f"Intent detected: {spoken_intent}", output_file=response_filename)

        output.update(transcription)
        output["intents"] = intents
        output["parameters"] = parameters

    elif ext in ['.png', '.jpg', '.jpeg']:
        print(f"🧾 Extracting text from {abs_path}")
        output = extract_fields(abs_path)
    else:
        raise ValueError("Unsupported file format.")

    # Save output JSON
    output_filename = os.path.join("outputs", os.path.basename(file_path) + ".json")
    with open(output_filename, "w") as f:
        json.dump(output, f, indent=4)

    print(f"✅ Processed: {abs_path}")
    print(f"📄 Output written to: {output_filename}")
