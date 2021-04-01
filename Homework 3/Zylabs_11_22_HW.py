word_collection = input() # words are inputted into the file
word_collection = word_collection.split()  # variable inputs are split to allow multiple entries
for W_C in range(len(word_collection)):  # W_C stands for word count, for condtion is used to check for multiples by observing length
    # Using string methods such as count, the words are counted
    print(word_collection[W_C], word_collection.count(word_collection[W_C])) # Words and thier frequnceis are printed
