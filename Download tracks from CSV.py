import csv, string
from pytube import YouTube, Search

# Load tracks from CSV
tracks = []
allowed = string.ascii_letters + string.digits + ' '

with open('track_info.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) # Skip header row
    for row in reader:
        if len(row) == 2:
            name = ''.join(char for char in row[0] if char in allowed)
            artist = row[1]
            tracks.append({'name': name, 'artist': artist})

# Download audio for each track
download_path = 'Downloads'

for track in tracks:
    search_query = f"{track['artist']} - {track['name']}"
    print(f"Downloading {search_query}")
    
    yt = Search(search_query).results[0]
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(download_path, filename=f"{track['artist']} - {track['name']}.mp3")
    print(out_file)

print('All file downloaded!')