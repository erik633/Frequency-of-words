import string

file_name = str(input("Enter name of the txt file you would like to scan: "))  # enter document.txt docoment
def word_counter (file_name, length, n):
    text = open(file_name) #read txt document

    split_text = text.read().split()  # read the file, returns a list of strings
    split_text = [''.join(c for c in split_text if c not in string.punctuation) for split_text in split_text] # remove punctuation from list
    dict = {}
    for word in split_text: #get frequency of words with the length of "length" in text/document
        if len(word) == length:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    reversed_list = []
    for key, value in dict.items(): #iterate through dictionary and append tuples to the list
        reversed_list.append((value, key))
    reversed_list.sort(reverse=True)
    number_of_words = 0
    for item in reversed_list: # print "n" number of items/tupples
        number_of_words += 1
        if number_of_words <= n:
            print(item[::-1]) # reverse the tuple
        else:
            break
    if number_of_words == 0: #condition if there are no words with length of characters
        print(f'No words with {length} characters were found.')


word_counter(file_name, 3, 10)


