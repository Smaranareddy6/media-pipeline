# 📦 Media Processing & Intent Inference Pipeline

This project demonstrates a modular pipeline that processes audio, image, and document inputs to extract structured JSON data, combining audio transcription, natural language understanding (NLU), document parsing, and speech synthesis in a unified interface.

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
| ⚠️ Tesseract Compatibility      | Installed but may still require absolute path on some systems       |
| ⚠️ Structured Field Heuristics  | Limited accuracy on noisy/foreign document layouts                   |

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

---

## ✅ Working Functionality

### 🧠 Audio Transcription + Intent Inference

- Successfully extracts transcription from voice files.
- Supports **multi-intent detection** and fallback intent recognition.

### 🪪 OCR & Document Parsing

The system extracts structured fields from image documents, including:

| Field             | Examples Extracted             |
|------------------|---------------------------------|
| `name`           | "Language Centre"               |
| `dob`            | "2/11/1976", "08/31/2014"        |
| `phone`          | "940-297-5964", "800-799-4723"   |
| `address`        | "4780 Alexander Drive"           |
| `passport_number`| "P123456AA"                      |
| `license_number` | "08311977", "125426"             |
| `email`          | "samsa698@lcfy.otago.ac.nz"      |
| `username`       | "Samsa698"                       |

---

## ⚠️ Limitations & Known Issues

| Area                       | Limitation                                                                 |
|---------------------------|----------------------------------------------------------------------------|
| 🖼️ Tesseract OCR           | Requires explicit path setup on Windows (`tesseract_cmd` workaround)       |
| 📃 Field Extraction Heuristics | Relies on regex + keyword matching; may misclassify unstructured text    |
| 🌐 Language Bias           | Intent classification currently assumes English inputs                    |
| 🎭 Ambiguous Inputs        | Ambiguity handled by labeling multiple intents, but parameters may be partial |
| 🧪 Document Noise          | Handwritten or low-res scans degrade OCR accuracy                          |

---

## 🛠️ Technologies Used

- Python 3.10+
- OpenAI Whisper (via `openai-whisper`)
- `pytesseract` (OCR)
- `gTTS` or `pyttsx3` (TTS)
- Regex + keyword heuristics for intent & field extraction

---

## 📌 Example Inputs

See the `/inputs/` folder for:

- `weather.wav`: "What’s the weather in Boston?"
- `flight.mp3`: "Book a flight from New York to LA"
- `license.jpg`: California driver license
- `passporttest.jpg`: Canadian passport scan

---

## 👥 Contributors

- Smarana Reddy – Project Lead