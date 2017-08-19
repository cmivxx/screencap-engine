import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")


driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])
driver.set_window_size(1280, 1024)
driver.get('https://www.chrisrmiller.com')
time.sleep(2)
# driver.execute_script('document.getElementsByClassName("mp")[0].style.background = "green"')
# driver.execute_script('document.body.style.background = "black"')
driver.save_screenshot('cmivxx-1.png')

driver.get('https://resume.chrisrmiller.com')
time.sleep(2)
# driver.execute_script("var body = document.getElementsByTagName('body')[0]; body.setAttribute('background-color', 'white')")
# driver.execute_script('document.body.style.background = "black"')
driver.save_screenshot('resume.png')