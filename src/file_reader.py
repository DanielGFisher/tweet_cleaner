import pandas as pd

class FileReader:

    def read_file(self,link):
        df = pd.read_csv(link)

        return df

    def save_file(self,df):
        df.to_csv(r"C:\Users\danie\PycharmProjectsc\twitter_project\data\original_tweets.csv")
