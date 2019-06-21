import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestSearch(object):
    @pytest.fixture(scope="class")
    def firefox_driver(cls):
        driver = webdriver.Firefox()
        # driver.implicitly_wait(10) # 隱性等待，全域影響，最長只等10秒
        driver.get("https://www.twitch.tv/")
        global wait
        wait = WebDriverWait(driver, 10)
        yield driver

        driver.quit()

    def searchKeyword(self, keyword):
        """ 搜尋指定關鍵字 """
        searchBar_XPath = "//input[@type='search']"
        searchResultPanel_XPath = "//div[@class='tw-border-b tw-border-l tw-border-r tw-border-radius-medium tw-border-t tw-c-background-base tw-c-text-inherit tw-elevation-1']"
        searchBar = wait.until(EC.visibility_of_element_located((By.XPATH, searchBar_XPath)))
        searchBar.clear()
        searchBar.send_keys(keyword)
        wait.until(EC.visibility_of_element_located((By.XPATH, searchResultPanel_XPath)))

    """
    場景1: 搜尋實況主
    Given 使用者進入網站
    When 搜尋實況主名稱
    Then 實況主的第一筆結果應與搜尋符合
    """
    def test_streamer(self, firefox_driver):
        tsetStreamerName = "餐餐自由配"
        self.searchKeyword(tsetStreamerName)
        firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
        streamerName = wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
        assert tsetStreamerName in streamerName

    """
    場景2: 搜尋實況分類
    Given 使用者進入網站
    When 搜尋實況分類名稱
    Then 實況分類的第一筆結果應與搜尋符合
    """
    def test_category(self, firefox_driver):
        tsetCategoryName = "Just Chatting"
        self.searchKeyword(tsetCategoryName)
        firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
        categoryName = wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
        assert tsetCategoryName in categoryName

    """
    場景3: 搜尋標籤
    Given 使用者進入網站
    When 搜尋標籤名稱
    Then 第一筆結果應含有搜尋的標籤
    """
    def test_tag(self, firefox_driver):
        tsetTagName = "中文"
        self.searchKeyword(tsetTagName)
        firstResultTag_XPath = "//div[@class='tw-align-items-center tw-flex tw-tag__content']"
        tagName = wait.until(EC.visibility_of_element_located((By.XPATH, firstResultTag_XPath))).text
        assert tsetTagName == tagName

    """
    場景4: 搜尋錯誤(無結果)的關鍵字
    Given 使用者進入網站
    When 搜尋錯誤的關鍵字
    Then 搜尋的結果應與關鍵字不符合
    """
    def test_wrongKeyword(self, firefox_driver):
        wrongKeyword = "unirook"
        self.searchKeyword(wrongKeyword)
        firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
        resultText = wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
        assert wrongKeyword not in resultText