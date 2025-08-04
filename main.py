from src.file_reader import FileReader
from src.data_analyzer import DataFrameAnalyser

Reader = FileReader()
df = Reader.read_file(r"C:\Users\danie\Downloads\tweets_dataset - tweets_dataset.csv")

analyser = DataFrameAnalyser()
bias = analyser.biases_count(df,"Biased")

print(bias)
