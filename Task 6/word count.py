file = open("input.txt", "r")
text = file.read()
file.close()
char_count = len(text)
lines = text.split("\n")
line_count = len(lines)
words = text.split()
word_count = len(words)
word_freq = {}
for word in words:
    word = word.lower()  
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("-"*50)
print("TEXT ANALYSIS RESULT")
print("-"*50)
print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
print("\nWord Frequency:")
for word, count in word_freq.items():
    print(word, ":", count)
