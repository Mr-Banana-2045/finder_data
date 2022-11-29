import requests
import argparse
import os, sys
from requests import get
import json

print("""
  \033[101;93m'########:'####:'##:::##:'########:::::'###::::'########::::'###::::\033[00m
\033[00m  \033[101;93m##.....::. ##:: ###:: ##: ##.... ##:::'## ##:::... ##..::::'## ##:::\033[00m
\033[00m  \033[101;93m##:::::::: ##:: ####: ##: ##:::: ##::'##:. ##::::: ##:::::'##:. ##::\033[00m
\033[00m  \033[101;93m######:::: ##:: ## ## ##: ##:::: ##:'##:::. ##:::: ##::::'##:::. ##:\033[00m
\033[00m  \033[101;93m##...::::: ##:: ##. ####: ##:::: ##: #########:::: ##:::: #########:\033[00m
\033[00m  \033[101;93m##:::::::: ##:: ##:. ###: ##:::: ##: ##.... ##:::: ##:::: ##.... ##:\033[00m
\033[00m  \033[101;93m##:::::::'####: ##::. ##: ########:: ##:::: ##:::: ##:::: ##:::: ##:\033[00m
\033[00m  \033[101;93m..::::::::....::.::\033[96mGitHub : Mr-Banana-2045\033[101;93m:::..:::::..:::::..:::::.:\033[00m

                \033[92m....:::::: \033[96mFINDER DATA \033[92m::::::....
             \033[96mFind out information of desired person\033[92m
""")
parser = argparse.ArgumentParser()

parser.add_argument('-tel', help= "phone target", type=str, required=True)
parser.add_argument('-ip', help= "ip target", type=str, dest='target', required=True)

args = parser.parse_args()

if (str(args.tel[::-1])==str(args.tel)):
	sys.exit(0)
else:
    print(" \033[101;93mname target\033[00m")
    print("\033[92m__________________________")
    print("name : ",get("https://numberbook.aryandev.ir/api.php" , json = {"number":args.tel}).json()["data"])
    print("")

print("\033[101;93minformation ip target\033[00m")
print("\033[92m______________________________")
data = requests.get("http://ip-api.com/json/"+args.target).json()
print("Organisation : ", data['org'])
print("City : ", data['city'])
print("Country : ", data['country'])
print("Region : ", data['region'])
print("Ngitude : ", data['lon'])
print("Latitude : ", data['lat'])
print("Region : ", data['region'])
print("Time zone : ", data['timezone'])
print("country Code : ", data['countryCode'])