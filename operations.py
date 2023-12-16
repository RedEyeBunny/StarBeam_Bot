import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.firefox.options import Options

credentials = {"Member_Type": "", "En_Ro": "", "Date_of_Birth": "", "PassWord": ""}

options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox()
lframe = "html > frameset:nth-child(2) > frameset:nth-child(2) > frame:nth-child(1)"
rframe = "html > frameset:nth-child(2) > frameset:nth-child(2) > frame:nth-child(2)"
tframe = "html > frameset:nth-child(2) > frame:nth-child(1)"
def login() -> None:
    driver.get("https://webkiosk.juet.ac.in/")
    Select(driver.find_element(By.ID, "UserType")).select_by_index(0)
    driver.find_element(By.ID, "MemberCode").send_keys("Enrollment_Number")
    driver.find_element(By.ID, "DATE1").send_keys("dd-mm-yyyy")
    driver.find_element(By.ID, "Password").send_keys("password")
    driver.find_element(By.ID, "txtcap").send_keys(driver.find_element(By.CLASS_NAME, "noselect").text)
    driver.find_element(By.ID, "BTNSubmit").click()


def attendance() -> None:
    left_frame = driver.find_element(By.CSS_SELECTOR,lframe)
    driver.switch_to.frame(left_frame)

    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/div/div[4]").click()
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/div/span[4]/a[1]").click()
    driver.switch_to.default_content()
    right_frame = driver.find_element(By.CSS_SELECTOR,rframe)

    driver.switch_to.frame(right_frame)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "table-1")))
    table = driver.find_element(By.CLASS_NAME, "sort-table")
    table.screenshot("attendance.png")
    driver.switch_to.default_content()

def subject_faculty() -> None:

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,lframe))

    try:
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/div/span[4]/a[3]").click()
    except (NoSuchElementException,ElementNotInteractableException):
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/div/div[4]").click()
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/div/span[4]/a[3]").click()

    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,rframe))
    try:
        driver.find_element(By.CSS_SELECTOR,"#table-1").screenshot("faculty_info.png")
    except NoSuchElementException:
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#table-1").screenshot("faculty_info.png")
    driver.switch_to.default_content()

def exam_marks() -> None:
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,lframe))
    try:
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/div/span[5]/a[2]").click()
    except (NoSuchElementException,ElementNotInteractableException):
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/div/div[5]").click()
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/div/span[5]/a[2]").click()

    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,rframe))
    time.sleep(1)
    Select(driver.find_element(By.CSS_SELECTOR, "#exam")).select_by_index(1)
    driver.find_element(By.XPATH,"/html/body/form/table[2]/tbody/tr[2]/td/input").click()
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#table-1")))
    driver.find_element(By.CSS_SELECTOR,"#table-1").screenshot("exam_marks.png")
    driver.switch_to.default_content()

def view_cgpa() -> None:
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,lframe))
    try :
        driver.find_element(By.CSS_SELECTOR,"#sub5 > a:nth-child(8)").click()
    except (NoSuchElementException,ElementNotInteractableException):
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[3]/td/div/div[5]").click()
        driver.find_element(By.CSS_SELECTOR,"#sub5 > a:nth-child(8)").click()
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, rframe))
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#table-1")))
    driver.find_element(By.CSS_SELECTOR,"#table-1").screenshot("cgpa_table.png")
    driver.switch_to.default_content()

def logout():
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR,tframe))
    driver.find_element(By.LINK_TEXT,"Signout").click()
    driver.close()
