from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pt
import time

driver = webdriver.Chrome(r'C:\chromedriver.exe')
a='https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F'
driver.get(a)



try:
    element1 = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,  ' //*[@id="login-username"] '))
    )
    element1.click()
    element1.send_keys("shyambali40@gmail.com")
except:
    
    driver.implicitly_wait(4)


try:
    element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,  ' //*[@id="login-password"] '))
    )
    element.click()
    element.send_keys('9982831397k')
except:
    
    driver.implicitly_wait(4)

login_button = driver.find_element_by_xpath('//*[@id="login-button"]')
login_button.click()

import time;time.sleep(2)

driver.get('https://open.spotify.com/playlist/2me0h2IiOMyDoJk8WSOPol')

try:
    play_button = '//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]'
    element3 = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,play_button))
    )
    element3.click()
    
except:
    play_button = '//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]'
    element3 = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,play_button))
    )
    element3.click()
'''
fav = input("Enter: ")
if fav is not None:
    search = '/html/body/div[4]/div/div[2]/nav/div[1]/ul/li[2]/a'
    aa = driver.find_element_by_xpath(search)
    aa.click()
    
    pt.write(fav)


    
    elementdi = '/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/input'
    be = driver.find_element_by_xpath(elementdi)
    be.click()

'''

    




