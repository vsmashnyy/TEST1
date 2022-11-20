from selenium import webdriver
import time

url = "https://jobs.dou.ua/companies/transferroom/"
driver = webdriver.Chrome()

try:
    driver.get(url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
