from numpy import equal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os 


#quoted-mention i0jNr
#message = driver.find_elements(By.XPATH,"//span[@class='i0jNr selectable-text copyable-text']") 
driver = webdriver.Chrome('/home/assaf/Documents/sel/chromedriver')#driver  
driver.get("http://web.whatsapp.com")#link
driver.maximize_window()

#get the message i replayed
def get_replay():
    message = driver.find_elements(By.XPATH,"//span[@class='quoted-mention i0jNr']") 
    try:
        rmsg=message[len(message)-1].get_property("innerHTML")
        rmsg=str(rmsg)
        rmsg=rmsg.replace("</span>","")
        rmsg=rmsg.replace("<span>","")
        return rmsg
    except:
        pass
    
#return true if if title equals to 'b'
def get_title(b="bot-questions"):
    message = driver.find_elements(By.XPATH,"//span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
    try:
        rmsg=message[len(message)-1].get_property("innerHTML")
        rmsg=str(rmsg)
        rmsg=rmsg.replace("</span>","")
        rmsg=rmsg.replace("<span>","")
        
        if(rmsg==b):
            return(True)
        else:
            return False
    except:
        pass
    
def main():
    input("ready to start?")
    while(True):
        try:
            elem=driver.find_element(By.CLASS_NAME,'_1pJ9J')#green dot
            #input("found message!")
            elem.click()
            
            M=get_title()
            print(M)
            
            user = driver.find_element(By.XPATH,"//span[@title='{}']".format('To-me'))
            user.click()
    
        except:
            pass

if __name__ == "__main__":
    main()