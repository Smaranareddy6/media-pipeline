import pytesseract
import re
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_fields(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
    except Exception as e:
        return {"error": f"Failed to read image: {str(e)}"}

    structured = {}
    text = text.strip()
    
    # --- Extract Full Name ---
    name_match = re.search(r"(?:Name|Nom|Surname|Given names?)[:\s|]*([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)", text, re.IGNORECASE)
    if name_match:
        structured['name'] = name_match.group(1)
    else:
        # Fallback: first reasonable two-word capitalized phrase
        fallback_names = re.findall(r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b", text)
        if fallback_names:
            structured['name'] = fallback_names[0]

    # --- Extract Date of Birth ---
    dob_match = re.search(r"(?:Date of Birth|DOB)?[:\s]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", text, re.IGNORECASE)
    if dob_match:
        structured['dob'] = dob_match.group(1)

    # --- Extract Email ---
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    if email_match:
        structured['email'] = email_match.group(0)

    # --- Extract Phone ---
    phone_match = re.search(r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})", text)
    if phone_match:
        structured['phone'] = phone_match.group(0)

    # --- Extract Passport Number ---
    passport_match = re.search(r"\bP[A-Z0-9]{6,9}\b", text)
    if passport_match:
        structured['passport_number'] = passport_match.group(0)

    # --- Extract License Number ---
    license_match = re.search(r"\b[0-9]{6,9}\b", text)
    if license_match:
        structured['license_number'] = license_match.group(0)

    # --- Extract Username (common in student cards) ---
    username_match = re.search(r"(?:Username|USERNAME)[:\s]*([a-zA-Z0-9_.+-]+)", text)
    if username_match:
        structured['username'] = username_match.group(1)

    # --- Extract Address ---
    address_match = re.search(r"(\d{3,6}\s+[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\s(?:Street|St|Road|Rd|Avenue|Ave|Drive|Dr|Blvd|Lane|Ln|Way))", text)
    if address_match:
        structured['address'] = address_match.group(1)

    # --- Final cleanup: remove invalid filler values ---
    for k in list(structured):
        if structured[k].lower() in {'passport', 'student', 'driver', 'license', 'payable', 'winter season'}:
            del structured[k]

    return {
        "extracted_text": text,
        "structured_fields": structured
    }
