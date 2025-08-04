import pandas as pd

class FileReader:
    def read_file(self,path):
        df = pd.read_csv(path)

        return df

    def save_file(self,df,path):
        df.to_csv(path)
