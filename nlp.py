import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text for analysis
text = "I am going to market with Rajesh Devi.Raju Maurya is dancer and his friends are good dancer.Sita devi is a dancer and Rima."

# Process the text with spaCy
doc = nlp(text)

# Tokenization
print("Tokenization:")
for token in doc:
    print(token.text)

# Part-of-speech tagging
print("\nPart-of-speech tagging:")
for token in doc:
    print(f"{token.text}: {token.pos_}")

# Named Entity Recognition (NER)
print("\nNamed Entity Recognition:")
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")
