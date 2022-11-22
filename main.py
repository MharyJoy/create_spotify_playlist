import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
                            client_id=os.getenv("APP_CLIENT_ID"),
                            client_secret=os.getenv("APP_CLIENT_SECRET"),
                            redirect_uri=os.getenv("APP_URI"),
                            scope=os.getenv("APP_SCOPE"),
                            show_dialog=True,
                            cache_path="token.txt"))

user_id = sp.current_user()["id"]

#TODO 1 - Using BeautifulSoup to scape the top 100 songs from a particular date of your choice
# URL = "https://www.billboard.com/charts/hot-100/2022-05-17/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
print(URL)

response = requests.get(URL)
website_html = response.text

song_names = []

soup = BeautifulSoup(website_html, "html.parser")
top_song = song_names.append(soup.find(name="h3").getText().strip())
all_song = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(all_song)

movie_titles = [song_names.append(song.getText().strip()) for song in all_song]
print(song_names)


# top_artist = []
# all_artist = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
# # print(all_artist)
#
# artist_name = [top_artist.append(artist.getText().strip()) for artist in all_artist]
# print(top_artist)


#TODO 2 - Then we're going to extract all of the song titles from the list
#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#TODO 3 - And then we're going to use the Spotify API to create a playlist for that particular date.
#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billoard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)