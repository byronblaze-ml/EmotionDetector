import string
from stopwords import swords_list
from emotions import emotion_dict
from collections import Counter
import matplotlib.pyplot as plt
# Retrieve file
print("Enter File Location: ")
file = input()

# Cleaning Text(removing punctuation, change to lower characters)

text = open(file, encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenization - Splitting sentences into words

tokenized_words = cleaned_text.split()


# Stop Words removal

final_words = [word for word in tokenized_words if word not in swords_list]
print(final_words)

# Emotion Classifier
emotions = [emotion_dict[word] for word in final_words if word in emotion_dict]
print(emotions)
count = Counter(emotions)
print(count)

fig, ax1 = plt.subplots()
ax1.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
