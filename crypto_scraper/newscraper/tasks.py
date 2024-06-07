# newscraper/tasks.py

from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@shared_task
def scrape_crypto_data(coins):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)
    
    data = {}
    for coin in coins:
        url = f'https://coinmarketcap.com/currencies/{coin}/'
        driver.get(url)
        
        try:
            # Example: Modify the scraping logic according to the actual HTML structure of the page
            price = driver.find_element_by_class_name('priceValue').text
            data[coin] = price
        except Exception as e:
            data[coin] = f"Error: {str(e)}"
    
    driver.quit()
    
    return data
