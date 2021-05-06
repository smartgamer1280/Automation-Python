import pyautogui,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Chrome(r'C:\chromedriver.exe')

driver.implicitly_wait(5)

a='https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F'
driver.get(a)





uname=driver.find_element_by_xpath('//*[@id="login-username"]')
uname.click()


email_id='your id'


uname.send_keys(email_id)


passw=driver.find_element_by_xpath('//*[@id="login-password"]')
passw.click()


Password='''Your password'''
passw.send_keys(Password)




submitbtn='//*[@id="login-button"]'
Submit=driver.find_element_by_xpath(submitbtn)


Submit.click()



driver.implicitly_wait(20)


playlist=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/nav/div[2]/div/div[3]/div[4]/div/div/ul/div[2]/li/a/span')

playlist.click()

driver.implicitly_wait(10)

start_playing=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[4]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')

start_playing.click()

driver.maximize_window()







	
