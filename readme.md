# Discord Bot with Python
***

### Libraries used:

* discord python api  `pip install discord.py`
* youtube download api  `pip install youtube_dl`
* chat exporter `pip install chat-exporter` 
* twitter api `pip install tweepy`

### Functionalities explored:

|Discord|Twitter|
|-------|-------|
|Setting activity and status|Posting status|
|Replies and Mentions|Posting text messages|
|Sending GIFs|Posting media files|
|Playing audio in voice channels| - |

### Instructions:

1. FFMPEG:
    * This software is needed for playing mp3 audio through discord api.
    * This can be skipped if youtube audio streaming is not needed.
    * You can download this here [FFMpeg](https://www.ffmpeg.org/download.html).
    * Alternatively you can find it on this repository as a folder.
    * Make sure to provide the correct path in-code for the application, which is inside the bin folder.
2. Wkhtmltopdf:
    * This software is used to convert an html page to other formats.
    * We will be using the html to jpg function.
    * You can download this here [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html).
    * Alternatively you can find it on this repository as a folder.
    * Make sure to provide the correct path in-code for the application, which is inside the bin folder.
3. Discord bot:
    * Using discord developer portal, create a bot.
    * Add it to a server using the proper credentials as shown on the portal.
    * Note down the application token and include it in the code where it is asked for.
4. Twitter bot:
    * Using twitter developer portal, create a bot.
    * Obtain the credentials and insert them in the code properly.
    * The code from "twit.py" in this repository should be copy pasted into the "discord.py" file for twitter functions.