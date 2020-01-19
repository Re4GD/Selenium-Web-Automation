# FIND UNREAD MAILS

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\cangu\Desktop\Coding\Python\Selenium\chromedriver.exe")

driver.get("https://webmail.bilkent.edu.tr/")
# driver.maximize_window()

driver.find_element_by_id("rcmloginuser").send_keys("your_bilkent_mail")
driver.find_element_by_xpath("/html/body/div/div[1]/form/table/tbody/tr[2]/td[2]/input").send_keys("password")
driver.find_element_by_id("rcmloginsubmit").click()

time.sleep(5)

mail_count = len(driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr"))
read_count, unread_count = 0, 0

current_page_num = 1

last_mail_el = driver.find_element_by_xpath("html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div/span[1]").text
last_mail_txt = last_mail_el.split(" ")
last_mail = last_mail_txt[5]
current_mail = last_mail_txt[3]

print("{} mails".format(last_mail))

while current_mail != last_mail:

    last_mail_el = driver.find_element_by_xpath("html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div/span[1]").text
    last_mail_txt = last_mail_el.split(" ")
    current_mail = last_mail_txt[3]

    mail_count = len(driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr"))
    read_count, unread_count = 0, 0

    for mail in range(1, mail_count + 1):

        element = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[1]/div[2]/table[2]/tbody/tr[" +
                                               str(mail) + "]/td[1]/span[3]/span")\

        if "unread" in element.get_attribute("class"):
            # print("unread")
            # element.click()
            unread_count += 1
        else:
            # print("read")
            read_count += 1

    print("Page {}, {} mails, {} read, {} unread".format(current_page_num, mail_count, read_count, unread_count))

    driver.find_element_by_id("pagejumper").clear()
    driver.find_element_by_id("pagejumper").send_keys(current_page_num + 1)
    time.sleep(2)
    driver.find_element_by_id("pagejumper").send_keys(Keys.RETURN)

    time.sleep(5)

    current_page_num += 1

print()
print("All mails analysed")

driver.quit()
