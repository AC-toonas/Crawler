from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from sys import exit

def GetLinkInPage():
    global max
    if QueueOfLinks:
        l = QueueOfLinks.pop(0)
        if not l in QueueOfVisited:
            QueueOfVisited.append(l)
            driver.get(l)

            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.mw-content-ltr.mw-parser-output'))
            )

            content = driver.find_element(By.CSS_SELECTOR, '.mw-content-ltr.mw-parser-output')
            links = content.find_elements(By                         .TAG_NAME, "a")

            if not max:
                for link in links:
                    href = link.get_attribute("href")
                    if href and "wikipedia.org" in href:
                        QueueOfLinks.append(href)






def CheckPageForRequirements():
    pass

def CheckForResponse():
    global max
    while True:
        cmd = input('Waiting for an response...')
        if cmd == "y" or cmd == "continue":
            GetLinkInPage()
        elif cmd == "exit":
            exit()
            print("program ended.")

        elif cmd == "links":
            print("There are a total of %s recorded links." %len(QueueOfLinks))
        elif cmd == "visited":
            print("There are a total of %s visited links."%len(QueueOfVisited))
        elif cmd == "liked":
            for p in QueueOfLiked:
                print(p)

        elif cmd == "maxtrue":
            max = True
            print("Max set to True.")
        elif cmd == "maxfalse":
            max = False
            print("Max set to False.")
        elif cmd == "record":
            QueueOfLiked.append(driver.current_url)
            print("Current url added to list.")
        
        elif cmd == "help":
            for line in helpdict:
                print(line) 
        elif cmd == "explain":
            print("The crawler, or internet crawler, is an algorithm that is helpful for searching online. For more information go to: ", r"https://www.akamai.com/glossary/what-is-a-web-crawler#:~:text=A%20web%20crawler%20is%20an,RSS%20aggregation%2C%20among%20other%20tasks.")
        else:
            print("Unknown command. Please check for mistakes or type help for a list of commands.")
        


QueueOfLinks = ["https://en.wikipedia.org/wiki/Game_theory"]
QueueOfVisited = []
QueueOfLiked = []

global max
max = False
helpdict = ["y/continue - continue the crawler to the next recorded page.", "exit - stop the crawler.",
            "links - print all recorded links", "visited - print all visited links", "liked - print all recorded links",
            "maxtrue - Set max to True. This stops the program from recording the links.", "maxfalse - Set max to false. This restarts the program from collecting links.",
            "record - record current link.", "help - print out a list of commands", "explain - explain what the crawler is."]

print("Please wait while we load the crawler...")

driver = webdriver.Chrome()
print("Window opened.")
time.sleep(1)


GetLinkInPage()
CheckForResponse()
