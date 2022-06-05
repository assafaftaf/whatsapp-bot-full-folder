from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os

#from cleancode import delete_quest 


user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='/home/assaf/Documents/sel/chromedriver', options=options)

driver.get('https://web.whatsapp.com')
driver.get_screenshot_as_file('screenshot.png')
print(driver.title)
"""
driver.get_screenshot_as_file('screenshot.png')
a=""
while(a!="done"):
    a=input("ready for another screenshot?")
    driver.get_screenshot_as_file('screenshot.png')
"""

def msg_is_hello():
    hello_words=["היי","הי","שלום","עזרה","אהלן"]
    msg=get_msg()
    for x in range(len(hello_words)):
        if(msg!= hello_words[x]):
            a=False
        else:    
            send_msg('שלום הגעתם למכונאי תורן! במידה ויש לכם שאלה כתבו לי את השאלה תוך הקפדה על סימן שאלה בסוף השאלה,למתן חומר על מערכת ניתן לכתוב את שם המערכת')
            return None
    if(a == False):
        #starting the next func,
        oil_system(msg)

def oil_system(msg):#1
    words=["שמן","1","מערכת שמן"]#custom
    files_path=["/home/assaf/Documents/sel/1/oil_system.pdf",]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על מערכת שמן:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
                return None
            
    if(a == False):
        #starting the next func,or:
        #custom
        fuel_system(msg)

def fuel_system(msg):#2
    words=["דלק","2","מערכת דלק"]#custom
    files_path=["/home/assaf/Documents/sel/2/fuel_system.pdf",]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על מערכת דלק:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
            return None
    if(a == False):
        #starting the next func,or:
        #custom
        air(msg)

def air(msg):#3
    words=["אוויר דחוס","מערכת מדחס","מדחס","3","מערכת אוויר דחוס"]#custom
    files_path=["/home/assaf/Documents/sel/3/air.pdf",]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על מערכת אוויר דחוס\מדחס:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
            return None
    if(a == False):
        #starting the next func,or:
        #custom
        water(msg)
        
        return None

def water(msg):#4
    words=["מים מתוקים","סניטרית","מערכת סניטרית","מערכת מים","4","מים"]#custom
    files_path=["/home/assaf/Documents/sel/4/water.pdf"]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על מערכת סניטרינית מים מתוקים:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
            return None
    if(a == False):
        #starting the next func,or:
        #custom
        firemain(msg)
        return None
    
def firemain(msg):#5
    words=["כא","5","כיבוי אש"]#custom
    files_path=["/home/assaf/Documents/sel/5/firemain.pdf",]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על מערכת כיבוי אש:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
            return None
    if(a == False):
        #starting the next func,or:
        #custom
        AC(msg)
        return None
    
def AC(msg):#6
    words=["מיזוג אויר","מיזוא","מיזו''א","מיזוג אוויר"]#custom
    files_path=["/home/assaf/Documents/sel/6/AC.pdf",]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על מערכת מיזוג אוויר:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
            return None
    if(a == False):
        #starting the next func,or:
        #custom
        gen(msg)
        return None
    
def gen(msg):#7
    words=["גנרטור","7"]#custom
    files_path=["/home/assaf/Documents/sel/7/gen.pdf",]#custom
    for x in range(len(words)):
        if(msg != words[x]):
            a=False
        else:    
            send_msg("כל מה שאני יודע על גנרטור:")#custom
            for i in range(len(files_path)):
                send_file(files_path[i])
                time.sleep(0.5)
            return None
    if(a == False):
        #starting the next func,or:
        #custom
        is_quest(msg)
        return None
    
#get the message i replayed
def get_replay():
    """
    check the last reaplay message we have in chat
    Returns:
        str: returns the replayed message we got
    """
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
def get_title():
    """
    checking with who we texting
    Returns:
        true if is it  bot questions else is false
    """
    message = driver.find_elements(By.XPATH,"//span[@class='ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr']")
    try:
        rmsg=message[len(message)-1].get_property("innerHTML")
        rmsg=str(rmsg)
        rmsg=rmsg.replace("</span>","")
        rmsg=rmsg.replace("<span>","")
        
        if(rmsg=="bot-questions"):
            return(True)
        else:
            return False
    except:
        pass

def get_msg():
    """_summary_

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

  
def send_file(file_name):
    driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
    driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(file_name)
    time.sleep(2)#need to check times!!!
    driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']").click()

def send_img(file_name):
    driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
    driver.find_element(By.CSS_SELECTOR,"input[type='image']").send_keys(file_name)
    time.sleep(2)#need to check times!!!
    driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']").click()

def send_msg(msg):
    elem2=driver.find_element(By.CLASS_NAME,'p3_M1')#text!
    elem2.click()
    elem2.send_keys(msg,Keys.ENTER)
    time.sleep(0.5)   
     
#questing: 
def is_quest(msg):
    try:  
        a=how_to_make_quest(msg)
        if(a==1):
            return None
        
        a=is_answer(msg) 
        if(a==1):
            return None
        
        a=exist_answer(msg)
        if(a==1):
            return None

        if(msg.find('?')!=-1):
            write_quest_to_file(msg)
            return None
        #somefiles
        #last func-1
        if(msg.find('נוהל')!=-1):#not working yet
            send_proc(msg)
        return None
    except:
        return None

def is_answer(msg):
    try:  

        if(get_title()==True):
            quest=get_replay()
            listq=os.listdir('./questions')
            for f in listq:
                if(f==quest):
                    if(msg.strip()=='במ'):
                        write_answer_to_file(quest,"שאלה זו נפסלה עקב בטחון מידע")
                        return 1
                    write_answer_to_file(quest,msg)
                    #send answer to asker()
                    return 1
            
                update_answer(quest,msg)
                return 1
    except:
        return 1

def send_proc(msg):
    path = "/home/assaf/Documents/sel/files"
    files = os.listdir(path)
    for f in files:
        if(str(f).strip()==str(msg).strip()+'.png'):
            print(f)
            print(msg)
            send_file(path+'/'+f)
            #send_file()
            time.sleep(0.5)
            return 1
    
#some funcs:
def delete_quest(tq):
    path = "/home/assaf/Documents/sel/questions/"
    
    print(path+tq)

    os.remove(path+tq)


def how_to_make_quest(msg):
    if(msg.find("איך לכתוב שאלה") ==0):
        time.sleep(0.5)
        send_msg(' לפני כתיבת שאלה מומלץ לבדוק שאלות של אנשים אחרים שניתנה להם כבר תשובה כדי לצפות בתשובות לחץ תשובות')
        send_msg("על מנת לכתוב שאלה יש להקפיד על שימוש בסימן שאלה כדי שהמערכת תוכל לקלוט את השאלה")
        return 1

    if(msg.find("איך לכתוב שאלה?") ==0):
        time.sleep(0.5)
        send_msg(' לפני כתיבת שאלה מומלץ לבדוק שאלות של אנשים אחרים שניתנה להם כבר תשובה כדי לצפות בתשובות לחץ תשובות')
        send_msg("על מנת לכתוב שאלה יש להקפיד על שימוש בסימן שאלה כדי שהמערכת תוכל לקלוט את השאלה")
        return 1

def watch_answers():
    try:
        path = '/home/assaf/Documents/sel/answers'
        files = os.listdir(path)
        for f in files:
            con=open(path+'/'+f,'r')
            time.sleep(0.5)
            send_msg(f+'->'+con.read())
            con.close()
    except:
        pass
    


def write_quest_to_file(tq):
    """writing quest to questions and send to group

    Args:
        tq (str): need to be in the end with '?'
    """
    tq=str(tq).strip()
    f=open("/home/assaf/Documents/sel/questions/"+tq,"a")
    f.write("")
    send_msg("קיבלתי את השאלה,אשתדל לענות בהקדם")
    bot_questions()
    send_msg(tq)
    f.close()
    
def write_answer_to_file(tq,bq):
    """write answer to file 
            and deleting the quest!
    Args:
        tq (str): title
        bq (str): answer
    """
    tq=str(tq).strip()
    f=open("/home/assaf/Documents/sel/answers/"+tq,"w")
    f.write(bq)
    f.close()
    delete_quest(tq)
    send_msg("תודה רבה!")

def update_answer(tq,bq):
    """this func update a answer when there is a mistake
    Args:
        tq (str): title vaierfied
        bq (str): answer to update
    """
    f=open("/home/assaf/Documents/sel/answers/"+tq,"w")
    f.write(bq)
    f.close()
    send_msg("תודה רבה!")
    
#func send answer for exist question
def exist_answer(msg):
    path = "/home/assaf/Documents/sel/answers"
    files = os.listdir(path)
    for f in files:
        con=open(path+'/'+f,'r')
        if(str(f).strip()==str(msg).strip()):
            send_msg(con.read())
            time.sleep(0.5)
            con.close()
            return 1
        con.close()
   
def bot_questions():
    user = driver.find_element(By.XPATH,"//span[@title='{}']".format('bot-questions'))
    user.click()
    
#mani func:
def main():
    
    a=input("ready to start?")
    while(a!="yes"):
        driver.get_screenshot_as_file('screenshot.png')
        a=input("ready to start?")
    while(True):
        try:
            #driver.get_screenshot_as_file('screenshot.png')
            elem=driver.find_element(By.CLASS_NAME,'_1pJ9J')#green dot
            #input("found message!")
            elem.click()

            msg_is_hello()
            user = driver.find_element(By.XPATH,"//span[@title='{}']".format('To-me'))
            user.click()
    
        except:
            pass

if __name__ == "__main__":
    main()