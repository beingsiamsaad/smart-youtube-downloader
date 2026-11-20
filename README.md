# Smart YouTube Downloader

A simple Python-based YouTube downloader for Ubuntu WSL and Linux.

## Features

- Download individual YouTube videos
- Download complete playlists
- Select specific videos from playlists
- Download MP4 videos
- Extract MP3 audio
- Best available quality
- Save downloaded files locally

## Requirements

- Python 3
- yt-dlp
- FFmpeg

## Installation

### 1. Update Ubuntu

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install dependencies

```bash
sudo apt install python3 python3-pip python3-venv ffmpeg git -y
```

### 3. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd smart-youtube-downloader
```

### 4. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install Python packages

```bash
pip install -r requirements.txt
```

## Run the downloader

```bash
python3 yt_tool.py
```

Follow the instructions displayed in the terminal.

## Platform

- Ubuntu
- Ubuntu WSL
- Linux

## License

MIT License
