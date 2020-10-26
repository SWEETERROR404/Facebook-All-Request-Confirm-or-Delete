import os,time,http.cookiejar,urllib.request,getpass,requests,bs4
logo = """\033[1;32;40m
        __                                           __
       (**)                                         (**)
       IIII                                         IIII
       ####                                         ####
       HHHH     Madness comes, and madness goes     HHHH
       HHHH    An insane place, with insane moves   HHHH
       ####   Battles without, for battles within   ####
    ___IIII___        Where evil lives,          ___IIII___
 .-`_._"**"_._`-.      and evil rules         .-`_._"**"_._`-.
|/``  .`\/`.  ``\|    Breaking them up,      |/``  .`\/`.  ``\|
`     }    {     '  just breaking them in    `     }    {     '
      ) () (  Quickest way out, quickest way wins  ) () (
      ( :: )      Never disclose, never betray     ( :: )
      | :: |   Cease to speak or cease to breath   | :: |
      | )( |        And when you kill a man,       | )( |
      | || |          you're a murderer            | || |
      | || |             Kill many                 | || |
      | || |        and you're a conqueror         | || |
      | || |        Kill them all ... Ooh..        | || |
      | || |           Oh you're a God!            | || |
      ( () )                                       ( () )
       \  /                                         \  /
        \/                                           \/

"""
welcome = """\033[1;33;40m
´
´´
´´´
´´´´
´´´´´´´´´´´´´´´´´¶
´´´´´´´´´´´´´´¶´´¶´´´¶¶
´´´´´´´´´´´´´´¶´¶¶´¶¶
´´´´´´´´´¶¶¶¶´´´´´´¶¶¶¶¶¶
´´´´´´´¶¶´´´´´´´´´´´´´´´´¶¶
´´´´´¶¶´´´´´´´´¶¶´´´´´´´´´´¶¶
´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´¶¶
´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶
´´¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶´¶
´¶´´´´´´´´´´´´´´´´¶´´´´´´´´´´´´´¶
´¶´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´¶
´¶´´´´´´´´´´´´¶¶´¶´´´´´´´´´´´¶´´´¶
´¶´´´´´´´´´´¶¶¶¶¶¶´´´´´´´¶¶¶¶´´´´¶
´¶´´´´´´´´´¶¶¶¶¶¶¶´´´´´´¶¶´´¶´´´´¶
´´¶´´´´´´´´¶¶¶¶¶´¶´´´´´¶¶¶¶¶¶´´´¶
´´¶¶´´´´´´´¶´´´´´¶´´´´¶¶¶¶¶¶´´´¶¶
´´´¶¶´´´´´´¶´´´´¶´´´´¶¶¶¶´´´´´¶
´´´´¶´´´´´´¶´´´¶´´´´´¶´´´´´´´¶
´´´´¶´´´´´´¶¶¶¶´´´´´´´´´¶´´¶¶
´´´´¶¶´´´´´´´´´´´´´´´¶¶¶´´¶     \033[1;31;40m░█──░█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀\033[1;33;40m
´´´´´¶¶¶´´´´´´´¶¶¶¶¶´´´´´´¶     \033[1;31;40m░█░█░█ █▀▀ █── █── █──█ █─▀─█ █▀▀\033[1;33;40m
´´´´´´´´¶¶¶´´´´´¶¶´´´´´´´¶¶     \033[1;31;40m░█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀\033[1;33;40m
´´´´´´´´´´´´¶¶´´´´´¶¶¶¶¶¶´
´´´´´´´´´´¶¶´´´´´´¶¶´¶
´´´´´´´¶¶¶¶´´´´´´´´¶´¶¶
´´´´´´´´´¶´´¶¶´´´´´¶´´´¶
´´´´¶¶¶¶¶¶´¶´´´´´´´¶´´¶´
´´¶¶´´´¶¶¶¶´¶´´´´´´¶´´´¶¶¶¶¶¶¶
´´¶¶´´´´´´¶¶¶¶´´´´´¶´¶¶´´´´´¶¶
´´¶´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´¶
´´´¶¶´´´´´´´´´¶´´´¶´´´´´´´´´´¶
´´´´¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶ ~*▀
"""
print(welcome)
time.sleep(3)
os.system('clear')
print(logo)
time.sleep(3)
l1="\033[1;32;40m If Any Problem than contact me on facebook account "
l2="\033[1;31;40m ------> https://m.facebook.com/Python3.7.py <------ "
l3="\033[1;32;40m       \t         Contact me on Github  "
l4="\033[1;31;40m ------> https://github.com/CodeWithMubeen   <------ "
print(f'{l1}\n{l2}\n{l3}\n{l4}')
email = input("Enter your facebook Email / Phone Number :- ")
password = getpass.getpass("Enter your Password :- ")
print("Please Wait")
time.sleep(2)
os.system('clear')
print(logo)
print(f'{l1}\n{l2}\n{l3}\n{l4}')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
authentication_url = "https://m.facebook.com/login.php"
payload = {
    'email': email,
    'pass': password
}
print("Please Wait")
data = urllib.parse.urlencode(payload).encode('utf-8')
req = urllib.request.Request(authentication_url, data)
resp = urllib.request.urlopen(req)
contents = resp.read()
def searcher(url):
    data = requests.get(url, cookies=cj)
    soup = bs4.BeautifulSoup(data.text, "html.parser")
    return soup
error = searcher(authentication_url).find(id='login_error')
if error != None:
    print(str(error).split("=")[2].split('"')[1].replace("_",' ').casefold())
print("Please wait for Extracting all Requests")
#Go to Friends Requests
url = "https://mbasic.facebook.com/friends/center/requests/#friends_center_main"
#see_more links extract
see_more = ["https://mbasic.facebook.com/friends/center/requests/"]
for i in see_more:
    for x in searcher(i).findAll(id="u_0_0"):
        for link in x.findAll("a"):
            href = link.get("href")
            if href[16] == "r":
                var = see_more.append("https://mbasic.facebook.com" + str(href)) == True
friends_name = []
confirm = []
delete = []
# class bm for link 0
for i in searcher(see_more[0]).findAll('div', class_="bm"):
    no = 0
    for a in i.findAll('a'):
        if no == 0:
            # name
            friends_name.append(a.text.replace("‏‎", "").replace("‎‏", "").replace("‏", ""))
        elif no == 1:
            # confirm request
            confirm.append('https://mbasic.facebook.com' + str(a).replace('"', "\n").split("\n")[3].replace("amp;", ""))
        elif no == 2:
            # Delete request
            delete.append('https://mbasic.facebook.com' + str(a).replace('"', "\n").split("\n")[3].replace("amp;", ""))
        no += 1
for next_class in see_more:
   for i in searcher(next_class).findAll('div', class_="bk"):
        no = 0
        for a in i.findAll('a'):
            if no == 0:
                friends_name.append(a.text.replace("‏‎","").replace("‎‏","").replace("‏",""))
            elif no == 1:
                # confirm request
                confirm.append('https://mbasic.facebook.com' + str(a).replace('"', "\n").split("\n")[3].replace("amp;", ""))
            elif no == 2:
                # Delete request
                delete.append('https://mbasic.facebook.com' + str(a).replace('"', "\n").split("\n")[3].replace("amp;", ""))
            no += 1
print("Total Requests "+str(len(friends_name)))
while True:
        user_input = input("Type 1 for All Accepted\nType 2 for All Deleted\n")
        if user_input > "2" or user_input < "1":
            print("Please Type Only 1 or 2 Number ")
        else:
            if int(user_input) == 1:
                for con in confirm:
                    searcher(con)
                break
            else:
                for remove in delete:
                    searcher(remove)
                break
