import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Define keywords and their associated intents
intent_mapping = {
    "create": "Create",
    "add": "Create",
    "update": "Update",
    "edit": "Update",
    "delete": "Delete",
    "remove": "Delete",
    "login": "Login",
    # Add more keywords and intents as needed
}

# Define a function for intent recognition
def recognize_intent(text):
    # Process the input text with spaCy
    doc = nlp(text.lower())  # Convert text to lowercase for case-insensitive matching

    # Initialize intent as None
    intent = None

    # Check for keywords in the processed text
    for token in doc:
        if token.text in intent_mapping:
            intent = intent_mapping[token.text]
            break

    return intent

# Example usage
user_input = "Please add a new user."
recognized_intent = recognize_intent(user_input)

if recognized_intent:
    print(f"Intent: {recognized_intent}")
else:
    print("Intent not recognized.")
