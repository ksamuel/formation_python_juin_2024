import string

import requests


def get_words(text):
    text = text.casefold()
    for punc in string.punctuation:
        text = text.replace(punc, " ")
    return text.split()


def count(words):
    """Count the words in a list of strings"""
    stats = {}

    for word in words:
        if word in stats:
            stats[word] += 1
        else:
            stats[word] = 1

    return stats


def get_dog_pic():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    return response.json()
