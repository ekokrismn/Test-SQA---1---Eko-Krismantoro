from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("https://www.tokopedia.com/")
titleweb = driver.title
print(titleweb)

search = driver.find_element(By.XPATH, '//*[@id="header-main-wrapper"]/div[2]/div[2]/div/div/div/div/input')
search.send_keys("kursi gaming")
time.sleep(3)

button_search = driver.find_element(By.XPATH, '//*[@id="header-main-wrapper"]/div[2]/div[2]/div/div/div/div/button')
button_search.click()
time.sleep(5)

result = driver.find_element(By.XPATH, '//*[@id="zeus-root"]/div/div[2]/div/div[2]/div[2]/span/div')
print("Total Product: " + result.text)

for x in range(0,700):
    driver.execute_script("window.scrollTo(0, "+str(x)+")")
    
time.sleep(1)

for x in range(700,5900):
    driver.execute_script("window.scrollTo(0, "+str(x)+")")

time.sleep(4)
driver.close()  

   
