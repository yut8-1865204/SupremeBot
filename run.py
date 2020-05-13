from selenium import webdriver
import time


name = "Angel Yu"
email = "yut8@uw.edu"
tel = "1234567890"
address ="111 street"
zip = "98105"
city = "Seattle"
state = "WA"
country = "USA"


chromedriver_location = "chromedriver_mac64.zip"

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

add_to_cart_button = '//*[@id="add-remove-button"]/input'
driver.find_element_by_xpath(checkout_button).click()

time.sleep(2)

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)


print("Web Driver Run")
