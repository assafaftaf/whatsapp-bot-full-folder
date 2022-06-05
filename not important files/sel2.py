from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os 


driver = webdriver.Chrome('/home/assaf/Documents/sel/chromedriver')#driver  
driver.get("http://web.whatsapp.com")#link
driver.maximize_window()

#quoted-mention i0jNr
#message = driver.find_elements(By.XPATH,"//span[@class='i0jNr selectable-text copyable-text']") 

def msg_is_hello():
    hello_words=["היי","הי","שלום","עזרה","אהלן"]
    msg=get_msg()
    for x in range(len(hello_words)):
        if(msg!= hello_words[x]):
            a=False
        else:    
            send_msg('שלום! הגעתם למכונאי תורן על מנת לקבל את תוכן המערכת אותה אתם לומדים הזינו את שם המערכת,במידה ויש לכם שאלה ניתן לכתוב אותה,במידה ולא יהיה מענה יש לכתוב:איך לכתוב שאלה כדי לענות על שאלות של מתלמדים יש לכתוב:איך לענות על שאלה')
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
    words=["מיזו''א","מיזוג אוויר"]#custom
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
    
def get_msg():
    message = driver.find_elements(By.XPATH,"//span[@class='i0jNr selectable-text copyable-text']") 
    try:
        rmsg=message[len(message)-1].get_property("innerHTML")
        rmsg=str(rmsg)
        rmsg=rmsg.replace("</span>","")
        rmsg=rmsg.replace("<span>","")
        return rmsg
    except:
        pass
#returning the msg(rmsg)

#sending:
def send_file(file_name):
    driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
    driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(file_name)
    time.sleep(2)#need to check times!!!
    driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']").click()
    
def send_msg(msg):#try name
    elem2=driver.find_element(By.CLASS_NAME,'p3_M1')#text!
    elem2.click().perform()
    elem2.send_keys(msg,Keys.ENTER).perform()
    time.sleep(0.5)   
###################

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
        #last func
        return None
    except:
        return None

def is_answer(msg):
    try:  
        how_to_make_answer(msg)
        
        if(msg.find("התשובה שלי:") !=-1):
            tq=msg[21:msg.find("התשובה שלי:")]
            print(tq)
            bq=msg[msg.find("התשובה שלי:")+11:len(msg)]
            write_answer_to_file(tq,bq,msg)
            return 1
    except:
        return 1

def some_files(msg):
    try: 
        if(msg.find('הסבר משאבת גג"ש')!=-1):
            send_file('./files/')
        #last func
        return None
    except:
        return None
    
#some funcs:
def delete_quest(tq):
    print("here")
    path = "/home/assaf/Documents/sel/questions/"
    
    print(path+tq)

    os.remove(path+tq)

def how_to_make_answer(msg):
    if(msg.find("איך לענות על שאלה") == 0):
        time.sleep(0.5)
        send_msg("שאלות של אנשים:")
        watch_quests()
        send_msg('נוסח תשובה לשאלה')
        send_msg("השאלה עלייה אני עונה:כאן תינתן השאלה עלייה בחרת לענות התשובה שלי:כאן תינתן התשובה שלך לשאלה")
        return None

    if(msg.find("איך לענות על שאלה?") == 0):
        time.sleep(0.5)
        send_msg("שאלות של אנשים:")
        watch_quests()
        send_msg('נוסח תשובה לשאלה')
        send_msg("השאלה עלייה אני עונה:הכאן תינתן השאלה עלייה בחרת לענות התשובה שלי:הכאן תינתן התשובה שלך לשאלה")
        return None
#able to delete^ no need any more
def how_to_make_quest(msg):
    if(msg.find("איך לכתוב שאלה") ==0):
        time.sleep(0.5)
        send_msg("על מנת לכתוב שאלה יש להקפיד על שימוש בסימן שאלה כדי שהמערכת תוכל לקלוט את השאלה")
        return 1

    if(msg.find("איך לכתוב שאלה?") ==0):
        time.sleep(0.5)
        send_msg("על מנת לכתוב שאלה יש להקפיד על שימוש בסימן שאלה כדי שהמערכת תוכל לקלוט את השאלה")
        return 1
#able to delete^ no need any more

def watch_quests():#sprint all quests!
    try:    
        path = "/home/assaf/Documents/sel/questions"
        files = os.listdir(path)
        for f in files:
            time.sleep(0.3)
            send_msg(f)
    except:
        pass

def write_quest_to_file(tq):
    tq=str(tq).strip()
    f=open("/home/assaf/Documents/sel/questions/"+tq,"a")
    f.write("")
    send_msg("קיבלתי את השאלה,אשתדל לענות בהקדם")
    bot_questions()
    send_msg(tq)
    f.close()
    
def write_answer_to_file(tq,bq,msg):
    tq=str(tq).strip()
    f=open("/home/assaf/Documents/sel/answers/"+tq,"a")
    f.write(bq)
    f.close()
    delete_quest(tq)
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
   
def searching_dot():
    elem=driver.find_element(By.CLASS_NAME,'_1pJ9J')#green dot
    #input("found message!")
    elem.click()
    
def To_me():
    user = driver.find_element(By.XPATH,"//span[@title='{}']".format('To-me'))
    user.click()
    
def bot_questions():
    user = driver.find_element(By.XPATH,"//span[@title='{}']".format('bot-questions'))
    user.click()
#mani func:
def main():
    input("ready to start?")
    while(True):
        try:
            searching_dot()
            #if()#msg is replay
            #then get msg() and get replayied 
            #answer of reaplayied =msg
            #delete qust by msg
            msg_is_hello()
            To_me()
        except:
            pass

if __name__ == "__main__":
    main()