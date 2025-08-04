import pandas as pd
import numpy as np
from pandas.io.sas.sas_constants import column_data_length_length


class DataAnalyser:
    def biases_count(self, df, category):
        return df[category].value_counts()

    def find_average_text_length(self, df, category):
        df['word_count'] = df[category].apply(lambda x: len(str(x).split()))
        return df['word_count'].mean()

    def find_largest_by_char(self, df, category):
        df['char_length'] = df[category].apply(lambda x: len(str(x)))
        max_length = df['char_length'].sort_values(ascending=False).head(3)
        return max_length

    def find_top_ten_words(self, df, category):
        pass

    def find_shouts(self, df, category):
        words = df[category].dropna().str.split()
        return words[words.str.isupper()]
