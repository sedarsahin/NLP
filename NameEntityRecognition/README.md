# Named Entity Recognition (NER) Tutorial using NLTK

This repository contains code and explanations for a tutorial on Named Entity Recognition (NER) using Python's Natural Language Toolkit (NLTK).

## Overview

Named Entity Recognition (NER) is a crucial task in Natural Language Processing (NLP) that involves identifying and categorizing entities within 
text data, such as names of people, organizations, locations, etc. This tutorial showcases how to perform NER using NLTK on a Wikipedia article about "Apple Inc."

## Tutorial Contents

1. **Retrieving and Preprocessing Data**
   - Utilizing the Wikipedia API to retrieve text data.
   - Tokenizing text into sentences and words using NLTK's `sent_tokenize` and `word_tokenize`.

2. **Part-of-Speech Tagging**
   - Tagging each tokenized sentence with parts of speech using NLTK's `pos_tag`.

3. **Named Entity Recognition**
   - Extracting and categorizing named entities using `ne_chunk_sents`.

4. **Visualizing NER Categories**
   - Visualizing the distribution of detected NER categories using Matplotlib's pie chart.

## Code and Exercises

The tutorial code is organized into sections, each corresponding to a specific step in the NER process. 
Additionally, exercises are provided to further explore and experiment with the concepts presented in the tutorial.

## Link to Step-by-Step

https://dshub.gitbook.io/ds-hub/machine-learning/natural-language-processing/name-entity-recognition-ner


## Files

- `ner_apple.py`: Python script containing the tutorial code and exercises.
- `ner_apple.ipynb`: Interactive Python Notebook containing the tutorial code and exercises for Jupyter Notebook users.
- `README.md`: This README file providing an overview of the tutorial.

## Usage

To run the tutorial code, follow these steps:

1. Ensure you have Python installed along with the required libraries (`nltk`, `wikipediaapi`, `matplotlib`).
2. Open the `ner_apple.py` file and execute it in a Python environment, or `ner_apple.ipynb` in Jupyter Notebook


## Contribution

Feel free to contribute by:
- Adding more exercises or expanding on existing ones.
- Improving code readability or explanations.
- Sharing feedback or suggestions for enhancement.

## Author

Created by Sedar Sahin

## License

This project is licensed under MIT. You're encouraged to use, modify, and share this content.
