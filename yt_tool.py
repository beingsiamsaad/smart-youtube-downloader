import os
import subprocess
import sys

def check_dependency(cmd):
    return subprocess.call(f"which {cmd}", shell=True,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL) == 0

def run_command(cmd):
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Check dependencies
    if not check_dependency("yt-dlp"):
        print("❌ yt-dlp not installed")
        return

    if not check_dependency("ffmpeg"):
        print("⚠️ ffmpeg not found (merging may fail)")

    os.makedirs("downloads", exist_ok=True)

    # URL input
    url = input("Enter YouTube video or playlist URL:\n> ").strip()
    if not url:
        print("❌ Empty URL")
        return

    # Detect playlist
    auto_playlist = "list=" in url

    print("\nInput type:")
    print("1. Single video")
    print("2. Playlist")
    print("3. Auto detect")
    choice = input("Choice: ")

    if choice == "1":
        is_playlist = False
    elif choice == "2":
        is_playlist = True
    else:
        is_playlist = auto_playlist

    selection = ""

    # Show playlist items
    if is_playlist:
        print("\n📃 Fetching playlist...\n")
        run_command([
            "yt-dlp",
            "--flat-playlist",
            "--print", "%(playlist_index)s. %(title)s",
            url
        ])

        selection = input(
            "\nEnter video numbers (e.g. 1,3,5 or 1-5, Enter for all):\n> "
        ).strip()

    # Download type
    print("\nDownload type:")
    print("1. Video (MP4)")
    print("2. Audio (MP3)")
    print("3. Best quality")
    dtype = input("Choice: ")

    # Cookies
    print("\nCookies:")
    print("0. None")
    print("1. Chrome")
    print("2. Edge")
    print("3. Firefox")
    cookie_choice = input("Choice: ")

    browser = None
    if cookie_choice == "1":
        browser = "chrome"
    elif cookie_choice == "2":
        browser = "edge"
    elif cookie_choice == "3":
        browser = "firefox"

    # Build command
    cmd = ["yt-dlp"]

    if browser:
        cmd += ["--cookies-from-browser", browser]

    if not is_playlist:
        cmd.append("--no-playlist")
    elif selection:
        cmd += ["--playlist-items", selection]

    cmd += ["-o", "downloads/%(title)s.%(ext)s"]

    # Format options (safe for WSL)
    if dtype == "1":
        cmd += ["-f", "bv*+ba/b", "--merge-output-format", "mp4"]
    elif dtype == "2":
        cmd += ["-x", "--audio-format", "mp3"]
    else:
        cmd += ["-f", "best"]

    cmd.append(url)

    print("\n🚀 Running:\n", " ".join(cmd), "\n")

    if run_command(cmd):
        print("\n✅ Download completed!")
    else:
        print("\n❌ Download failed")

if __name__ == "__main__":
    main()
