""" This script is used to make custom auto-login-script for any site that has a username and password field"""
print("Get the chromedriver file if this one is not supported.")
name_of_file = input("Enter name of site: ")
name_of_file+="_AutoLogin.py"
username = input("Enter username for the site: ")
password = input("Enter password for the site: ")
loginpage=input("Enter login page URL: ")
elementID_Username=input("Enter ID for Username: ")
elementID_Password=input("Enter ID for Password: ")
elementID_Signin=input("Enter ID of Sign-in button: ")

data=f'''
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except Exception as e:
    import sys
    print("Selenium module not found")
    sys.exit()

usernameStr = '{username}'
passwordStr = '{password}'

browser = webdriver.Chrome()

browser.get(('{loginpage}'))


username = browser.find_element_by_id('{elementID_Username}')
username.send_keys(usernameStr)

password = browser.find_element_by_id('{elementID_Password}')
password.send_keys(passwordStr)


signInButton = browser.find_element_by_id('{elementID_Signin}')
signInButton.click()
'''

file = open(name_of_file,'w')
file.write(data)
file.close()