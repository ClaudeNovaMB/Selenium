from selenium import webdriver
from selenium.webdriver.support import select
import time


driver = webdriver.Chrome(executable_path=r"PATH_TO_YOUR_WEBDRIVER") 
time.sleep(2)
driver.maximize_window()


def quote_data():

    driver.get("https://public.bitmex.com/?prefix=data/quote/")
    time.sleep(3)
    elem1 = driver.find_element_by_id('listing')
    items_in_elem1 = elem1.find_elements_by_tag_name('a')
    skip = [1001,2002] # Skips the page breaks
    counter = 0
    for item in items_in_elem1[1:]:
        counter +=1
        if counter not in skip:
            item.click()
            time.sleep(0.5) # Depends on your internet speed. You can leave it or change it
        else:
            pass
                  
 
def trade_data():

    driver.get("https://public.bitmex.com/?prefix=data/trade/")
    time.sleep(3)
    elem2 = driver.find_element_by_id('listing')
    items_in_elem1 = elem2.find_elements_by_tag_name('a')
    skip = [1001,2002] # Skips the page breaks
    counter = 0
    for item in items_in_elem2[1:]:
        counter +=1
        if counter not in skip:
            item.click()
            time.sleep(0.5) # Depends on your internet speed. You can leave it or change it
        else:
            pass       
    
if __name__ == '__main__':
    quote_data()
    trade_data()