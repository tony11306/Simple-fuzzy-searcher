from FuzzySearcher import FuzzySearcher

sc = FuzzySearcher(is_case_sensitive=True, tolerance=4)
sentence = 'coment'
print(sentence)
for word in sentence.split():
    print(sc.get_best_match(word))