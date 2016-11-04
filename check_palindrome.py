#word = "racecar"
#word = "racecars"
word = "madamimadam"
length_word = len(word)
palindrome = False

for letter in word:
	if letter == word[length_word-1]:
		print("comparing ", letter," with ", word[length_word-1])
		length_word -= 1
		palindrome = True
	else:
		palindrome = False
		print("comparing ", letter," with ", word[length_word-1])
		break

	
if palindrome == True:
	print("Word ", word, " is a palindrome!", palindrome)
elif palindrome == False:
	print("word is not a palindrome is", palindrome)
