import regex as re
import joblib
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
spam_keywords = []
greeting_words = []
with open('spam_keywords.txt', 'r', encoding='utf-8') as file:
    # Read each line in the file and add it to the list
    for line in file:
        spam_keywords.append(line.strip())
with open('greeting_words.txt', 'r', encoding='utf-8') as file:
    # Read each line in the file and add it to the list
    for line in file:
        greeting_words.append(line.strip())


def count_distinct_words(message):
    # Convert the message to lowercase and remove punctuation
    message = message.lower()
    message = ''.join(c for c in message if c.isalpha() or c.isspace())

    # Split the message into words
    words = message.split()

    # Use a set to count the distinct words
    distinct_words = set(words)

    # Return the count of distinct words
    return len(distinct_words)


# Load the trained Random Forest Classifier model
# Replace with the actual path
model_path = 'random_forest_model.joblib'
clf = joblib.load(model_path)


def extract_features(message):

    http_pattern = re.compile(
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
    phone_pattern = re.compile(
        r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{10}')

    length = len(message)
    has_http_link = 1 if http_pattern.search(message) else 0
    has_phone_number = 1 if phone_pattern.search(message) else 0

    keywords_in_message = [
        word for word in spam_keywords if word in message.lower()]
    keywords = 1 if keywords_in_message else 0

    greeting_words_in_message = [
        word for word in greeting_words if word in message.lower()]
    has_greeting_words = 1 if greeting_words_in_message else 0

    distinct_words = count_distinct_words(message)

    return (
        has_http_link,
        has_phone_number,
        length,
        has_greeting_words,
        distinct_words,
        keywords
    )


def test_predict():
    # Test cases for the predict function

    # Test a legitimate message
    assert predict("This is a legitimate message.") == "Ham"

    # Test a known spam message

    # Test a message with a phone number
    assert predict("Call me at 123-456-7890.") == "Spam"

    # Test a message with a link
    assert predict("Visit our website at www.example.com.") == "Spam"

    # Test a message with keywords
    assert predict("Make money fast with this opportunity!") == "Spam"

    # Test a message with greeting words
    assert predict("Hello there! How are you?") == "Ham"

    # Add more test cases as needed

    print("All test cases passed!")


def predict(message):
    # Preprocess the input message and extract features
    features = extract_features(message)

    # Make predictions using the loaded model
    prediction = clf.predict([features])  # Pass features as a list

    # Return the predicted label (0 or 1)
    return "Spam" if prediction[0] else "Ham"


if __name__ == '__main__':

    if len(sys.argv) > 1:
        user_inputs = sys.argv[1:]
    else:
        exit()

    results = {}
    for i in user_inputs:
        results[i] = predict(i)
    print(results)
    test_predict()
