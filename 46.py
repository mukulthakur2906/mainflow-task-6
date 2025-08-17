from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nxt = word[:i] + c + word[i+1:]
                if nxt in wordSet:
                    wordSet.remove(nxt)
                    queue.append((nxt, steps+1))
    return 0

if __name__ == "__main__":
    beginWord = input("Enter start word: ")
    endWord = input("Enter end word: ")
    wordList = input("Enter dictionary words (space separated): ").split()
    result = word_ladder(beginWord, endWord, wordList)
    if result:
        print("Shortest transformation length:", result)
    else:
        print("No transformation possible!")
