# %% - APPROACH 1
from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://hopamchuan.com/")

# -- using "save_screenshot()" will allow to save screenshot as any format (jpg, jpeg, png, etc)
driver.save_screenshot("D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\screenshot1.jpg") 

# %% - APPROACH 2
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://hopamchuan.com/")

# -- using "get_screenshot_as_file()" 
driver.get_screenshot_as_file("D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\screenshot2.jpg")


# %%
