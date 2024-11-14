word1 = "listen"
word2 = "silent"
sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)
is_anagram = sorted_word1 == sorted_word2

if is_anagram:
    print("The words are anagram")
else:
    print("The words ar not anagram")
