import json

from src.cleaner import DataCleaner
from src.data_analyzer import DataAnalyser
from src.file_reader import FileReader
from src.report import ReportBuilder
fr = FileReader()
da = DataAnalyser()
dc = DataCleaner()

df = fr.read_file(r"C:\Users\danie\Downloads\tweets_dataset - tweets_dataset.csv")
df = df[['Text', 'Biased']].dropna(subset=['Text'])

df = dc.clean_symbols(df, 'Text')
df = dc.convert_to_lowercase(df, 'Text')
df['char_length'] = df['Text'].apply(lambda x: len(str(x)))

fr.save_file(df, r"C:\Users\danie\PycharmProjectsc\twitter_project\data\cleaned_tweets.csv")

bias_count = da.biases_count(df, 'Biased')
average_words = da.find_average_text_length(df, 'Text')

anti_semetic = da.find_bias_dataframe(df, 'Biased', 1)
average_anti = da.find_average_text_length(anti_semetic, 'Text')

non_antisemetic = da.find_bias_dataframe(df, 'Biased', 0)
average_non_anti = da.find_average_text_length(non_antisemetic, 'Text')

largest_antisemetic_tweets = anti_semetic.sort_values(by='char_length', ascending=False).head(3)
largest_non_antisemetic_tweets = non_antisemetic.sort_values(by='char_length', ascending=False).head(3)

top_10 = da.find_top_ten_words(df, 'Text')

rb = ReportBuilder(df, bias_count, average_words, average_anti, average_non_anti,
                   top_10, largest_antisemetic_tweets, largest_non_antisemetic_tweets)

report = rb.build_report()

with open(r"C:\Users\danie\PycharmProjectsc\twitter_project\data\report.json", "w") as f:
    json.dump(report, f, indent=4)



