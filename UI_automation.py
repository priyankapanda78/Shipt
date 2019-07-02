
#### UI Automation of Feature - StoreView based on zip code



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os
import sys

if(len(sys.argv) < 2):
    print("Please pass chrome driver location.")

chromedriver = sys.argv[1] # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver
url = "https://www.shipt.com"
driver = webdriver.Chrome(chromedriver)
driver.get(url)


#Login button on homepage
login=driver.find_element_by_xpath('//a[contains(@href, "https://shop.shipt.com/#/app/home") and @class="button-secondary"]')
login.click()
time.sleep(2)

#Input for username and password is given
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("priyanka.panda78@gmail.com")
password.send_keys("testuser123")
time.sleep(2)

#Click on Login Button
driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
time.sleep(2)

#Click on StoreView button
driver.find_element_by_xpath("//button[@data-test='ShoppingStoreSelect-storeView']").click()
time.sleep(3)

#validating there are more than 0 stores for the selected address
stores = driver.find_elements_by_xpath("//div[@data-test='ChooseStore-store']")
print (len(stores))
assert (len(stores) > 0)
time.sleep(2)

#Store is selected
stores[len(stores)-1].click()
time.sleep(3)

#Validating the items are displayed "On Sale" section
items = driver.find_elements_by_xpath("//section[@id='shelfIndex-0-On Sale']//li")
print (len(items))
assert (len(items) > 0)
time.sleep(2)

#Click on the Store select button and choose a different address from dropdown
driver.find_element_by_xpath("//button[@data-test='ShoppingStoreSelect-storeView']").click()
driver.find_element_by_id("SelectAddress-select-selected-option-label").click()
time.sleep(2)

#Clicked on a saved address from the dropdown
driver.find_element_by_id("dropdown_option_1").click()
time.sleep(3)

#Total number of stores are displayed and are more than 0 in count
stores = driver.find_elements_by_xpath("//div[@data-test='ChooseStore-store']")
print (len(stores))
assert (len(stores) > 0)
time.sleep(2)

#Store is selected
stores[len(stores)-1].click()
time.sleep(3)

#Validating the items are displayed "On Sale" section
items = driver.find_elements_by_xpath("//section[@id='shelfIndex-0-On Sale']//li")
print (len(items))
assert (len(items) > 0)
time.sleep(2)

#Click on the Addresses button
driver.find_element_by_xpath("//a[@href='/account/addresses']").click()
time.sleep(2)

#Click on Add Address button
driver.find_element_by_xpath("//button[contains(text(),'Add Address')]").click()
time.sleep(2)

#Input given for Address autocomplete
address = driver.find_element_by_id("AddressForm-autocomplete")
address.send_keys("203 Parkcrest Way, Riverton, WY 82501")

#Input for the street field
street = driver.find_element_by_id("adr-street1")
street.send_keys("203 Parkcrest Way")

#Input for the city field
city = driver.find_element_by_id("adr-city")
city.send_keys("Riverton")

#Input for the state field
state = driver.find_element_by_id("adr-state")
state.send_keys("WY")

#Input for the zipcode field
zipcode = driver.find_element_by_id("adr-zip")
zipcode.send_keys("82501")

#Click on the submit button
driver.find_element_by_xpath("//button[@data-test='AddressForm-submit-button']").click()
time.sleep(3)

#Capturing the error message
error = driver.find_element_by_xpath("//div[contains(@class, 'AddressForm-zipCodeWrapper')]//span[@data-test='Input-error']")
print(error.text)

#Validating the error message
assert error.text == 'Zip code not in service area'


