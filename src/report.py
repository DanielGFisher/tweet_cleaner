class ReportBuilder:
    def __init__(self, df, bias_count, average_words, average_anti, average_non_anti, top_10,
                 largest_antisemetic_tweets, largest_non_antisemetic_tweets):
        self.df = df
        self.bias_count = bias_count
        self.average_words = average_words
        self.average_anti = average_anti
        self.average_non_anti = average_non_anti
        self.top_10 = top_10
        self.largest_antisemetic_tweets = largest_antisemetic_tweets
        self.largest_non_antisemetic_tweets = largest_non_antisemetic_tweets

    def build_report(self):
        report = {
            "total_tweets": {
                "total": len(self.df),
                "anti_semetic": int(self.bias_count.get(1, 0)),
                "non_anti_semetic": int(self.bias_count.get(0, 0))
            },
            "average_length": {
                "total": int(self.average_words),
                "anti_semetic": int(self.average_anti),
                "non_anti_semetic": int(self.average_non_anti)
            },
            "common_words": {
                "total": self.top_10
            },
            "longest_three_tweets": {
                "antisemetic": self.largest_antisemetic_tweets['Text'].tolist(),
                "non_antisemetic": self.largest_non_antisemetic_tweets['Text'].tolist()
            }
        }
        return report

