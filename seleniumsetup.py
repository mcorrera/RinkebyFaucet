import random
import time

# import undetected_chromedriver as uc
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

global driver


def end():
    global driver
    driver.quit()


def randomsleep():
    delaytime = random.randrange(5, 10)
    time.sleep(delaytime)


def setoptions():
    myoptions = Options()
    myoptions.add_argument("--incognito")
    return myoptions


def scrollwindow():
    driver.execute_script("window.scrollTo(0, 1500)")
    time.sleep(2)


def waitforit(csstoget):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, csstoget))
        )
        print(f"{csstoget} was FOUND!")
        time.sleep(1)
        return True
    except:
        print(f"{csstoget} was not found.")
        return False


def initUCdriver(proxies):
    global driver
    chrome_options = uc.ChromeOptions()
    if proxies:
        PROXY = "46.4.73.88:2000"  # IP:PORT or HOST:PORT
        chrome_options.add_argument("--proxy-server=%s" % PROXY)
    chrome_options.headless = False
    driver = uc.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    print(f"UC Driver Initalized.")

    return driver


def initchromedriver(proxies):
    global driver
    chrome_options = setoptions()
    if proxies:
        PROXY = "46.4.73.88:2000"  # IP:PORT or HOST:PORT
        chrome_options.add_argument("--proxy-server=%s" % PROXY)
    chrome_path = ".\chromedriver.exe"
    chrome_options.binary_location = (
        "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
    )
    s = Service(r".\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=chrome_options)
    print(f"Chrome Driver Initalized.")
    return driver
