def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    text = input("Enter text: ")
    result = word_frequency(text)
    print("Word Frequency:")
    for word, count in result.items():
        print(f"{word} : {count}")
