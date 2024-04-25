import nltk
import json
from random import sample

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')

def get_common_words(num_words):
    word_freq = nltk.FreqDist(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
    common_words = [word for word, _ in word_freq.most_common(num_words)]
    return common_words

def main():
    num_words = 1000
    words = get_common_words(num_words)
    
    json_data = [{"id": idx, "word": word} for idx, word in enumerate(words)]
    
    with open('./data/words.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    main()
