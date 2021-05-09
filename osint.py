# OSINT - 2021
# HeadlessMan
# Hijau = Information
# Kuning = Result
import time, os, requests, sys
from colorama import Fore,Style
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import numpy as np
import concurrent.futures
logo = f"""
 OPEN SOURCE INTELLIGENCE
        Good Luck
"""

errorsys = f"""
{Fore.YELLOW}(!) How to using tools open source intelligence (!){Style.RESET_ALL}
    1) python3 / python osint.py name phone
    2) python3 osint.py ravensyah 62895391829277
    3) used "+" for add space | python3 osint.py headless+man | headless man
    4) tested on: linux mint(ubuntu)
{Fore.YELLOW}[!] Features in this osint tools [!]{Style.RESET_ALL}
    1) search for social media by username or name
    2) search the web or articles that are related to a username or name
    3) looking for information through a mobile number
    4) get posts instagram ( photo, video, dll )

Donate BTC: {Fore.YELLOW}371nZWBU7X6asMa3Ya15WkY2BKX4qQ2j7M{Style.RESET_ALL}
"""
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

os.system("clear")
print(logo)

if(len(sys.argv) != 3):
   print(errorsys)
   sys.exit(1)

username = sys.argv[1].replace("+", " ")
phone = sys.argv[2]

def page_info(user):
    try:
       pages = np.arange(1,3)
       for url in pages:
           url = "https://www.bing.com//search?q="+user+"&first="+str(url)
           session = HTMLSession()
           response = session.get(url)
           res = response.html.find("cite")
           for angka in range(0, len(res)):
               domain = res[angka].text
               if (f"{username}" in requests.get(domain).text):
                   print(f"{Fore.YELLOW}[+] Result found: {domain}{Style.RESET_ALL}")
               else:
                   pass
    except:
        print(f"[{Fore.RED}X{Style.RESET_ALL}] Result not found.")

def instagram_info(userig):
    try:
       url = "https://www.instagram.com/{userig}/"
       global req
       req = requests.get(url, headers=headers)
       soup = BeautifulSoup(req,text, 'lxml')
       tag = soup.find("meta", attrs={"name":"description"})
       teks = tag.attrs["content"]
       status = teks.split("-")[0]
       if req.text == 200:
          print(f"{Fore.YELLOW}[+] Found account: {status}{Style.RESET_ALL}")
       else:
          print(f"[{Fore.RED}X{Style.RESET_ALL}] Not found account {userig}")
    except:
       pass

def info_number(nomor):
    try:
       v = requests.get(f"http://apilayer.net/api/validate?access_key=7c68ba213f11c8a26757b878c5fdf6d4&number={nomor}")
       headlessman = v.json()
       print(f"{Fore.YELLOW}[+] Status: {headlessman['valid']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Number: {headlessman['number']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Local format: {headlessman['local_format']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] International format: {headlessman['international_format']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Country Prefix: {headlessman['country_prefix']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Country Code: {headlessman['country_code']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Country Name: {headlessman['country_name']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Location: {headlessman['location']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Carrier: {headlessman['carrier']}{Style.RESET_ALL}")
       print(f"{Fore.YELLOW}[+] Line type: {headlessman['line_type']}{Style.RESET_ALL}{Style.RESET_ALL}")
    except Exception as e:
       #print(f"[{Fore.RED}X{Style.RESET_ALL}] Api key error.")
       print(e)

instagram = f'https://www.instagram.com/{username}'
facebook  = f'https://www.facebook.com/{username}'
twitter = f'https://www.twitter.com/{username}'
youtube = f'https://www.youtube.com/{username}'
pinterest = f'https://id.pinterest.com/{username}'
telegram = f'https://t.me/{username}'
github = f'https://github.com/{username}'
blogger = f'https://{username}.blogspot.com/'
patreon = f'https://www.patreon.com/{username}'
scribd = f'https://www.scribd.com/{username}'
hackerone = f'https://hackerone.com/{username}'
wordpress = f'https://{username}.wordpress.com/'
slack = f'https://{username}.slack.com/'
tumblr = f'https://{username}.tumblr.com'
flickr = f'https://www.flickr.com/people/{username}'
steam = f'https://steamcommunity.com/id/{username}'
vimeo = f'https://vimeo.com/{username}'
soundcloud = f'https://soundcloud.com/{username}'
disqus = f'https://disqus.com/by/{username}'
medium = f'https://medium.com/@{username}'
deviantart = f'https://{username}.deviantart.com'
vk = f'https://vk.com/{username}'
aboutme = f'https://about.me/{username}'
imgur = f'https://imgur.com/user/{username}'
flipboard = f'https://flipboard.com/@{username}'
slideshare = f'https://slideshare.net/{username}'
fotolog = f'https://fotolog.com/{username}'
spotify = f'https://open.spotify.com/user/{username}'
mixcloud = f'https://www.mixcloud.com/{username}'
badoo = f'https://www.badoo.com/en/{username}'
bitbucket = f'https://bitbucket.org/{username}'
dailymotion = f'https://www.dailymotion.com/{username}'
etsy = f'https://www.etsy.com/shop/{username}'
cashme = f'https://cash.me/{username}'
behance = f'https://www.behance.net/{username}'
goodreads = f'https://www.goodreads.com/{username}'
instructables = f'https://www.instructables.com/member/{username}'
keybase = f'https://keybase.io/{username}'
kongregate = f'https://kongregate.com/accounts/{username}'
livejournal = f'https://{username}.livejournal.com'
angellist = f'https://angel.co/{username}'
last_fm = f'https://last.fm/user/{username}'
dribbble = f'https://dribbble.com/{username}'
codecademy = f'https://www.codecademy.com/{username}'
gravatar = f'https://en.gravatar.com/{username}'
pastebin = f'https://pastebin.com/u/{username}'
foursquare = f'https://foursquare.com/{username}'
roblox = f'https://www.roblox.com/user.aspx?username={username}'
gumroad = f'https://www.gumroad.com/{username}'
newsground = f'https://{username}.newgrounds.com'
wattpad = f'https://www.wattpad.com/user/{username}'
canva = f'https://www.canva.com/{username}'
creative_market = f'https://creativemarket.com/{username}'
trakt = f'https://www.trakt.tv/users/{username}'
five_hundred_px = f'https://500px.com/{username}'
buzzfeed = f'https://buzzfeed.com/{username}'
tripadvisor = f'https://tripadvisor.com/members/{username}'
hubpages = f'https://{username}.hubpages.com'
contently = f'https://{username}.contently.com'
houzz = f'https://houzz.com/user/{username}'
blipfm = f'https://blip.fm/{username}'
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
hackernews = f'https://news.ycombinator.com/user?id={username}'
codementor = f'https://www.codementor.io/{username}'
reverb_nation = f'https://www.reverbnation.com/{username}'
designspiration = f'https://www.designspiration.net/{username}'
bandcamp = f'https://www.bandcamp.com/{username}'
colourlovers = f'https://www.colourlovers.com/love/{username}'
ifttt = f'https://www.ifttt.com/p/{username}'
ebay = f'https://www.ebay.com/usr/{username}'
okcupid = f'https://www.okcupid.com/profile/{username}'
trip = f'https://www.trip.skyscanner.com/user/{username}'
ello = f'https://ello.co/{username}'
tracky = f'https://tracky.com/user/~{username}'
basecamp = f'https://{username}.basecamphq.com/login'
google_plus = f'https://plus.google.com/s/{username}/top'

WEBSITE = [instagram, facebook, twitter, youtube, pinterest, telegram, github, blogger, patreon,
scribd, hackerone, wordpress, slack, google_plus,
tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp, codementor]

count = 0
nomor = phone

print(f"{Fore.BLUE}[~] ---- Searching information number phone {nomor} ---- [~]{Style.RESET_ALL}")
time.sleep(2)
print(f"{Fore.GREEN}[-] Scanning {nomor}...")
time.sleep(2)
info_number(nomor)

print(f"{Fore.BLUE}[~] ---- Searching informations for {username} ---- [~]{Style.RESET_ALL}")
time.sleep(2)
print(f"{Fore.GREEN}[-] Searching social media...{Style.RESET_ALL}")
time.sleep(2)
print(f"{Fore.GREEN}[-] Total social media for scan ({len(WEBSITE)}){Style.RESET_ALL}")
for url in WEBSITE:
    try:
       try:
          req = requests.get(url, verify=True, headers=headers)
       except:
          urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
          req = requests.get(url, verify=False, headers=headers)
       if req.status_code == 200:
          print(f"{Fore.YELLOW}[+] Result found: {url}{Style.RESET_ALL}")
          count += 1
       else:
           pass
    except:
        pass

print(f"{Fore.GREEN}[-] Total social media with username {username} is {count}{Style.RESET_ALL}")
time.sleep(2)

print(f"{Fore.BLUE}[~] ---- Get Instagram Information {username} ---- [~]{Style.RESET_ALL}")
print(f"{Fore.BLUE}[-] Search username {username} instagram...{Style.RESET_ALL}")

userig = username
instagram_info(userig)

print(f"{Fore.GREEN}[-] Get Instagram Post...{Fore.YELLOW}")
urlig = requests.get("https://www.instagram.com/{username}/", headers=headers)
if urlig.status_code == 200:
   os.system(f'instaloader profile {username}')
   print(f"{Fore.GREEN}[-] Please check the folder named username {username} instagram..{Style.RESET_ALL}")
else:
   print(f"{Style.RESET_ALL}[{Fore.RED}X{Style.RESET_ALL}] Account instagram {username} not found.")

print(f"{Fore.BLUE}[~] ---- Search the web or articles that are related to a username or name ---- [~]{Style.RESET_ALL}")
time.sleep(2)
print(f"{Fore.GREEN}[-] Search & Scan web...{Style.RESET_ALL}")
user = username.split()
if user:
   try:
      with concurrent.futures.ThreadPoolExecutor(int(30)) as headlessman:
        headlessman.map(page_info, user)
   except ValueError as e:
      print(f"Found Error: {e}")
