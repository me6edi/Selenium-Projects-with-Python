from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

path = "C:/Users/Mehedi Amin/Downloads/Compressed/chromedriver_win32/chromedriver.exe"

s = Service(path)

driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/") 
time.sleep(1)

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("me6edi")
box.send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element_by_xpath("""//*[@id="rso"]/div[1]/div/div/div[1]/div/a""").click()
time.sleep(1)
driver.find_element_by_xpath("""/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]""").click()

driver.save_screenshot('C:/Users/Mehedi Amin/Desktop/Selenum/mehedi1.jpg')
time.sleep(3)


# element = driver.find_element_by_tag_name('body')
# while True:
#     element.send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)

element = driver.find_element_by_tag_name('html')

element.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.HOME)
time.sleep(3)

driver.get("https://www.google.com/") 
time.sleep(1)

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("me6edi")
box.send_keys(Keys.ENTER)
time.sleep(1)

driver.find_element_by_xpath('''//*[@id="rso"]/div[2]/div/div/div[1]/div/a/div/div/div/cite''').click()

element = driver.find_element_by_tag_name('html')

element.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(2)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
element.send_keys(Keys.HOME)
time.sleep(3)

driver.get("https://www.google.com/") 
time.sleep(2)

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("me6edi")
box.send_keys(Keys.ENTER)
time.sleep(3)


driver.find_element_by_xpath('''//*[@id="rso"]/div[4]/div/div/div/div[1]/div/a/div/div/div/cite''').click()

driver.get("https://www.youtube.com/") 
time.sleep(2)
song = driver.find_element_by_xpath("""/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input""")
song.send_keys("KSHMR & Lost Stories")
song.send_keys(Keys.ENTER)
time.sleep(2)
driver.get("https://www.youtube.com/watch?v=EW4pNzAbVao&list=RDEW4pNzAbVao&start_radio=1").click()