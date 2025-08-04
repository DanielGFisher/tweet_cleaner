import pandas as pd

class FileReader:
    def read_file(self,path):
        df = pd.read_csv(path)

        return df

    def save_file(self,df,path):
        df.to_csv(path)

    def save_to_json(self, df, path):
        try:
            df.to_json(path, orient='records', lines=True, force_ascii=False)
            print(f"JSON file saved successfully at {path}")
        except Exception as e:
            print(f"Error saving JSON file to {path}: {e}")