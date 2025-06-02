# - Count word frequencies in a text file

# Pueudo code
#  def count_word_frequencies(filepath):
# 	read the content of file and iterate wthough it
# 	for word in content
# 	if word not in frequencies
# 	frequencies of word = 1
# 	else freqs[word] += 1

def count_word_frequencies(filepath):
    frequencies = {}
    with open(filepath, 'r') as source:
        for line in source:
            words = line.strip().split()
            for word in words:
                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
                print(f'frequencies: {frequencies}')
                print(f'word: {word}, frequency: {frequencies[word]}')

count_word_frequencies('MyData')
