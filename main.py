import requests
from bs4 import BeautifulSoup


#TODO 1 - Using BeautifulSoup to scape the top 100 songs from a particular date of your choice
# URL = "https://www.billboard.com/charts/hot-100/2022-05-17/"

travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"
print(URL)

response = requests.get(URL)
website_html = response.text

top_songs = []

soup = BeautifulSoup(website_html, "html.parser")
top_song = top_songs.append(soup.find(name="h3").getText().strip())
all_song = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(all_song)

movie_titles = [top_songs.append(song.getText().strip()) for song in all_song]
print(top_songs)


top_artist = []
all_artist = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")
# print(all_artist)

artist_name = [top_artist.append(artist.getText().strip()) for artist in all_artist]
print(top_artist)


#TODO 2 - Then we're going to extract all of the song titles from the list

#TODO 3 - And then we're going to use the Spotify API to create a playlist for that particular date.

