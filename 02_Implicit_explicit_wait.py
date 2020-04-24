# %% -- IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# %% 4> IMPLICIT WAIT ===================
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.implicitly_wait(10)

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()

driver.close()

# %% 5> EXPLICIT WAIT ==================
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")

# -- Open website
driver.get("https://www.expedia.com/")
driver.implicitly_wait(3)

# -- click on Flight button
driver.find_element(By.ID, "tab-flight-tab-hp").click()
time.sleep(5) # python function

# -- fill in all the information
# ---- Departure
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
time.sleep(3)

# ---- Destination
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
time.sleep(3)

# ---- Flight Date
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/10/2020")
time.sleep(3)

# ---- Flight Return
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("01/30/2021")
time.sleep(5)

# ---- Hit Search button
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

# -- Explicit wait statement
wait = WebDriverWait(driver, 10)
waitElement = wait.until(EC.element_to_be_clickable(By.XPATH, "//*[@id='stopFilter_stops-0']"))
waitElement.click()

# -- Close browser
time.sleep(3)
driver.close()

# %%
