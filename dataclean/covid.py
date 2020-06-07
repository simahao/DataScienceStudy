
class Covid(Csv):
    def __init__(self, path):
        super(Covid, self).__init__(path)
    def deal_china_cronavirus(self):
        return self.read_csv(self.path)


if __name__ == "__main__":
    covid = Covid('../data/covid.csv')
    df = covid.deal_china_cronavirus()
    print(df)
