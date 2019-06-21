import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class searchTestUnitTest(unittest.TestCase):  
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(10) # 隱性等待，全域影響，最長只等10秒
        self.driver.get("https://www.twitch.tv/")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def searchKeyword(self, keyword):
        """ 搜尋指定關鍵字 """
        searchBar_XPath = "//input[@type='search']"
        searchResultPanel_XPath = "//div[@class='tw-border-b tw-border-l tw-border-r tw-border-radius-medium tw-border-t tw-c-background-base tw-c-text-inherit tw-elevation-1']"
        searchBar = self.wait.until(EC.visibility_of_element_located((By.XPATH, searchBar_XPath)))
        searchBar.clear()
        searchBar.send_keys(keyword)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, searchResultPanel_XPath)))

    """
    場景1: 搜尋實況主
    Given 使用者進入網站
    When 搜尋實況主名稱
    Then 實況主的第一筆結果應與搜尋符合
    """
    def test_streamer(self):
        tsetStreamerName = "餐餐自由配"
        self.searchKeyword(tsetStreamerName)
        firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
        streamerName = self.wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
        self.assertIn(tsetStreamerName, streamerName)

    """
    場景2: 搜尋實況分類
    Given 使用者進入網站
    When 搜尋實況分類名稱
    Then 實況分類的第一筆結果應與搜尋符合
    """
    def test_category(self):
        tsetCategoryName = "Just Chatting"
        self.searchKeyword(tsetCategoryName)
        firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
        categoryName = self.wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
        self.assertIn(tsetCategoryName, categoryName)

    """
    場景3: 搜尋標籤
    Given 使用者進入網站
    When 搜尋標籤名稱
    Then 第一筆結果應含有搜尋的標籤
    """
    def test_tag(self):
        tsetTagName = "中文"
        self.searchKeyword(tsetTagName)
        firstResultTag_XPath = "//div[@class='tw-align-items-center tw-flex tw-tag__content']"
        tagName = self.wait.until(EC.visibility_of_element_located((By.XPATH, firstResultTag_XPath))).text
        self.assertEqual(tsetTagName, tagName)

    """
    場景4: 搜尋錯誤(無結果)的關鍵字
    Given 使用者進入網站
    When 搜尋錯誤的關鍵字
    Then 搜尋的結果應與關鍵字不符合
    """
    def test_wrongKeyword(self):
        wrongKeyword = "unirook"
        self.searchKeyword(wrongKeyword)
        firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
        resultText = self.wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
        self.assertNotIn(wrongKeyword, resultText)

if __name__ == '__main__':
    unittest.main()