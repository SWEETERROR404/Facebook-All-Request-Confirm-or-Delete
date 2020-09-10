import http.cookiejar
import urllib.request
import getpass
import requests
import bs4

logo = """
╔════════════════════════════════════════════════════╗
║ ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓███████████ ║           
║ ████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬███████████ ║
║ ███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████ ║
║ ████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████ ║
║ ███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓███████████ ║
║ ████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬███████████ ║
║ ███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████ ║
║ ████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████ ║
║ ███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████ ║
║ █████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████ ║
║ █████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████████████ ║
║ █████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████████████ ║
║ ████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████████████ ║
║ ████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓████████████ ║
║ █████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓████████████ ║
║ █████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬█████████████ ║
║ ██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓█████████████ ║
║ ███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬██████████████ ║
║ ███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓██████████████ ║
║ ████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓███████████████ ║   
║ ██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓█████████████████ ║
║ ███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓██████████████████ ║
║ ██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬████████████████████ ║
║ ███████████████▓▓▓██▓▓╬╬╬╬╬╬▓█████████████████████ ║
║              Created By Mubeen Ahmad               ║
╚════════════════════════════════════════════════════╝


                                                                                     \n\033[1;32;47m"""
print(logo)
print("\033[1;36;40m Facebook All Requests Confirm or Delete")

print("\033[1;32;40m If Any Problem than contact me on facebook account ")
print("\033[1;31;40m ------> https://m.facebook.com/Python3.7.py <------ ")
print("\033[1;32;40m       \t Contact me on Github  ")
print("\033[1;31;40m ------> https://github.com/CodeWithMubeen <------ ")

email = input("Enter your facebook Email / Phone Number :- ")
password = getpass.getpass("Enter your Password :- ")

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
authentication_url = "https://m.facebook.com/login.php"
payload = {

    'email': email,
    'pass': password
}
data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
print("Please wait for Extracting all Requests")
#Go to Friends Requests
url = "https://mbasic.facebook.com/friends/center/requests/#friends_center_main"
data = requests.get(url, cookies=cj)
soup = bs4.BeautifulSoup(data.text, "html.parser")
#see_more links extract
see_more = ["https://mbasic.facebook.com/friends/center/requests/"]
for i in see_more:
    data = requests.get(i, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    for x in soup.findAll(id="u_0_0"):
        for link in x.findAll("a"):
            href = link.get("href")
            if href[16] == "r":
                see_more.append("https://mbasic.facebook.com"+str(href))
            else:
                break
friends_name = []
confirm = []
delete = []
# class bm for link 0
data = requests.get(see_more[0], cookies=cj)
soup = bs4.BeautifulSoup(data.text, "html.parser")
for i in soup.findAll('div', class_="bm"):
    no = 0
    for a in i.findAll('a'):
        if no == 0:
            # name
            friends_name.append(a.text.replace("‏‎", "").replace("‎‏", "").replace("‏", ""))
        elif no == 1:
            # confirm request
            confirm.append('https://mbasic.facebook.com'+str(a).replace('"', "\n").split("\n")[3].replace("amp;",""))
        elif no == 2:
            # Delete request
            delete.append('https://mbasic.facebook.com'+str(a).replace('"', "\n").split("\n")[3].replace("amp;",""))
        no += 1
# class bk for link 1 to end
for next_class in see_more:
    data = requests.get(next_class, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    for i in soup.findAll('div', class_="bk"):
        no = 0
        for a in i.findAll('a'):
            if no == 0:
                friends_name.append(a.text.replace("‏‎","").replace("‎‏","").replace("‏",""))
            elif no == 1:
                # confirm request
                confirm.append('https://mbasic.facebook.com'+str(a).replace('"', "\n").split("\n")[3].replace("amp;",""))
            elif no == 2:
                # Delete request
                delete.append('https://mbasic.facebook.com'+str(a).replace('"', "\n").split("\n")[3].replace("amp;",""))
            no += 1
print("Total Requests "+str(len(friends_name)))
user_input = int(input("Type 1 for All Accepted\nType 2 for All Deleted\n"))
#Confirm
if user_input == 1:
    for name in friends_name:
        print(name + "\nConfirm Request\n")
        print("Please Wait")
    for con in confirm:
        data = requests.get(con, cookies=cj)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
#Delete
elif user_input == 2:
    for name in friends_name:
        print(name + "\nDelete Request\n")
        print("Please Wait")
    for remove in delete:
        data = requests.get(delete, cookies=cj)
        soup = bs4.BeautifulSoup(data.text, "html.parser")
else:
        print("Wronge Input")