from collections import defaultdict

def countWords(wordCount, paragraph):
    words = paragraph.split()
    for word in words:
        wordCount[word] += 1

def displayWordCount(wordCount):
    for word, count in wordCount.items():
        print(f"{word}-{count}")


if __name__ == "__main__":
    wordCount = defaultdict(int)
    paragraph = "the quick brown fox jumps over the lazy dog the quick fox"
    countWords(wordCount, paragraph)
    displayWordCount(wordCount)
