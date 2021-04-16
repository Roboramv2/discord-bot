# Discord Bot with Python
***

### Libraries used:

* discord python api  `pip install discord.py`
* youtube download api  `pip install youtube_dl`

### Discord functionalities explored:

1. Setting activity and status
2. Replies
3. Mentions
4. Sending GIFs
5. Finding out in which voice channel someone is in
6. Playing audio in voice channels using ytdl and ffmpeg

### Instructions:

1. FFMPEG:
    * This software is needed for playing mp3 audio through discord api.
    * This can be skipped if youtube audio streaming is not needed.
    * You can download this here [FFMpeg](https://www.ffmpeg.org/download.html).
    * Alternatively you can find it on this repository as a folder.
    * Make sure to provide the correct path in-code for the application, which is inside the bin folder.
2. Discord bot:
    * Using discord developer portal, create a bot.
    * Add it to a server using the proper credentials as shown on the portal.
    * Note down the application token and include it in the code where it is asked for.