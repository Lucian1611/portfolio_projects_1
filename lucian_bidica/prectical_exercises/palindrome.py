vocabulary = [line.strip().lower() for line in open('words.txt', "r")]
vocabulary
count = 0
for word in vocabulary:
    if word == word[::-1]:
        count += 1
        print(word)
print(f'in the "words.txt" file we found {count} palindrome words')
