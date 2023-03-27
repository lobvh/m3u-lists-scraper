<h1 align="center">
 M3U LISTS SCRAPER
</h1> 

One day I sat in front of my TV trying to input different *free* IPTV ```m3u``` lists found on the Internet. Each of them contains different number of channels, and some of them span >20k channels. Since lightweight IPTV players (I have poor TV!) don't offer functionalities like "search channels" ([Tivimate](https://www.tivimate.org/en) doesn't!), and as some of the lists doesn't contain stuff I was looking for or they are lagging/having bad links you can imagine how much time I would spend scanning each list and testing if they have what I need.

Out of all 10k+ channels + VOD stuff that IPTV resellers offer all I want is an access to some ```EX-YU``` (only ```HRT 3```, because they have **the perfect** choice of those non-Americana movies), ```Swedish``` (language learning) and ```French``` (language learning) channels. 

Of course, when my wife found out what I'm trying to accomplish I had to expand the list with new regex sh\*t...

I was like... there has to be a better way than manually trying lists one-by-one. I know that all this jazz could be easily solved by paying a cheap IPTV reseller with stable servers etc. but nevertheless I wanted to translate my remote controler patterns into scripts. 

The naive idea is to scrape all the ```m3u``` links and download ```.m3u``` files, delete the ones that are empty, filter each ```.m3u``` file for the channels I'm looking for via naive ```regex``` and collect everything into one *big* ```m3u``` file. I've named the file ```k.m3u``` because I wanted as little  manual entering via remote controller as possible. Then, I would create a simple ```HTTP``` server via ```python -m http.server``` and download the playlist on [Tivimate](https://www.tivimate.org/en) from my localhost.

Yes, some of the stuff could be polished depending on the needs but to find stable channels I would basically collect them in one place and manually check which ones works on my TV. That already reduces enormous time and bypasses the non-premium *search channel* + *multiple playlists* features on [Tivimate](https://www.tivimate.org/en). 

There are two main scripts that should be run in succesion:
- ```scrape-m3u.py``` which finds all the ```m3u``` links on the given URL (you can find it easilly via Google) and downloads ```m3u``` files in those links, 
- ```fav-channels.sh``` which searches all the channels I'm looking for in the downloaded ```m3u``` files, extracts them into ```k.m3u``` file and also does some post-processing (data cleaning). 

**Requirements:**
```ripgrep```, [fd](https://github.com/sharkdp/fd), ```perl``` and ```Python```.

**NOTE:** I'm not responsible for any illegal operations, nor do I promote them. **Do it at your own risk.**
Also, I don't promote [Tivimate](https://www.tivimate.org/en). I use it because I have poor TV and I'm not expecting much from the IPTV player. Choose your poison depending on the needs.
