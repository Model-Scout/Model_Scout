# TWICE Korean singles lyrics

Lyric lines and timings of the Korean singles by kpop girl group TWICE

### What is the data?

This dataset contains all TWICE Korean single lyrics from 2015-2022. The included songs are Like Ooh Ahh (2015),Cheer Up (2016),TT (2016),Heart Shaker (2017),Knock Knock (2017),Likey (2017),Dance The Night Away (2018),What Is Love (2018),Yes or Yes (2018),Fancy (2019),Feel Special (2019),More&More (2020),I Can't Stop Me (2020),Cry For Me (2020), Alcohol Free (2021), Scientist (2021) and Talk that Talk (2022)


### How was the data obtained?

Since TWICE is pretty popular, I expected to find a table somewhere in the web that contains this kind of data but unfortunately, I havent found any so I decided to make my own.This would normally be a transcription exercise that would take up a lot of time and energy, but I think I found a way to lazily do it with help of some programming.

1. First, I obtained timing data from subtitles (.srt) of TWICE music videos in Youtube. This is simple–we just need to extract the .srt subtitle file from the video (there are lots of online applets for this!) and read the file in python to get the start and end timestamps of each subtitle line.

2. Next, I got the song lyrics by scraping blog entries from colorcodedlyrics.com. Because the lines are already color-tagged, we could map a member with her part a quite easily.

Whenever a line assignment is seemingly erroneous in the color coded lyrics website, I go back to the music video and/or performance videos to be able to correct it if necessary. (I also admit that in the 3 years I’ve been listening to the group, I’ve already developed an ear to detect each of their voices)

### Acknowledgements
I thank the TWICE official channel for providing the subtitles for the music videos, and also the Youtubers jaedungi, krystallized and lemoring for helping me check the line timings using their line distribution videos

출처: Kaggle (jcacperalta/twice-korean-singles-lines)
태그: popular culture, music, korea
라이선스: Other (specified in description)
수정일: 2022-09-05T03:36:49.077Z
