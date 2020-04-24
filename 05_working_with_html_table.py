# %% -- IMPORT LIBRARIES
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# %% -- TEST CASES
# NOTE: find_elements_by_xpath (element with "s") will have the len() method
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")

driver.get("file:///D:/00_MASTER%20OF%20COMPUTER%20SCIENCE_MUM/00_Projects/12_Automation%20Testing_Basic/table1.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("Number of rows: ", rows)
print("Number of cols: ", cols)

print("FName"+"    "+"LName"+"    "+"Age")

for row in range(2, rows+1):
    for col in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(value, end = "    ")
    print()

driver.close()
# %%
