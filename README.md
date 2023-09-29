# Download songs from Spotify Playlists
<p align="center">
  <img width="100" src="https://cdn-icons-png.flaticon.com/512/8560/8560446.png">
</p>
<p align="center">Enjoy your song from anywhere.</p>


## 🎧 Description
 - Enter the link to your favorite Spotify playlist to extract the songs, which can then be downloaded as YouTube MP3 files and extracted as a CSV file.
 - CSV file can be used for song analysis.
 - Downloaded tracks can be accessed offline.

## 🔍 How to Use
### Before Using the Application

Navigate to the [Spotify developer portal](https://developer.spotify.com/dashboard) and log in. Register a new app in the developer console to generate your API keys.

<p align="center"> 
<img src = 'https://github.com/hmyle/Download-songs-from-Spotify-Playlists/assets/116583355/959c93dd-bbb4-445e-92e8-f6da0e081c55'>
</p>

In order to authenticate your Python application with the Spotify API you need to get your authentication keys -- `client_id` and `client_secret`.

<p align="center"> 
<img src = 'https://github.com/hmyle/Download-songs-from-Spotify-Playlists/assets/116583355/70db74c6-e3c0-4ac0-b6de-af56db4ab0d6'>
</p>

Adjust the .env file with your `client_id` and `client_secret`.

```
# .env example
SPOTIPY_CLIENT_ID = 'Replace with your client ID'
SPOTIPY_CLIENT_SECRET = 'Replace with your client secret'
```


### How to Use the application
<p align="center"> 
<img src= 'https://github.com/hmyle/Download-songs-from-Spotify-Playlists/assets/116583355/6f33cdef-3cbd-46a5-99a6-ff2cd0d6f0c9'>
</p>

Find your playlist and select "Copy link to playlist". Run "Extract track to CSV.py" then paste the link into the box, then click submit.

<p align="center"> 
<img src = 'https://github.com/hmyle/Download-songs-from-Spotify-Playlists/assets/116583355/87657423-89be-479f-a723-f3b5cae988c7'>
</p>

A new CSV file will be created and filled with your favorite songs from your favorite playlist! Then, if you want to download all MP3 files of the songs. Run the file name "Download tracks from CSV.py".

<p align="center"> 
<img src = 'https://github.com/hmyle/Download-songs-from-Spotify-Playlists/assets/116583355/cf3e1db5-9e3b-4362-9b1c-1e3e931c2672'>
</p>

All the tracks will be downloaded to the "Downloads" folder.

## 🔧 Build Information
 - Python3
 - External Libraries: pytube, spotipy, dotenv, tkinter 

## 🏆 Author
- Le Ha My  - hmyle.it@gmail.com


