# 'break' terminates a loop
# 'continue' skips one iteration of a loop

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic" ]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + ' '
    if len(news_ticker) > 140:
        news_ticker = news_ticker[:140]
        break

print(len(news_ticker))
print(news_ticker)
