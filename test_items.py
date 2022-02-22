import time
from selenium.common.exceptions import NoSuchElementException 
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def check_exists_css_selector(browser,css_selector):
    try:
        browser.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True
def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    assert check_exists_css_selector(browser,".btn-add-to-basket"), "Сart button not found!"
   
