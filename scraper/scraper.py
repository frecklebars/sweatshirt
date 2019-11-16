import lyricsgenius as genius
import json

genius_client_access_token = open("token/_client_access_token.txt", 'r').read()

api = genius.Genius(genius_client_access_token)

lyricsf = open("lyrics.txt", "w", encoding="utf-8")

file = open("songs.json", "r", encoding="utf-8")
songs = json.load(file)
file.close()

#tldr takes each artist in the json and then each song in their specific category and gets the lyrics
for artist in songs["artists"]:
    for song in songs[artist]:
        song = api.search_song(song, artist)
        lyricsf.write(song.lyrics)
        lyricsf.write("\n\n")
lyricsf.close()
