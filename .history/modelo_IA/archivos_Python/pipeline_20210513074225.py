import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import random

from .config import spellchecker
from .config import MODEL_PATH
from .config import PADDING
from .config import LABELS
from .config import RESPUESTAS
from .config import TOKENIZER_PATH
from .config import EXCLUDED_CHARACTERS


class Pipeline(object):
    def __init__(self, user_name):
        self.model = tf.keras.models.load_model(MODEL_PATH)
        self.user_name = user_name
        self.excluded_characters = EXCLUDED_CHARACTERS
        self.spellchecker = spellchecker

    def _remove_excluded_characters(self, question:str):
        sequence = [' '.join([word.lower() for word in question.split() if not word in self.excluded_characters])]
        return sequence

    def _spell_check(self, question: str) -> str:
        question = question.split()
        to_correct = self.spellchecker.unknown(question)
        corrected = [self.spellchecker.correction(word) if word in to_correct else word for word in question]
        return ' '.join(corrected)

    def preprocess_question(self, question: str):
        return self._remove_excluded_characters(self._spell_check(question))

    def transform_input_question(self, sequence):
        with open(TOKENIZER_PATH, 'rb') as handle:
            tokenizer = pickle.load(handle)
        tokenized_sequence = tokenizer.texts_to_sequences(sequence)
        sequence_docs = pad_sequences(tokenized_sequence, maxlen=self.model.input.get_shape()[1], padding=PADDING)
        return sequence_docs

    def make_predictions(self, sequence_docs):
        prediction = np.argmax(self.model.predict(sequence_docs))
        return list(LABELS.keys())[prediction]

    def run_model(self, question):
        preprocessed_question = self.preprocess_question(question=question)
        sequence_docs = self.transform_input_question(sequence=preprocessed_question)
        prediction = self.make_predictions(sequence_docs=sequence_docs)
        try:
            response = random.choice(RESPUESTAS[prediction])
        except:
            response = f"Tu intención -> {prediction}"
        else:
            if not response:
                response = f"Tu intención -> {prediction}"
            else:
                if '{}' in response.split():
                    response = response.format(self.user_name)
        return response