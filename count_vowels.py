sentence = "this is my sentence with some vowels"
vowel_total = 0
for letter in sentence:
	if letter in "aeoiu":
		vowel_total +=1
		
print(vowel_total, " is the amount of vowels in the sentence.")
