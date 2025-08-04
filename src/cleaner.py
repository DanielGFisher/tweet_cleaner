import string

class DataCleaner:
    def clean_symbols(self, df, category):
        df[category] = df[category].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

        return df

    def convert_to_lowercase(self, df, category):
        df[category] = df[category].str.lower()

        return df

    def classify_biases(self,df, category):
        df[category] = df[category].map({1: 'antisemitic', 0: 'semitic'})