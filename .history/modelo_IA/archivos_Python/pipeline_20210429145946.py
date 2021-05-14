import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
import spacy
import numpy as np
import pickle
import random
from config import MAXLEN_SEQ
from config import PADDING
from config import MODEL_PATH
from config import LABELS
from config import RESPUESTAS
from config import TOKENIZER_PATH


class Pipeline(object):
    def __init__(self):
        self.model = tf.keras.models.load_model(MODEL_PATH)
        self.excluded_words = ['un', 'uno', 'unas', 'una', 'unos']

    def preprocess_question(self, question):
        sequence = [' '.join([word for word in question.split() if not word in self.excluded_words])]
        return sequence

    def transform_input_question(self, sequence):
        with open(TOKENIZER_PATH, 'rb') as handle:
            tokenizer = pickle.load(handle)
        tokenized_sequence = tokenizer.texts_to_sequences(sequence)
        sequence_docs = pad_sequences(tokenized_sequence, maxlen=MAXLEN_SEQ, padding=PADDING)
        return sequence_docs

    def make_predictions(self, sequence_docs):
        return list(LABELS.keys())[np.argmax(self.model.predict(sequence_docs))]

    def run_model(self, question):
        preprocessed_question = self.preprocess_question(question=question)
        sequence_docs = self.transform_input_question(sequence=preprocessed_question)
        prediction = self.make_predictions(sequence_docs=sequence_docs)
        response = random.choice(RESPUESTAS[prediction])
        if '{}' in response.split():
            return response.format('Daniel')
        else:
            return response