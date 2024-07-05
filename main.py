import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import subprocess
import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox, scrolledtext, Label
import re
import os
import requests
from io import BytesIO
from PIL import Image, ImageTk
from googleapiclient.discovery import build

# Spotify API credentials
client_id = 'c83b7fd3c3704e30b1fb5c69e23a4b82'
client_secret = 'd1479f72d1614e5488675aafa56322ad'

# YouTube API credentials
youtube_api_key = 'AIzaSyAPo075c0Q7BMZn1VTON_mlKVI4KOE52lo'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

# Global variables to control cancellation, pause and track downloads
cancel_download = False
pause_download = False
download_log = []

def extract_id(url):
    match = re.search(r'(album|track|playlist)/([a-zA-Z0-9]+)', url)
    if match:
        return match.group(2), match.group(1)
    return None, None

def get_genres(artist_ids):
    genres = set()
    for artist_id in artist_ids:
        artist = sp.artist(artist_id)
        genres.update(artist['genres'])
    return ", ".join(genres) if genres else "Unknown Genre"

def youtube_search_link(search_song_title):
    try:
        request = youtube.search().list(
            q=search_song_title,
            part='snippet',
            type='video',
            maxResults=1
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        return f'https://www.youtube.com/watch?v={video_id}'
    except Exception as e:
        update_log(f"Error during YouTube search: {str(e)}")
        return None

def download_by_link(search_song_title, id_song, download_dir, retries=3):
    try:
        for attempt in range(retries):
            if cancel_download:
                update_log("Download cancelled by user.")
                return -1

            while pause_download:
                update_log("Download paused by user.")
                threading.Event().wait(1)

            youtube_link = youtube_search_link(search_song_title)
            if not youtube_link:
                update_log(f"No YouTube link found for: {search_song_title}")
                continue

            command = f'ytmdl --url "{youtube_link}" --quiet -o "{download_dir}" --spotify-id "{id_song}"'
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    update_log(output.strip())
                if cancel_download:
                    process.terminate()
                    update_log("Download cancelled by user.")
                    return -1
                while pause_download:
                    update_log("Download paused by user.")
                    threading.Event().wait(1)
            rc = process.poll()
            if rc == 0:
                update_log(f"Download completed for: {search_song_title}")
                download_log.append((search_song_title, command))
                return 0
            else:
                update_log(f"Error downloading {search_song_title}: Return code {rc}. Retrying ({attempt + 1}/{retries})")
        return rc
    except Exception as e:
        update_log(f"Exception during download: {str(e)}")
        return -1

def download_playlist(playlist_url, download_dir, suffix):
    try:
        global cancel_download
        global pause_download
        cancel_download = False
        pause_download = False

        playlist_id, _ = extract_id(playlist_url)
        if not playlist_id:
            raise ValueError("Invalid playlist URL")

        playlist = sp.playlist(playlist_id)
        tracks = playlist['tracks']
        total_tracks = tracks['total']
        downloaded_tracks = 0
        update_album_cover(playlist['images'][0]['url'])

        while tracks:
            for track in tracks['items']:
                if cancel_download:
                    messagebox.showinfo("Cancelled", "Download cancelled!")
                    generate_report(download_dir)
                    return

                id_song = track['track']['id']
                song_name = track['track']['name']
                artists = [artist['name'] for artist in track['track']['artists']]
                search_song_title = f"{song_name} - {', '.join(artists)}"
                if suffix:
                    search_song_title += f" - {suffix}"

                download_result = download_by_link(search_song_title, id_song, download_dir)
                if download_result == 0:
                    downloaded_tracks += 1
                update_progress(downloaded_tracks, total_tracks)

            if tracks['next']:
                tracks = sp.next(tracks)
            else:
                break

        messagebox.showinfo("Success", "Download completed!")
        generate_report(download_dir)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_album(album_url, download_dir, suffix):
    try:
        global cancel_download
        global pause_download
        cancel_download = False
        pause_download = False

        album_id, _ = extract_id(album_url)
        if not album_id:
            raise ValueError("Invalid album URL")

        album = sp.album(album_id)
        tracks = album['tracks']['items']
        total_tracks = len(tracks)
        downloaded_tracks = 0
        update_album_cover(album['images'][0]['url'])

        for track in tracks:
            if cancel_download:
                messagebox.showinfo("Cancelled", "Download cancelled!")
                generate_report(download_dir)
                return

            id_song = track['id']
            song_name = track['name']
            artists = [artist['name'] for artist in track['artists']]
            search_song_title = f"{song_name} - {', '.join(artists)}"
            if suffix:
                search_song_title += f" - {suffix}"

            download_result = download_by_link(search_song_title, id_song, download_dir)
            if download_result == 0:
                downloaded_tracks += 1
            update_progress(downloaded_tracks, total_tracks)

        messagebox.showinfo("Success", "Download completed!")
        generate_report(download_dir)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_track(track_url, download_dir, suffix):
    try:
        global cancel_download
        global pause_download
        cancel_download = False
        pause_download = False

        track_id, _ = extract_id(track_url)
        if not track_id:
            raise ValueError("Invalid track URL")

        track = sp.track(track_id)
        id_song = track['id']
        song_name = track['name']
        artists = [artist['name'] for artist in track['artists']]
        search_song_title = f"{song_name} - {', '.join(artists)}"
        if suffix:
            search_song_title += f" - {suffix}"
        update_album_cover(track['album']['images'][0]['url'])

        download_result = download_by_link(search_song_title, id_song, download_dir)
        if download_result == 0:
            update_progress(1, 1)

        messagebox.showinfo("Success", "Download completed!")
        generate_report(download_dir)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_download():
    global download_log
    global pause_download_button
    download_log = []
    url = url_entry.get()
    suffix = suffix_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return

    download_dir = filedialog.askdirectory()
    if not download_dir:
        messagebox.showwarning("Input Error", "Please select a download directory")
        return

    # Show progress bar and log after download starts
    progress_bar.pack(pady=10, fill=ttk.X)
    progress_text.pack(pady=10)
    cancel_button.pack(pady=5)
    pause_download_button.pack(pady=5)

    # Identify the type of URL and call the corresponding function
    _, url_type = extract_id(url)
    if url_type == "playlist":
        download_thread = threading.Thread(target=download_playlist, args=(url, download_dir, suffix))
    elif url_type == "album":
        download_thread = threading.Thread(target=download_album, args=(url, download_dir, suffix))
    elif url_type == "track":
        download_thread = threading.Thread(target=download_track, args=(url, download_dir, suffix))
    else:
        messagebox.showwarning("Input Error", "Invalid URL")
        return

    download_thread.start()

def update_log(message):
    progress_text.config(state=ttk.NORMAL)
    progress_text.insert(ttk.END, message + "\n")
    progress_text.yview(ttk.END)
    progress_text.config(state=ttk.DISABLED)

def update_progress(current, total):
    progress_var.set((current / total) * 100)

def update_album_cover(url):
    global album_cover_label
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img.thumbnail((150, 150))
    img = ImageTk.PhotoImage(img)
    album_cover_label.config(image=img)
    album_cover_label.image = img
    album_cover_label.pack(pady=10)

def pause_download_action():
    global pause_download
    if pause_download:
        pause_download = False
        pause_download_button.config(text="Pause Download")
        update_log("Download resumed by user.")
    else:
        pause_download = True
        pause_download_button.config(text="Resume Download")
        update_log("Download paused by user.")

def cancel_download_action():
    global cancel_download
    cancel_download = True
    update_log("Cancelling download... Please wait.")

def generate_report(download_dir):
    report_file = os.path.join(download_dir, "download_report.txt")
    with open(report_file, "w") as f:
        f.write("Download Report\n")
        f.write("================\n")
        f.write(f"Total songs downloaded: {len(download_log)}\n\n")
        for entry in download_log:
            song_title, command = entry
            f.write(f"Song: {song_title}\n")
            f.write(f"Command: {command}\n\n")
    update_log(f"Download report generated: {report_file}")

# Create the main window
root = ttk.Window(themename="darkly")
root.title("Spotify Downloader")

# URL entry
ttk.Label(root, text="Spotify URL:").pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# Suffix entry
ttk.Label(root, text="Optional Suffix:").pack(pady=5)
suffix_entry = ttk.Entry(root, width=50)
suffix_entry.pack(pady=5)

# Download button
download_button = ttk.Button(root, text="Download", command=start_download, bootstyle=SUCCESS)
download_button.pack(pady=20)

# Progress bar (initially hidden)
progress_var = ttk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, bootstyle=INFO)

# Progress log (initially hidden)
progress_text = scrolledtext.ScrolledText(root, state=ttk.DISABLED, width=60, height=20)
progress_text.pack_configure(pady=10)  # Adjust the padding for visibility

# Cancel button (initially hidden)
cancel_button = ttk.Button(root, text="Cancel Download", command=cancel_download_action, bootstyle=DANGER)

# Pause button (initially hidden)
pause_download_button = ttk.Button(root, text="Pause Download", command=pause_download_action, bootstyle=WARNING)

# Album cover (initially hidden)
album_cover_label = Label(root)

# Run the application
root.mainloop()
