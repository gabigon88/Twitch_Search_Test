from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('I key {keyword} in search bar')
def step_impl(context, keyword):
    searchBar_XPath = "//input[@type='search']"
    searchBar = context.wait.until(EC.visibility_of_element_located((By.XPATH, searchBar_XPath)))
    searchBar.clear()
    searchBar.send_keys(keyword)
    context.keyword = keyword

@when('I search the keyword')
def step_impl(context):
    searchResultPanel_XPath = "//div[@class='tw-border-b tw-border-l tw-border-r tw-border-radius-medium tw-border-t tw-c-background-base tw-c-text-inherit tw-elevation-1']"
    context.wait.until(EC.visibility_of_element_located((By.XPATH, searchResultPanel_XPath)))

@then('the first result should be matched')
def step_impl(context):
    firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
    firstResultText = context.wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
    assert context.keyword in firstResultText

@then('the tag of first result should be matched')
def step_impl(context):
    firstResultTag_XPath = "//div[@class='tw-align-items-center tw-flex tw-tag__content']"
    firstResultTag = context.wait.until(EC.visibility_of_element_located((By.XPATH, firstResultTag_XPath))).text
    assert context.keyword == firstResultTag

@then('the first result should not be matched')
def step_impl(context):
    firstResult_XPath = "//div[@class='tw-align-items-center tw-flex tw-flex-nowrap tw-flex-row']"
    firstResultText = context.wait.until(EC.visibility_of_element_located((By.XPATH, firstResult_XPath))).text
    assert context.keyword not in firstResultText
