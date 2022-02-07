from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path = r"C:\Users\hoang\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")
time.sleep(5)

login = driver.find_element(By.XPATH, "//span[text()='Log in']")
login.click()

time.sleep(5)
facebook = driver.find_element(By.XPATH,'//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()
time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
#print(driver.title)
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys("ngantestingemail@gmail.com")
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys("Hkn12008631")
login_fb = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
login_fb.click()
#next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
#next.click()
#time.sleep(5)
#password = driver.find_element(By.XPATH, '//*[@id="pass"]')
#password.send_keys("Hkn12008631")

time.sleep(5)
#Switch back to Tinder window
driver.switch_to.window(base_window)
time.sleep(5)
location_popup = driver.find_element(By.XPATH,'//*[@id="q-315288401"]/div/div/div/div/div[3]/button[1]/span')
location_popup.click()
time.sleep(5)
notification_enable = driver.find_element(By.XPATH,'//*[@id="q-315288401"]/div/div/div/div/div[3]/button[1]/span')
notification_enable.click()
time.sleep(5)
accept_cookie =  driver.find_element(By.XPATH,'//*[@id="q1413092675"]/div/div[2]/div/div/div[1]/button')
accept_cookie.click()
time.sleep(5)
for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)
driver.quit()