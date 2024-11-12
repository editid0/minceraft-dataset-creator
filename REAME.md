# Minecraft dataset creator
## FAQ
### What is this for?
This tool listens for keypresses and mouse movements and logs the exact time of each.

### How do I start it?
1. First start an OBS recording of minecraft.
2. Start the `main.py` script to listen for keypresses.
3. Open minecraft and play as normal.
4. Record for between 9:30 and 10 minutes (No more than 10m).
5. Press Ctrl+z to stop listening for keypresses.
6. Stop the OBS recording.
7. Move the video file into the `gamerec` folder.
8. Rename the log.txt file to the same name as the video but replace mkv/mp4/mov with txt.
9. Put the txt file into the keyrec folder.
10. Run `timeextract.py` and input `gamerec\{video file name}`
11. Copy the exact timestamp
12. In meta.json create a new session, fill in the info, and paste the timestamp into the video_time value.
13. Fill in the exact minecraft version you were playing on.

### Can I use the gameplay videos for anything?
Yes, please link to this repo if possible though.

### Can I contribute my own gameplay?
Yes, follow the gameplay rules below and use git to make a commit and make a pull request to add your gameplay.

## Gameplay rules
1. No overlays (game must look as vanilla as possible)
2. No texture packs.
3. No videos over 10 minutes
4. No videos under 9 minutes 30 seconds.
5. Videos can't start where another ended.