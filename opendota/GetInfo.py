from pyparsing import javaStyleComment
import requests
import json

# r = requests.get("https://api.opendota.com/api/players/221608911/")
r = requests.get("https://api.opendota.com/api/matches/6672334709")

JsonText = json.loads(r.text)
Player = JsonText['players']

for i in range(10):
    print(Player[i]['kills'])


# f = open("dataTest.json",'a') 
# f.write(r.text)
# f.close()
