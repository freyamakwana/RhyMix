# RhyMix

RhyMix is a simple music player application built using Python's Tkinter library for the GUI and Pygame for playing audio. It provides basic functionalities like play/pause, skipping songs, and adjusting volume, along with displaying album covers and song names.

## Features

- **Play/Pause:** Control playback of songs.
- **Skip Songs:** Navigate to the next or previous song in the playlist.
- **Volume Control:** Adjust the volume using a slider.
- **Album Cover Display:** View album covers while playing songs.

## Usage

- Open the application and navigate through your music library.
- Click the "Play" button to start playing the current song.
- Use the ">" button to skip to the next song and the "<" button to go back to the previous song.
- Adjust the volume using the slider.
- Enjoy listening to your favorite tunes with RhyMix!

## Adding Songs and Album Covers

To add additional songs and album covers:
1. Place your song files (in .wav format) in the `songs` directory.
2. Add the file paths of your songs to the `list_of_songs` list in the `main.py` file.
3. Place your cover images (in .jpg or .png format) in the `img` directory.
4. Add the file paths of your album covers to the `list_of_covers` list in the `main.py` file.

## Dependencies

- Python 3.x
- Tkinter
- Pygame
- Pillow (PIL)
