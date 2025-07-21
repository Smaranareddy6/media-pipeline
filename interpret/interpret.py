import spacy
import re 

nlp = spacy.load("en_core_web_sm")

def extract_location(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geo-Political Entity
            return ent.text
    return None

def interpret_text(text):
    text_lower = text.lower()
    intents = []
    parameters = {}

    if any(word in text_lower for word in ["weather", "forecast", "rain", "temperature", "hot", "cold"]):
        intents.append("get_weather")
    if any(word in text_lower for word in ["time", "clock", "hour", "what time"]):
        intents.append("get_time")
    if "flight" in text_lower and "book" in text_lower:
        intents.append("book_flight")
    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text_lower):
        intents.append("greet")
    if any(word in text_lower for word in ["pizza", "movie", "music", "technology", "funny", "cool", "awesome"]):
        intents.append("smalltalk")

    location = extract_location(text)
    if location:
        parameters["location"] = location

    return {
        "intents": intents if intents else ["unknown"],
        "parameters": parameters
    }
