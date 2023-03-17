import pickle
import warnings

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings('ignore')


def tokenize(column):
    tokens = word_tokenize(column)
    return [w for w in tokens if w.isalpha()]


def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w) for w in text]


def process(inp):
    stop = stopwords.words('english')
    df = pd.DataFrame(inp)
    df[0] = df[0].str.lower()
    
    df['tokenized'] = df.apply(lambda x: tokenize(x[0]), axis=1)
    df['NoStopWords'] = df['tokenized'].apply(lambda x: [item for item in x if item not in stop])
    df['lemmatized'] = df['NoStopWords'].apply(lambda x: lemmatize_text(x))
    
    texts = []
    for item in df['lemmatized']:
        texts.append(" ".join(item))
    
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', use_idf=True, norm='l2')
    matrix = tfidf_vectorizer.fit_transform(texts)
    tfidf_matrix = pd.DataFrame(matrix.toarray(), columns=tfidf_vectorizer.get_feature_names())
    return tfidf_matrix


with open('PICO_Classifier_RF', 'rb') as f:
    model = pickle.load(f)

questions = ["What causes depression?", "how can i treat depression?", "is depression chronic",
             "What does it feel like to have depression?"]

