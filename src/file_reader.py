import pandas as pd

class FileReader:
    def read_file(self,path):
        df = pd.read_csv(path)

        return df

    def save_file(self,df,path):
        df.to_csv(path)

    def save_to_json(self, df, path):
        df.to_json(path, orient='records', lines=True, force_ascii=False)
