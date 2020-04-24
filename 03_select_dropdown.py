# %% -- IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# %%
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.implicitly_wait(2)

# -- Select the drop down button
element = driver.find_element_by_id("RESULT_RadioButton-9") 
dropdown = Select(element)

# -- Select by text
dropdown.select_by_visible_text("Morning")
driver.implicitly_wait(2)

# -- Select by Index
dropdown.select_by_index(1)
driver.implicitly_wait(2)

# -- Select by box value
dropdown.select_by_value("Radio-2")
driver.implicitly_wait(2)

# -- Count number of Options
print("Dropdown options: ", len(dropdown.options))

# -- Print out all Options
listOptions = dropdown.options

for o in listOptions:
    print(o.text)

# %%
