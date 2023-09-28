import csv
import os
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk

# GUI to input link

root = tk.Tk()
root.title("Spotify Playlist Downloader")
root.geometry("550x150") 
root.configure(bg='#426e86')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title_label = tk.Label(root, text="Spotify Playlist Downloader", font=("Helvetica", 18,"bold"), bg='#426e86', fg='#fff')
title_label.grid(row=0, columnspan=2, pady=10)

link_label = tk.Label(root, text="Enter Playlist link", font=("Helvetica", 12,"bold"), bg='#426e86', fg='#fff') 
link_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

link_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
link_entry.grid(row=1, column=1, sticky="e", padx=10, pady=10) 

submit_btn = tk.Button(root, text="Submit", font=("Helvetica", 12), command=root.quit)
submit_btn.grid(row=2, column=1, sticky="e", padx=10, pady=10)

root.mainloop()

PLAYLIST_LINK = link_entry.get()
print(PLAYLIST_LINK)


CLIENT_ID = '4c7a8ce7e4624bc9bbb9ad131cc20727'
CLIENT_SECRET = '3313da573b164934bee40fa0678232f5'
OUTPUT_FILE_NAME = "track_info.csv"

# authenticate
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# create spotify session object
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# get uri from https link
if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", PLAYLIST_LINK):
    playlist_uri = match.groups()[0]
else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")

# get list of tracks in a given playlist (note: max playlist length 100)
tracks = session.playlist_tracks(playlist_uri)["items"]

# create csv file
with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # write header column names
    writer.writerow(["track", "artist"])

    # extract name and artist
    for track in tracks:
        name = track["track"]["name"]
        artists = ", ".join(
            [artist["name"] for artist in track["track"]["artists"]]
        )

        # write to csv
        writer.writerow([name, artists])

