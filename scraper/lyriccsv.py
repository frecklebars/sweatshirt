import pandas as pd

lyrics = pd.read_csv("lyrics.csv", encoding="utf-8")
lyrics = lyrics[["lyrics"]]
lyrics = lyrics.dropna()

file = open("lyrics2.txt", "w", encoding="utf-8")


for i in range(len(lyrics)):
    song = lyrics.iloc[i]["lyrics"]
    file.write(song)