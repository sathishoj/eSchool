import time

import xlrd
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver\chromedriver.exe")
driver.maximize_window()
print("Window Maximized")
driver.get("https://eschool.gleamly.com/login")
print("URL Opened")
time.sleep(5)
Email = driver.find_element_by_xpath("//div/input[@formcontrolname='email']")
Password = driver.find_element_by_xpath("//div/input[@formcontrolname='password']")
Login = driver.find_element_by_xpath("//button[@class='mat-focus-indicator SignIn mt-3 mat-button mat-button-base']")

workbook = xlrd.open_workbook("eSchoolLogin.xls")
sheet = workbook.sheet_by_name("Login")

for curr_row in range(1,2):
    email = sheet.cell_value(curr_row,0)
    password = sheet.cell_value(curr_row,1)

    Email.send_keys(email)
    Password.send_keys(password)
    Login.click()

time.sleep(8)

if driver.current_url == "https://eschool.gleamly.com/admin-dashboard":
    print("Login successful")
else:
    print("Username or Password wrong")
time.sleep(3)

Logout = driver.find_element_by_xpath("//div/button[@class='btn btn-secondary dropdown-toggle']").click()
Logout1 = driver.find_element_by_xpath("//div/app-logout-button/a[@class='dropdown-item']").click()
time.sleep(3)

if driver.current_url == "https://eschool.gleamly.com/login":
    print("Logout successful")
else:
    print("Logout Fail")

time.sleep(3)
driver.close()