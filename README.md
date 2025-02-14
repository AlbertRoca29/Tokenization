# Tokenizer exploration

This repository investigates tokenizers, their behavior, and differences across various languages and implementations. The exploration includes popular NLP libraries like spaCy and NLTK.


## Table of Contents
1. [Setup](#setup)
2. [Download Models](#download-models)
3. [Custom Data](#custom-data)

---


## Setup

1) **Initialize the Repository** <br>
Clone or download the repository

2) **Install Dependencies** <br>
Install the required Python packages by running:

    ```bash
    pip install -r requirements.txt
    ```

## Download Models

### For spaCy
Download the necessary spaCy language models by running the following commands:
```bash
# English models
python -m spacy download en_core_web_sm   # English small model
python -m spacy download en_core_web_md   # English medium model

# Other languages
python -m spacy download es_core_news_sm  # Spanish small model
python -m spacy download ja_core_news_sm  # Japanese small model
python -m spacy download ca_core_news_sm  # Catalan small model

python -m spacy download en_core_web_sm   # English small model

python -m spacy download en_core_web_md   # English medium model

python -m spacy download es_core_news_sm  # Spanish small model
python -m spacy download ja_core_news_sm  # Japanese small model
python -m spacy download ca_core_news_sm  # Catalan small model
```

### For NLTK
To use NLTK, uncomment the following lines in the first code block of your `.ipynb` files:

```python
import nltk
nltk.download('punkt')
```

<a id="custom-data"></a>

## Custom Data <span style="color:red;">not implemented</span> 
If you want to use custom data, follow these steps:

1) Add sample text files for English, Spanish, and Japanese in the data/ folder. Different folder for language?

2) ?

You can use public domain books, news articles, or any text data of your choice.

