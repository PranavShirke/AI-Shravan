import tkinter as tk
from tkinter import Entry, Button, Label, messagebox
import yt_dlp
import webview  # For embedding video playback

# GUI Window
root = tk.Tk()
root.title("Sign Language Media Finder")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

def get_best_youtube_video(query):
    """Find the best matching YouTube video URL for the given query using yt-dlp."""
    ydl_opts = {
        "quiet": True,
        "format": "best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch1:{query}", download=False)  # Use ytsearch1:
            if "entries" in result and len(result["entries"]) > 0:
                return result["entries"][0]["webpage_url"]  # Return actual video link
        except Exception as e:
            print(f"Error: {e}")

    return None

def play_video():
    """Find and play the best matching YouTube video inside Tkinter."""
    word = entry.get().strip().lower()
    img_label.config(text="Searching...", fg="black")

    video_url = get_best_youtube_video(f"{word} ASL sign")

    if video_url:
        img_label.config(text="Playing sign language video...", fg="green")
        webview.create_window("Sign Language Video", video_url)  # Open in GUI
        webview.start()
    else:
        img_label.config(text="No video found.", fg="red")

def download_video():
    """Download the selected YouTube video using yt-dlp."""
    word = entry.get().strip().lower()
    video_url = get_best_youtube_video(f"{word} ASL sign")

    if video_url:
        ydl_opts = {
            "outtmpl": "%(title)s.%(ext)s",
            "format": "best",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        messagebox.showinfo("Download Complete", "The video has been downloaded.")
    else:
        messagebox.showerror("Error", "No video found to download.")

# GUI Elements
entry = Entry(root, font=("Arial", 16), width=20)
entry.pack(pady=20)

search_btn = Button(root, text="Search Sign", font=("Arial", 14), command=play_video)
search_btn.pack()

download_btn = Button(root, text="Download Video", font=("Arial", 14), command=download_video)
download_btn.pack(pady=5)

img_label = Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
img_label.pack(pady=10)

root.mainloop()
