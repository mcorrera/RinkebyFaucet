import datetime
import time

from selenium.webdriver.common.by import By

import seleniumsetup
import bs4 as BeautifulSoup
import settings
import prep


def RinkebyFaucet(accountAddress):
    url = "https://rinkebyfaucet.com/"
    html = prep.getpage(url)

    myxpath = "//div[@id='root']/div/div[2]/div[2]/div[2]/div/span/div/div/input"
    buttonxpath = (
        "//div[@id='root']/div/div[2]/div[2]/div[2]/div/span/div/div[2]/button/div/span"
    )
    settings.driver.find_element(By.XPATH, myxpath).send_keys(accountAddress)
    settings.driver.find_element(By.XPATH, buttonxpath).click()
    time.sleep(10)
    print("GetEth END")


def GetEth():
    lorenzoAccount = "0x8a15b70E91D6CAea474A112502118E4a87C91fbc"
    marcAccount = "0x9c2Ce4FE3e8ABd5E5241227D5C8ad15aBC3546Ac"
    RinkebyFaucet(lorenzoAccount)
    RinkebyFaucet(marcAccount)


if __name__ == "__main__":
    driver = seleniumsetup.initUCdriver(False)
    # driver = seleniumsetup.initchromedriver(False)
    settings.init(driver)
    GetEth()
    settings.end()
