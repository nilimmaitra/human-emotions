import json
from collections import defaultdict
from textblob import TextBlob

def load_emotion_words(human_emotions):
    with open(human_emotions, 'r') as f:
        emotion_words = json.load(f)
    return emotion_words

def count_emotion_words(text, emotion_words):
    word_counts = defaultdict(int)
    for word in text.split():
        for emotion, words in emotion_words.items():
            if word.lower() in words:
                word_counts[emotion] += 1
    return word_counts

def analyze_text(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def detect_emotions(text, emotion_words):
    word_counts = count_emotion_words(text, emotion_words)
    if not word_counts:
        polarity = analyze_text(text)
        if polarity > 0:
            word_counts['happy'] = 1
        elif polarity < 0:
            word_counts['sad'] = 1
        else:
            word_counts['neutral'] = 1
    return word_counts

def main():
    emotion_words = load_emotion_words('human_emotions.json')
    user_text = input('Enter your text: ')
    emotion_scores = detect_emotions(user_text, emotion_words)
    print('Emotion scores:', emotion_scores)
    overall_emotion = max(emotion_scores, key=emotion_scores.get)
    print('Overall emotion:', overall_emotion)

if __name__ == '__main__':
    main()
