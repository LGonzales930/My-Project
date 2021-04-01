word_collection = input()
word_collection = word_collection.split()  # variable inputs are split to allow multiple entries
for W_C in range(len(word_collection)):  # W_C stands for word count
    print(word_collection[W_C], word_collection.count(word_collection[W_C])) # Words and thier frequnceis are printed