import argparse
import requests, json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()
parser.add_argument ("-t", help= "TARGET/HOST", type=str, dest='target', required=True )
args = parser.parse_args()

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

ip = args.target
api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = red+bold+"[+]"
        b = lgreen
        print("\n")
        print (a, "[IP]:", b, data['query'])
        print (a, "[ISP]:", b, data['isp'])
        print (a, "[Organization]:", b, data['org'])
        print (a, "[City]:", b, data['city'])
        print (a, "[Region]:", b, data['region'])
        print (a, "[Longitude]:", b, data['lon'])
        print (a, "[Latitude]:", b, data['lat'])
        print (a, "[Time Zone]:", b, data['timezone'])
        print (a, "[Zip Code]:", b, data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print (red+bold+"[-] End.")
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" [-] Conection Error."+clear)
sys.exit(1)
