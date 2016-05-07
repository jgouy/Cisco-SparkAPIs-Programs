#!/usr/bin/python

# Keep Reading Spark room to find any command from the operator
#
while True:
#
#       import os
#       import subprocess
        import sys
        import requests
#       retcode = os.system("echo 'foo &> /dev/null")
#
#       sys.path.insert(0, '/usr/lib/python2.7/bridge')
#
        from time import sleep
#       from bridgeclient import BridgeClient as bridgeclient
#
#       value = bridgeclient()
#
        url = "https://api.ciscospark.com/v1/messages"
#
        querystring = {"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vZDhiNjk3MDAtZjM3Yi0xMWU1LWJiMDctYjFhZjQ4ZGRhMzYy","max":"1"}
#
        headers = {
        'authorization': "Bearer ZjdmZjYzMDgtMjMxNC00NTYwLTlmNWEtZDE3MTE3ZWI0OWU1YTVjNmY1NmYtMmJl",
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "8da75f6c-2ce7-87ec-8bc1-15619d22f10c"
        }
#
        response = requests.request("GET", url, headers=headers, params=querystring)
#
        if 'Spark turn alarm off please' in response.text:
                print('Desligue o Alarme via Comando para o Arduino')
#                value.put('D13','1')
                sleep(10)

        if 'Spark turn alarm on please' in response.text:
                print('Ligue o Alarme via Comando para o Arduino')
#                value.put('D13','0')
                sleep(10)
#
print("Spark Command Lookup Running...\n")

