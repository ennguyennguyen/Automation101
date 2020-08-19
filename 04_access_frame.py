# %% -- IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager

# %% -- TEST CASES
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.selenium.dev/selenium/docs/api/java/")
time.sleep(3)

# -- Access the 1st frame -> click on an element of the frame
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

# -- Need to go back to the parent frame
# -- Using switch_to and pass in the default_content()
driver.switch_to.default_content()

# -- Access the 2nd frame -> click on an element of the frame
driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

# -- return to parents frame
# -- Using switch_to and pass in the default_content()
driver.switch_to.default_content()

# -- Access the 3rd frame
driver.switch_to_frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[2]").click()
time.sleep(3)

# -- close the browser
driver.close()


# %%
