from janome.tokenizer import Tokenizer
import pandas as pd
import sys

class Sentiment:
    def __init__(self, text):
        self.text = text
        self.t = Tokenizer()

    def speech(self, partOfSpeech, dictionary):
        try:
            result = pd.DataFrame(
                {attr_name: getattr(token, attr_name) for attr_name in dir(token) if not attr_name.startswith("_")}
                for token in self.t.tokenize(self.text)
            )
            speech = result[result['part_of_speech'].str.contains(partOfSpeech,na=False)]
            speech = speech.drop(columns=['infl_form','infl_type','node_type','part_of_speech','phonetic','reading','surface'])
            speech['score'] = speech['base_form'].isin(dictionary['name']).astype(int)
            checkSpeech = dictionary[dictionary['name'].isin(speech['base_form'])]
            scoreSpeech = checkSpeech['score'].sum()
            return scoreSpeech
        except Exception as e:
            scoreSpeech = 0
            return scoreSpeech

