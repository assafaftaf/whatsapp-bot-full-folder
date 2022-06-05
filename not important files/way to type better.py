from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/assaf/Documents/sel/chromedriver')#driver  
    # Navigate to url
driver.get("http://www.google.com")

    # Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver " )
driver.find_element(By.NAME, "q").send_keys("webdriver " )
 
driver.find_element(By.NAME, "q").send_keys("webdriver " )  

driver.find_element(By.NAME, "q").send_keys("webdriver " )  

driver.find_element(By.NAME, "q").send_keys("webdriver " )
driver.find_element(By.NAME, "q").send_keys("12312423 " )


    # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
  