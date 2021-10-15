from selenium import webdriver
from bs4 import BeautifulSoup
import re
from datetime import date, timedelta, datetime

url = 'https://www.hoseasons.co.uk/lodges/canterbury-reach-lodge-retreat-canb'

def configure_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver

def extract_prices_from_page(year, soup,driver):

    booking_buttons = soup.select("td.ui-datepicker-same-month ui-datepicker-unselectable ui-state-disabled ")
    epic = driver.find_element_by_xpath("//a[@class='ui-state-default ui-state-hover']//div[1]//p[1]")
    print(epic)
    for btn in booking_buttons:
        date_str = next(iter(btn.select('span.date-square')))
        dte = datetime.strptime(f'{date_str} {year}', '%a %d %b %Y')

        price = driver.find_element_by_css_selector
        # this is where we save to database - using a reference to the price
        # monitor config, the current date, and the date and price for the
        # property
        print(price)
        print(date_str)


def first_of_next_month(dte):
    return (dte.replace(day=1) + timedelta(days=32)).replace(day=1)



def find_prices(url):

    driver = configure_driver()
    dte = date.today()
    while dte < (date.today() + timedelta(weeks=52)):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        extract_prices_from_page(dte.year, soup, driver)
        dte = first_of_next_month(dte)



find_prices(url)