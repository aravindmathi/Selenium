import os
from os import strerror
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import sys
text = "Please ignore the message. Whatsapp testing"
driver = webdriver.Chrome("C:\\Users\\learngcp451\\Downloads\\chromedriver.exe")
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")
try:
    with open(os.path.join(os.getcwd(),'contacts.txt')) as f:
        for line in f:            
            contact=line.rstrip()            
            try:
                inp_xpath_search = "//input[@title='Search or start new chat']"
                input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
                input_box_search.click()
                time.sleep(2)
                input_box_search.send_keys(contact)
                time.sleep(2)
                selected_contact = driver.find_element_by_xpath('//span[@title ="{}"]'.format(contact))
                selected_contact.click()
                inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
                input_box = driver.find_element_by_xpath(inp_xpath)
                time.sleep(2)
                input_box.send_keys(text + Keys.ENTER)
                print("Sent Successfully: ",contact)
                with open(os.path.join(os.getcwd(),'Success.txt'),'a') as s:
                    s.write('\n['+str(datetime.now())+']:'+"Successfully sent to "+str(contact))
                time.sleep(2)
            except:
                print("Failed Miserably: ",contact)                
                inp_xpath_cancel = "//button[@class='_2heX1']"      
                
                input_box_cancel = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_cancel))
                input_box_cancel.click()
                with open(os.path.join(os.getcwd(),'error.txt'),'a') as w:
                    w.write('\n['+str(datetime.now())+']:'+' Possibly Contact or group does not exist:'+str(contact)+' Error: {}'.format(sys.exc_info()[0]))
                time.sleep(2)
        driver.quit()            
                
            
except Exception as exc:
    with open(os.path.join(os.getcwd(),'error.txt'),'a') as w:
        w.write('\n['+str(datetime.now())+']:'+str(strerror(exc.errno)))
        print("Check error.txt")

    

