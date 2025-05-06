from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

input_box = driver.find_element(By.NAME, "q")

input_box.send_keys("America")

input_box.send_keys(Keys.RETURN)

i = input('Done lagging?')
wiki = driver.find_element(By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md')
wiki.click()

for g in range(10):
    i = input('Done lagging?')
    content = driver.find_element(By.CSS_SELECTOR, '.mw-content-ltr.mw-parser-output')
    links = content.find_elements(By.TAG_NAME, "a")
    count = 0
    for link in links:
        href = link.get_attribute("href")
        if href and "wikipedia.org" in href:
            count += 1
            if count == 8:
                driver.execute_script("arguments[0].click();", link)
                break
    

i = input('Finish browsing?')
driver.quit()
