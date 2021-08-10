from operator import itemgetter

file = open('desolation_row.txt', 'r').read()
punctuation = '.,?!;:"'

for mark in punctuation:
    file = file.replace(mark, '')
words = file.lower().strip().split()

word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

sorted_counts = sorted(word_counts.items(), key=itemgetter(1), reverse=True)
print(f"{'Word':15}{'Count':5}")
print("=" * 20)

for k, v in sorted_counts[:10]:
    print(f"{k:15}{v:5}")

print("=" * 20)

total_words = len(words)
unique_words = len(word_counts)
unique_proportion = unique_words / total_words
print(f"Total Words: {total_words}")
print(f"Unique Words: {unique_words}")
print(f"Percent unique: {unique_proportion:.2%}")