from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import os
rege = "^[\/\?].+|^\w.+[\/]$"

url = "http://ricardonarvaja.info/WEB/"
dirs = ["ANDROID%20REVERSING/",
"C++%20DESDE%20CERO/",
"CONCURSOS%202009/",
"CONCURSOS%202010/",
"CONCURSOS%202011/",
"CONCURSOS%202012/",
"CONCURSOS%202013/",
"CONCURSOS%20TRIMESTRALES/",
"CONCURSOS%20VIEJOS/",
"CRACKING%20PARA%20BEBES%20POR%20IVINSON/",
"CURSO%20DE%20ARM%20EXPLOIT/",
"CURSO%20NUEVO/",
"CURSO%20VIEJO/",
"C%20Y%20REVERSING/",
"DEBUGGERS%20PARA%20LOS%20NUEVOS%20WINDOWS%2032%20Y%2064%20BITS/",
"EXPLOITING/",
"EXPLOITING%20Y%20REVERSING%20USANDO%20HERRAMIENTAS%20FREE/",
"IDA%20DESDE%20CERO/",
"INTRODUCCION%20AL%20CRACKING%20CON%20OLLYDBG%20DESDE%20CERO/",
"INTRODUCCION%20AL%20CRACKING%20CON%20XDBG%20POR%20ANGEL%20ZARZA/ ",
"OTROS/",
"RADARE/",
"RUBY%20POR%20TINCOPASAN/"]
os.mkdir("RN")
os.chdir("RN")
for dir in dirs:
    os.mkdir(dir)
    os.chdir(dir)
    opened = url + dir
    html_page = urlopen(opened)
    soup = BeautifulSoup(html_page, features="html.parser")
    for link in soup.findAll('a'):
        file = link.get('href')
        if  not re.search(rege, file):
            r = requests.get((opened + file), allow_redirects=True)
            open(file, 'wb').write(r.content)

        elif re.search("^\w.+/$", file):
            os.mkdir(file)
            os.chdir(file)
            sopa = BeautifulSoup(urlopen((opened + file)), features="html.parser")
            for links in sopa.findAll('a'):
                file1 = links.get('href')
                if not re.search(rege, file1):
                    r = requests.get((opened + file + file1), allow_redirects=True)
                    open(file1, 'wb').write(r.content)

                elif re.search("^\w.+/$", file1):
                    os.mkdir(file1)
                    os.chdir(file1)
                    sopas = BeautifulSoup(urlopen((opened + file + file1)), features="html.parser")
                    for linkss in sopas.findAll('a'):
                        file2 = linkss.get('href')
                        if  not re.search(rege, file2):
                            r = requests.get((opened + file + file1 + file2), allow_redirects=True)
                            open(file2, 'wb').write(r.content)
                        elif re.search("^\w.+/$", file2):
                            os.mkdir(file2)
                            os.chdir(file2)
                            sopass = BeautifulSoup(urlopen((opened + file + file1 + file2)), features="html.parser")
                            for linksss in sopass.findAll('a'):
                                file3 = linksss.get('href')
                                if not re.search(rege, file3):
                                    r = requests.get((opened + file + file1 + file2 + file3), allow_redirects=True)
                                    open(file3, 'wb').write(r.content)
                            os.chdir("../")
                    os.chdir("../")
            os.chdir("../")
    os.chdir("../")
