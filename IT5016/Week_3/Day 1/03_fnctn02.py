def function02(word1,word2):
    len1 = len(word1)
    len2= len(word2)
    shorter_length = min(len1,len2)
    return shorter_length

word1= input("Enter first word: ")
word2 = input("Enter second letter: ")
print(function02,(word1,word2))