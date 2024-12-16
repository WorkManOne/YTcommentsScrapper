# YTcommentsScrapper
* Scrap YouTube comments and responses containing certain words.
* Build tree structure of comments and responses
* Fast and super simple solution written with the help of ChatGPT. 

# Installing
Using https://github.com/egbertbouman/youtube-comment-downloader
```
pip install youtube-comment-downloader
```
# Usage:
### 1. Customize needed keywords in code. 
Word "mus" is already in code as example.
### 2. Put url of videos you want to scrap comments from.
Just put it in urls.txt file. You can put multiple urls in file, each from a new line.
### 3. Launch scripth with
```
python main.py
```
or whatever way you use to launch python scripts
### 4. Wait until script finishes its work 
When it finish scrapping one video, all comments, 
that contain word you specified will 
be in filtered_comments_VIDEOID.txt file
### 5. Done!
