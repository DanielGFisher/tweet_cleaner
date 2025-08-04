from src.cleaner import DataCleaner
from src.data_analyzer import DataAnalyser
from src.file_reader import FileReader

fr = FileReader()
da = DataAnalyser()
dc = DataCleaner()

df = fr.read_file(r"C:\Users\danie\Downloads\tweets_dataset - tweets_dataset.csv")
df = df[['Text', 'Biased']].dropna(subset=['Text'])

print(df)
print()

df = dc.clean_symbols(df, 'Text')
df = dc.convert_to_lowercase(df, 'Text')
fr.save_file(df,r"C:\Users\danie\PycharmProjectsc\twitter_project\data\cleaned_tweets.csv")

print(df)
print()

bias_count = da.biases_count(df, 'Biased')
print(bias_count)
print()

average_words = da.find_average_text_length(df, 'Text')
print(average_words)
print()

largest_tweets = da.find_largest_by_char(df, 'Text')
print(largest_tweets[['Text', 'char_length', 'Biased']])
print()

anti_semetic = da.find_bias_dataframe(df,'Biased', 1)
print(anti_semetic)

largest_antisemetic_tweets = anti_semetic.sort_values(by='char_length', ascending=False).head(3)
print(largest_antisemetic_tweets)
print()

non_antisemetic = da.find_bias_dataframe(df,'Biased', 0)

largest_non_antisemetic_tweets = non_antisemetic.sort_values(by='char_length', ascending=False).head(3)
print(largest_non_antisemetic_tweets)
print()

top_10 = da.find_top_ten_words(df, 'Text')
print(top_10)
print()

