# %% - IMPORT LIBRARIES ------------------------
from selenium import webdriver

# %% - UPLOAD FILE -----------------------------
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("file:///D:/00_MASTER%20OF%20COMPUTER%20SCIENCE_MUM/00_Projects/12_Automation%20Testing_Basic/file_upload_page.html")


# -- Still use the send_keys method, but send the file instead of some text
driver.find_element_by_xpath("//*[@id='myFile']").send_keys("D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\uploadfile1.txt")

