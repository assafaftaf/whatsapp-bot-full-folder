"""
        this doc contain funcs to send whatsupp message and recive automate!
        use start and enter ur chromedriver name, make sure ur chromedriver located in the file folder
"""
from glob import glob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os
  
def start(name,x):
    """starts the whatsupp with chrome driver, make sure you got the version for your google chrome
    the func wait x time until you log into web whatsupp

    Args:
        name (str): name of chorme-driver file
        x (int):time to wait until u log in whatsupp web
    """
    
    driver = webdriver.Chrome('./'+name)#driver  
    driver.get("http://web.whatsapp.com")#link
    driver.maximize_window()
    time.sleep(x)
    #how to make a global var
    #global driver...
    
def get_msg(driver):
    """this func will recive a message (incomming) and return it example code:
    while(True):
        msg=get_msg()
    
    message will recive when it upcomming
    
    Returns:
        returning the msg(rmsg)
    """
    message = driver.find_elements(By.XPATH,"//span[@class='i0jNr selectable-text copyable-text']") 
    try:
        rmsg=message[len(message)-1].get_property("innerHTML")
        rmsg=str(rmsg)
        rmsg=rmsg.replace("</span>","")
        rmsg=rmsg.replace("<span>","")
        return rmsg
    except:
        pass

