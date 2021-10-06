from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os


    
channel_id =    'Your channel ID' #INSERT ID YOUTUBE
channel_pass =  'Your channel Password' #INSERT PASS YOUTUBE
user_data_dir = 'C:\\chrome-dev-profile'
delay_action = 6 #delay for action
delay_popup = 30 #delay for get stats

script_folder = os.path.dirname(__file__)
driver_folder = os.path.join(script_folder,'chromedriver.exe')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

option = Options()


option.add_argument("--user-data-dir={}".format(user_data_dir))
option.add_argument('--profile-directory=Default')
option.add_experimental_option("prefs", 
{"profile.default_content_setting_values.notifications": 2 
 }) 
option.headless = True # FALSE = SHOW ACTION IN CHROME
driver = webdriver.Chrome(driver_folder, options=option)
url_sub = 'https://www.subpals.com/login/final/{}/'.format(channel_id)
driver.get(url=url_sub)

driver.implicitly_wait(10)
# storing the current window handle to get back to dashbord 
main_page = driver.current_window_handle 
driver.find_element(By.NAME, 'channelid').send_keys(channel_id)  # channel id
driver.find_element_by_name('password').send_keys(channel_pass)  # Channel password
driver.find_element_by_xpath("//button[@type='submit']").click() # SUMBMIT
print("[+]Logged to SubPals.[+]")

try:
    activate = driver.find_element_by_xpath('/html/body/div/center[2]/div/div[1]/div[2]/form/div/a')  # activate plan
    driver.execute_script("arguments[0].click();", activate)
except:
    print("[+]Plan is already activated.[+]")

time.sleep(delay_action)
try:
    left_videos = int(driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div/div[2]/div[1]/h2/span/div').text)
except:
    print("[X]You already used the program in the last 12 hours.[X]")
    quit()
while left_videos:
    left_videos = int(driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div/div[2]/div[1]/h2/span/div').text)
    try:
        driver.execute_script("arguments[0].click();",WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/a'))))
    except NoSuchElementException:
        pass
        quit()
    for handle in driver.window_handles: 
        if handle != main_page: 
            yt_page = handle 
    try:
        driver.switch_to.window(yt_page)
        print("[.] Changing Page [.]")
    except:
        print("[X]Popup not found[X]")
        quit()
    # Sub:
    print("[.] Subscribing [.]")
    try:
        driver.execute_script("arguments[0].click();",WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='confirm-button']/a"))))
    except NoSuchElementException:
        pass
        quit()
    time.sleep(delay_action)
    driver.implicitly_wait(2)
    print("[.] Changing Page [.]")
    driver.switch_to.window(main_page)
    print("[.] Clicking continue...Wait! [.]")
    try:
        driver.execute_script("arguments[0].click();",WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/div/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[3]/a'))))
    except NoSuchElementException:
        pass
        quit()
    time.sleep(delay_action)
    try:
        left_videos = int(driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div/div/div/div[2]/div[1]/h2/span/div').text)
        print("[===========================================]")
        print("[...]Continuing cycle[...]")
    except:
        print("[===========================================]")
        print("No more videos left on SubPals.")
        print("[===========================================]")
        break
    print(f'[+] Next video [+]')
quit()
