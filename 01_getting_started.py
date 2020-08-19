# %% Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

# %% 1> BASIC COMMANDS

# --Initial web browser
#driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

# -- open website
driver.get("https://hopamchuan.com/")

# -- Automation test code in here
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='login-link']").click()

time.sleep(5)

# -- close website
# ---- using close() will close the current browser
driver.close()

# ---- using quit() will close ALL browser
# driver.quit()

# %% 2> NAVIGATION BACK & FORWARD
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://hopamchuan.com/")
print("title: ", driver.title)
time.sleep(5)  # NOTE: need to leave a sleep time in order for the web to load

driver.find_element_by_xpath("//*[@id='login-link']").click()
print("after click Login: ", driver.title)
time.sleep(5)

driver.back()
print("after click back: ", driver.title)
time.sleep(5)

driver.forward()
print("after click forward: ", driver.title)
time.sleep(5)

driver.close()

# %% 3> USING is_selected(), is_displayed(), is_enabled()
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

username = driver.find_element_by_name("userName")
print("username field: ", username)
print("username is enabled: ", username.is_displayed())
print("username is enabled: ", username.is_enabled())

password = driver.find_element_by_name("password")
print("password field: ", password)
print("username is enabled: ", password.is_displayed())
print("password is enabled: ", password.is_enabled())

username.send_keys("mercury")
password.send_keys("mercury")

driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_elements_by_css_selector("input[value=roundtrip]")
print(roundtrip_radio.is_selected())

onetrip_radio = driver.find_elements_by_css_selector("input[value=oneway]")
print(onetrip_radio.is_selected())

driver.close()