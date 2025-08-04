from collections import Counter

class DataAnalyser:
    def biases_count(self, df, category):
        return df[category].value_counts()

    def find_average_text_length(self, df, category):
        df['word_count'] = df[category].apply(lambda x: len(str(x).split()))
        return df['word_count'].mean()

    def find_largest_by_char(self, df, category):
        df['char_length'] = df[category].apply(lambda x: len(str(x)))
        max_length = df.sort_values(by='char_length', ascending=False).head(3)
        return max_length

    def find_top_ten_words(self, df, category):
        all_words = ' '.join(df[category]).split()
        word_counts = Counter(all_words)
        ten_words = [word for word, count in word_counts.most_common(10)]
        return ten_words

    def find_shouts(self, df, category):
        pass

    def find_bias_dataframe(self, df, category, val):
        return df[df[category] == val]
