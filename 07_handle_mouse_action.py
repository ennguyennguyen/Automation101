# %% - IMPORT LIBRARIES ------------------------
from selenium import webdriver
from selenium.webdriver import ActionChains

# %% - MOUSE HOVER ----------------------------
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

adminPanel = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
userMgmt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

# -- In order to simulate the mouse, we need to create a ActionChain and then move to each elements, finish with the .perform() method
actions = ActionChains(driver)
actions.move_to_element(adminPanel).move_to_element(userMgmt).move_to_element(users).click().perform()

# %% - RIGHT CLICK -------------------------
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

# -- Using the context_click().perform() for the right click
actions = ActionChains(driver)
actions.context_click(button).perform()

# %% - DRAG AND DROP ------------------------
driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_button = driver.find_element_by_xpath("//*[@id='box3']")
dest_button = driver.find_element_by_xpath("//*[@id='box103']")

actions = ActionChains(driver)
actions.drag_and_drop(source_button, dest_button).perform()


