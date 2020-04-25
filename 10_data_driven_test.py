# %% -- IMPORT LIBRARIES
from selenium import webdriver
import XLUtilities

# %% -- TEST CASES
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

# -- define the path to data file
path = "D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\DataDriven_LoginCredentials.xlsx"

# -- count the rows
rows = XLUtilities.countRow(path, "Sheet1")
print(rows)

# -- iterate through each rows, get the value of username and password and perform test
for r in range(2, rows+1):
    username = XLUtilities.readFile(path, "Sheet1", r, 1)
    password = XLUtilities.readFile(path, "Sheet1", r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    if(driver.title == "Find a Flight: Mercury Tours:"):
        print("test passed")
        XLUtilities.writeFile(path, "Sheet1", r, 3, "test passed")
    else:
        print("test failed")
        XLUtilities.writeFile(path, "Sheet1", r, 3, "test failed")

    driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a").click()



# %%
