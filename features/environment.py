from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    context.browser = webdriver.Firefox()
    # driver.implicitly_wait(10) # 隱性等待，全域影響，最長只等10秒
    context.browser.get("https://www.twitch.tv/")
    context.wait = WebDriverWait(context.browser, 10)
    
def after_all(context):
    context.browser.quit()