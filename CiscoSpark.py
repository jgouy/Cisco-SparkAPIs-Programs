#!/usr/bin/env python

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("t")
parser.add_argument("h")
args = parser.parse_args()

# print args.t
# print args.h

str1 = """{\r\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vZDhiNjk3MDAtZjM3Yi0xMWU1LWJiMDctYjFhZjQ4ZGRhMzYy\","""
filename = """\"file\": \"http://www.ti.com/lsds/sites/ti/analog/sensors/images/icon-temperature.png","""
str2 = """\"text\": \"EnvMon Alert (SE1540) Fora do Padrao => """
str3 = "Temp: " + args.t + "c" + " Humi: " + args.h + "%"
str4 = """\"\r\n}"""
#
url = "https://api.ciscospark.com/v1/messages"

stringa = str1 + filename + str2 + str3 + str4

payload = stringa
print payload

headers = {
   'authorization': "Bearer ZjdmZjYzMDgtMjMxNC00NTYwLTlmNWEtZDE3MTE3ZWI0OWU1YTVjNmY1NmYtMmJl",
   'content-type': "application/json",
   'cache-control': "no-cache",
   'postman-token': "3cd027f8-9c39-13c1-dc6a-4c8f251e9735"
          }
response = requests.request("POST", url, data=payload, headers=headers)
