import wikipediaapi
from nltk.chunk import ne_chunk_sents
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from collections import defaultdict
import matplotlib.pyplot as plt


## Step 1: Retrieving and Preprocessing Data ##

# Wikipedia API to retrieve an article about "Tesla Inc." #
user_agent='MyProjectName (merlin@example.com)'
wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='en')
article = wiki_wiki.page('Apple Inc.')
# print(article.title)
# print(article.summary)

# Preprocessing Data ##
# Tokenize the text into sentences
sentences = sent_tokenize(article.text)
print(sentences[:3])

# Further tokenize each sentence into words
token_sentences = [word_tokenize(sent) for sent in sentences]
print(token_sentences[0])

# # Exercise 1:
# # Print the first five sentences
# print(sentences[:5])

# ------------------------------------------------------------------------ #

## Step 2: Part-of-Speech Tagging ##
pos_sentences = [pos_tag(w) for w in token_sentences]
print(pos_sentences[0])

# # Exercise 2:
# # Print the POS tags for the first ten sentences
# for sent in pos_sentences[:10]:
#     print(sent)

# ------------------------------------------------------------------------ #

## Step 3: Named Entity Recognition Name Entity Recognition ##
# Create the named entity chunks
chunked_sentences = ne_chunk_sents(pos_sentences)

# Create a defaultdict for NER categories
ner_categories = defaultdict(int)

# Count and categorize named entities
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, 'label'):
            ner_categories[chunk.label()] += 1


# # Exercise 3:
# # Identify and print the named entities detected
# for sent in chunked_sentences:
#     for chunk in sent:
#         if hasattr(chunk, 'label'):
#             print(chunk)

# # Count and display the number of named entities for different categories
# print(ner_categories)

# ------------------------------------------------------------------------ #

## Step 4: Visualizing NER Categories ##
# Create labels and values for the pie chart
labels = list(ner_categories.keys())
values = list(ner_categories.values())

# Plot the pie chart
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.show()

# # Exercise 4:
# # Customize the pie chart
# # Display percentages with no decimal points
# plt.pie(values, labels=labels, autopct='%1.0f%%', startangle=140)
# plt.show()