# EXERCISE 6.4: Random text generator (Markov Chain)

import random


text_lines = [
    "the fire and the wind",
    "the fire is warm and bright",
    "the wind is cold"
]


# process_line

def process_line(line):
    words = line.split()
    full_words = ["BEGIN"] + words + ["END"]

    pairs = []

    for index in range(len(full_words) - 1):
        current_word = full_words[index]
        next_word = full_words[index + 1]
        pairs.append((current_word, next_word))

    return pairs


# process_textfile()

def process_textfile(f):
    chain = {}

    for line in f:
        pairs = process_line(line)

        for current_word, next_word in pairs:
            if current_word not in chain:
                chain[current_word] = []

            chain[current_word].append(next_word)

    return chain


# generate random line

def generate_line(chain):
    current_word = "BEGIN"
    sentence_words = []

    while current_word != "END":
        possible_next_words = chain[current_word]
        next_word = random.choice(possible_next_words)

        if next_word != "END":
            sentence_words.append(next_word)

        current_word = next_word

    return " ".join(sentence_words)


markov_chain = process_textfile(text_lines)

print(f"Input text lines: {text_lines}")

for key, value in markov_chain.items():
    print(f"{key}: {value}")

for sentence_number in range(1, 4):
    random_sentence = generate_line(markov_chain)
    print(f"Sentence {sentence_number}: {random_sentence}")