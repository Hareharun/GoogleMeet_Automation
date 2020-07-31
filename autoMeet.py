from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

"""
BROWSERSTACK_URL = 'https://username:N3WrZgWLxkMDgJPmEq8Q@hub-cloud.browserstack.com/wd/hub'
desired_cap = {

    'os': 'Windows',
    'os_version': '10',
    'browser': 'Chrome',
    'browser_version': '80'

}
"""
#JS code to end call set your time
js='function endCall() \n' \
   '{\n' \
   '    document.getElementsByClassName("U26fgb JRY2Pb mUbCce kpROve GaONte Qwoy0d ZPasfd vzpHY")[0].click();\n' \
   '}\n' \
   'function forceMidnightPageReloadGetTargetTime(hour,minute) {\n' \
   'var t = new Date();\n' \
   '    t.setHours(hour);\n' \
   '    t.setMinutes(minute);\n' \
   '    t.setSeconds(0);\n' \
   '    t.setMilliseconds(0);\n' \
   '    return t;\n' \
   '}\n' \
   'var timetarget = forceMidnightPageReloadGetTargetTime("Enter Hours","Enter mins").getTime();\n' \
   'var timenow =  new Date().getTime();var offsetmilliseconds = timetarget - timenow;\n' \
   'setTimeout(function(){endCall();}, offsetmilliseconds);'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1,
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2
})
driver = webdriver.Chrome(executable_path=r'C:\Users\Hareharun\Desktop\chromedriver_win32\chromedriver.exe',options=chrome_options);
driver.get('https://accounts.google.com/signin')
#gmailid
driver.find_element_by_name("identifier").send_keys("Google Username")
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
driver.implicitly_wait(15)
#password
driver.find_element_by_name("password").send_keys("Google Password")
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()
driver.implicitly_wait(4)
#opening the google_meet
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
driver.implicitly_wait(4)
driver.get('https://meet.google.com/')
driver.implicitly_wait(10)
#Toggling to meetid
driver.find_element_by_xpath("//*[@id='page-content']/section[1]/div/div[1]/div[2]/div/div[2]/input").send_keys('Google Meet ID')
driver.implicitly_wait(4)
driver.find_element_by_xpath("//*[@id='page-content']/section[1]/div/div[1]/div[2]/div/div[2]/a/button/span").click()
driver.implicitly_wait(6)
driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
driver.implicitly_wait(4)
#Executes js code
driver.execute_script(js)



