import re
import os
import cgi
import spotipy
import spotipy.util as util
from HTMLParser import HTMLParser

pl_id = 'YOUR_PLAYLIST_ID'
u_id = 'YOUR_SPOTIFY_USER_ID'
token = 'YOUR_TOKEN'
f = open('/PATH/TO/HTML/FILE.txt','r')
data = f.read()
a = '<span class="track-title">'
b = '</span>'
c = '<span class="track-artist">'
d = '</span>'
h = HTMLParser()
ab = re.findall ( a + '(.*?)' + b, data, re.DOTALL)
cd = re.findall ( c + '(.*?)' + d, data, re.DOTALL)
sp = spotipy.Spotify(auth=token)
for abi, cdi in zip(ab, cd):
    if abi == "Song Title":
        continue
    tr = cgi.escape(h.unescape(abi) + " " + h.unescape(cdi))
    print(h.unescape(abi) + " " + h.unescape(cdi))
    results = sp.search(q=tr, limit=1)
    for i, t in enumerate(results['tracks']['items']):
        print ' ', i, t['uri']
        sp.user_playlist_add_tracks(u_id, pl_id, [t['uri']])
