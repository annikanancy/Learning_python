sentence = str(input())
def word_frequency(text):
    counts = {}

    clean_text = text.lower().replace(".", "").replace(",", "")
    print(clean_text)
    words = clean_text.split()
    print(words)

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts    

print(word_frequency(sentence))