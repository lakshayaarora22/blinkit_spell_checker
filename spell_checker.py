import time
import nltk

class BlinkItSpellingChecker:

    def __init__(self):
        self.blank_spaces = 0
        self.word_cache = {}
        self.word_set = set(nltk.corpus.words.words())
        
        # Read content from file
        with open("blinkit_sentences.txt", "r") as file:
            content = file.read()
        
        self.check(content)

    def check(self, content):
        space_count = content.count(" ")

        if space_count != self.blank_spaces:
            self.blank_spaces = space_count
            start_time = time.perf_counter()
            for word in content.split():
                if word.lower() not in self.word_cache:
                    if word.lower() not in self.word_set:
                        print(f"Misspelled word: {word}")
                    self.word_cache[word.lower()] = False  # Cache miss
                else:
                    if not self.word_cache[word.lower()]:
                        print(f"Misspelled word: {word}")
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Time taken : {elapsed_time / len(content.split()):.8f} seconds")

BlinkItSpellingChecker()