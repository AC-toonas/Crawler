#BFS good GUI
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
from sys import exit

def GetLinkInPage():
    global max
    if QueueOfLinks:
        l = QueueOfLinks.pop(0)
        if l not in QueueOfVisited:
            QueueOfVisited.append(l)
            driver.get(l)
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.mw-content-ltr.mw-parser-output'))
            )
            content = driver.find_element(By.CSS_SELECTOR, '.mw-content-ltr.mw-parser-output')
            links = content.find_elements(By.TAG_NAME, "a")
            if not max:
                for link in links:
                    href = link.get_attribute("href")
                    if href and "wikipedia.org" in href:
                        QueueOfLinks.append(href)

def CheckForResponse(cmd):
    global max
    if cmd == "y" or cmd == "continue":
        GetLinkInPage()
    elif cmd == "exit":
        driver.quit()
        messagebox.showinfo("Crawler", "Program ended.")
        window.destroy()
        exit()

        
    elif cmd == "links":
        messagebox.showinfo("Crawler", "There are a total of %s recorded links." % len(QueueOfLinks))
    elif cmd == "visited":
        messagebox.showinfo("Crawler", "There are a total of %s visited links." % len(QueueOfVisited))
    elif cmd == "liked":
        for p in QueueOfLiked:
            messagebox.showinfo("Liked Page", p)
    elif cmd == "maxtrue":
        max = True
        messagebox.showinfo("Crawler", "Max set to True.")
    elif cmd == "maxfalse":
        max = False
        messagebox.showinfo("Crawler", "Max set to False.")
    elif cmd == "record":
        QueueOfLiked.append(driver.current_url)
        messagebox.showinfo("Crawler", "Current URL added to list.")
    elif cmd == "help":
        for line in helpdict:
            messagebox.showinfo("Help", line)
    elif cmd == "explain":
        messagebox.showinfo("Explain", "The crawler is an algorithm that helps search online.\n\nMore info:\nhttps://www.akamai.com/glossary/what-is-a-web-crawler")
    else:
        messagebox.showinfo("Crawler", "Unknown command. Type 'help' for a list of commands.")

def userenter(event):
    cmd = userinput.get()
    userinput.set("")
    threading.Thread(target=CheckForResponse, args=(cmd,)).start()

def start_driver_and_crawl():
    global driver
    driver = webdriver.Chrome()
    window.after(0, lambda: messagebox.showinfo("Crawler", "Window opened."))
    GetLinkInPage()

window = Tk()
window.geometry('800x800')
window.title('Crawler')
window.maxsize(800, 400)
window.minsize(200, 200)
window.configure(bg='Black')
window.iconbitmap(r"C:\Users\14168\OneDrive\Desktop\Mingxi_Chen\Python\Algorithms\Internet\Browsers\Crawler\CrawlerAppIcon.ico")

title = Label(window, text="AC 3000",bg="Black", fg="White", font=("haiti", 65))
title.place(x=400, y=125, anchor="center")

t1 = Label(window, text="Insert commands below",bg="Black", fg="White", font=("haiti", 20))
t1.place(x=400, y=190, anchor="center")

userinput = StringVar()
inputholder = Entry(window, textvariable=userinput, width=30, font=("haiti", 30))
inputholder.place(x=400, y=270, anchor="center")
inputholder.bind("<Return>", userenter)

QueueOfLinks = ["https://en.wikipedia.org/wiki/%s" %simpledialog.askstring("AC3000 message", "What topic do you want to use crawler on? Please insert format based on the last section of the wikipedia link.")]
QueueOfVisited = []
QueueOfLiked = []
max = False
helpdict = [
    "y/continue - continue the crawler to the next recorded page.",
    "exit - stop the crawler.",
    "links - print all recorded links",
    "visited - print all visited links",
    "liked - print all recorded links",
    "maxtrue - Set max to True. This stops the program from recording the links.",
    "maxfalse - Set max to false. This restarts the program from collecting links.",
    "record - record current link.",
    "help - print out a list of commands",
    "explain - explain what the crawler is."
]

try:
    messagebox.showinfo("Crawler", "Please wait while we load the crawler...")
    threading.Thread(target=start_driver_and_crawl).start()
except:
    messagebox.showerror("Error", "There has been an error.")

mainloop()
