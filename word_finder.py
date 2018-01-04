from nltk.corpus import wordnet
import itertools

def generate_word_permutations(given_letters):
	english_words = []

	minimum_word_length = 3
	for count in range(minimum_word_length, len(given_letters)+1):
		# find all permutations of the given_letters.
		for item in itertools.product(given_letters, repeat=count):
			# check if it's an english word first...
			potential_word = "".join(item)
			if wordnet.synsets(potential_word):
				# check if there are no letter duplicates...
				letter_valid = True
				temp_letters = given_letters
				for letter in potential_word:
					if letter in temp_letters:
						temp_letters = temp_letters.replace(letter, "", 1)
					else:
						letter_valid = False
				# then show it...
				if letter_valid:
					english_words.append(potential_word)

	# remove word duplicates
	possible_words = []

	for word in english_words:
		if word not in possible_words:
			possible_words.append(word)
	print (possible_words)

if __name__ == '__main__':
	run_script_infinitely = True
	while run_script_infinitely:
		given_letters = input("Enter your letters: ")
		generate_word_permutations(given_letters)