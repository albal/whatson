import requests
from bs4 import BeautifulSoup as bs
import lxml
import xml.etree.ElementTree as ET

feed = "http://www.xmltv.co.uk/feed/9437"
#feed = "http://www.xmltv.co.uk/feed/1897"
channel_name = "ITV"
program_name = "Who wants to be"


resp = requests.get(feed)
content = resp.content
bs_content = bs(content, "lxml")

channels = bs_content.find_all("channel")
for channel in channels:
    for name in channel.find_all("display-name"):
        if name.get_text() == channel_name:
            cont = str(channel)
            channel_id = cont.split('"')[1]

programs = bs_content.find_all("programme", {"channel":channel_id})
for program in programs:
    for title in program.find_all("title"):
        if program_name in title.get_text():
            print(program)

