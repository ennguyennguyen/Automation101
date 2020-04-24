# %% -- IMPORT LIBRARIES
from selenium import webdriver

# %% -- Body
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://hopamchuan.com/")

driver.maximize_window()

# -- Scroll to a number of pixel by running the JS script named "window.scrollBy" with the end pixel at 1000
# driver.execute_script("window.scrollBy(0,1000)", "")

# -- Scroll to a identified element using the arguments[0].scrollIntoView();
# element = driver.find_element_by_xpath("//*[@id='hot-today']/div[29]/div[1]/div/a")
# driver.execute_script("arguments[0].scrollIntoView();", element)

# -- Scroll to the end of page using window.scrollBy(0, document.body.scrollHeight)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")


