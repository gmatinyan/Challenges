def is_anagram_of_polindrom(word):
	"""Is the word an anagram of polindrom?"""

	seen = {}

	for letter in word:
		value = seen.get(letter, 0)
		value += 1

	count_of_odds = 0

	for value in seen.values():
		if value % 2 != 0:
			count_of_odds += 1

	if count_of_odds <= 1:
		return True
	else:
		return False


print is_anagram_of_polindrom("abbc")
print is_anagram_of_polindrom("racecar")
print is_anagram_of_polindrom("aaa")
print is_anagram_of_polindrom("a")