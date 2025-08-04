from src.cleaner import DataCleaner
from src.data_analyzer import DataAnalyser
from src.file_reader import FileReader

fr = FileReader()
da = DataAnalyser()
dc = DataCleaner()

df = fr.read_file(r"C:\Users\danie\Downloads\tweets_dataset - tweets_dataset.csv")

df = df[['Text', 'Biased']]

print(df)
print()

cleaned_df = dc.clean_symbols(df,'Text')
cleaned_df = dc.convert_to_lowercase(df, 'Text')

print(cleaned_df)
print()

bias_count = da.biases_count(cleaned_df,'Biased')
print(bias_count)
print()

average_words = da.find_average_text_length(cleaned_df, 'Text')
print(average_words)
print()

largest_tweet = da.find_largest_by_char(cleaned_df, 'Text')
print(largest_tweet)
print()