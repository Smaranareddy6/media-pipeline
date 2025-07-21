# 📦 Media Processing & Intent Inference Pipeline

This project demonstrates a modular pipeline that processes audio, image, and document inputs to extract structured JSON data. It combines transcription, NLU (natural language understanding), OCR, and speech synthesis into a unified and flexible interface.

---

## 🎯 Project Goals

| Feature                          | Goal                                                                 |
|----------------------------------|----------------------------------------------------------------------|
| ✅ Media Handling                | Read `.wav`, `.mp3`, `.m4a`, `.png`, `.jpg`, `.jpeg` files           |
| ✅ NLU & Data Extraction         | Convert unstructured media into structured JSON                      |
| ✅ Unified Interface             | Single CLI entry point auto-routes media types                       |
| ✅ Audio Transcription           | Converts voice to text using OpenAI Whisper                         |
| ✅ Intent Detection              | Identifies one or more user intents using basic pattern matching     |
| ✅ Speech Synthesis              | Responds with synthesized speech audio                              |
| ✅ OCR & Field Extraction        | Parses documents and IDs for structured fields                       |
| ⚠️ Tesseract Compatibility      | Installed but may require absolute path configuration               |
| ⚠️ Structured Field Heuristics  | Regex-based heuristics may not work with noisy layouts               |

---

## 📁 Folder Structure

```
media-pipeline/
├── inputs/                # Drop your input files here
├── outputs/               # JSON and audio results are stored here
├── extract/               # Document field extraction (OCR)
├── transcribe/            # Audio transcription (Whisper)
├── interpret/             # Intent classification + entity parsing
├── synthesize/            # Text-to-speech synthesis
├── orchestrator/          # Unified file-type router
├── run_pipeline.py        # Entry point script
```

---

## 🚀 How to Run

### 1. Clone this Repository

```bash
git clone https://github.com/Smaranareddy6/media-pipeline.git
cd media-pipeline
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

Also install **Tesseract OCR**:
- 📦 Windows: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
- Add to Python:
  ```python
  import pytesseract
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```

### 3. Add Files to `/inputs/`

Supported formats:
- Audio: `.wav`, `.mp3`, `.m4a`
- Images: `.png`, `.jpg`, `.jpeg`

### 4. Run the Pipeline

```bash
python run_pipeline.py
```

The system will process each file and output structured JSON to the `/outputs/` folder.

---

## ✅ What Works

### 🧠 Audio Transcription + Intent Detection
- Supports multi-intent extraction.
- Returns transcription, intent(s), and key parameters.

### 🪪 Document Parsing (OCR)
- Extracts from common formats like ID cards, passports, licenses, and bills.

| Field             | Examples Extracted             |
|------------------|---------------------------------|
| `name`           | "Language Centre", "Alexander Drive" |
| `dob`            | "2/11/1976", "08/31/2014"        |
| `phone`          | "940-297-5964", "800-799-4723"   |
| `address`        | "4780 Alexander Drive"           |
| `passport_number`| "P123456AA"                      |
| `license_number` | "08311977", "125426"             |
| `email`          | "samsa698@lcfy.otago.ac.nz"      |
| `username`       | "Samsa698"                       |

---

## ⚠️ Limitations & Notes

| Area                       | Limitation                                                                 |
|---------------------------|----------------------------------------------------------------------------|
| 🖼️ Tesseract OCR           | Requires absolute path on Windows                                          |
| 🔍 Field Extraction Logic  | Uses regex patterns; performance may degrade on scanned/foreign-language docs |
| 🎧 Whisper Transcription   | Requires `ffmpeg`; performance may vary with background noise              |
| 🧪 Document Variance       | Some layout types (e.g., bills or medical cards) may be inconsistently parsed |
| ❓ Ambiguity Handling       | When input implies multiple intents, both are captured as a list           |

---

## 🔄 How to Swap Modules

| Component     | Replace With                                   |
|---------------|------------------------------------------------|
| Transcriber   | Replace `transcribe/transcribe.py` with Google Speech, Vosk, etc. |
| Interpreter   | Replace `interpret/interpret.py` with Rasa, spaCy, or LLM-based intent parser |
| Synthesizer   | Modify `synthesize/speak.py` to use Amazon Polly, ElevenLabs, etc. |
| OCR Engine    | Swap `pytesseract` with AWS Textract, EasyOCR, PaddleOCR |

Each component follows a modular function-call structure and can be swapped with minimal interface changes.

---

## 🧠 Assumptions Made

- All images are assumed to be printed (not handwritten).
- English is the expected language for both voice and documents.
- Filenames are treated as unique IDs for linking input/output.
- If fields conflict, most recently matched value is retained.
- For audio: fallback intent is `unknown` if no match is found.

---

## 📌 Sample Inputs

Examples included in the `/inputs/` directory:
- `weather.wav` – Audio asking for weather
- `flight.mp3` – Requesting flight booking
- `utilitybill.png` – Scanned electricity bill
- `passporttest.jpg` – Canadian passport image

---

## 👤 Author

- Smarana Reddy – Full-stack Developer | [LinkedIn](https://www.linkedin.com/in/smarana/)
