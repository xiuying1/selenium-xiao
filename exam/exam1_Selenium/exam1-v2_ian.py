from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse
from collections import Counter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def print_results_and_count_domains(browser):
    # Find all elements with class="c-container"
    results = browser.find_elements(By.CLASS_NAME, 'c-container')
    
    # Initialize a counter to count domains
    domain_counter = Counter()
    
    # Initialize a list to store results
    result_list = []
    result_list_real = []

    # Iterate through each result and print the title and link
    for result in results:
        title_element = result.find_element(By.XPATH, './/h3')
        link_element = result.find_element(By.XPATH, './/a')
        
        title = title_element.text
        link = link_element.get_attribute('href')
        result_list.append(f"{title}  --> {link}")
        
        # Parse the link to get the domain
        domain = urlparse(link).netloc
        domain_counter[domain] += 1

    # Print the result list
    print("结果列表")
    for item in result_list:
        print(item)
    
    # Print the result statistics
    print("\n结果统计")
    for domain, count in domain_counter.items():
        print(f"{domain}  --> {count}")
        
def search_and_print_results(browser, keyword):
    # Find the search box and enter the keyword
    search_box = browser.find_element(By.NAME, 'wd')
    search_box.clear()
    search_box.send_keys(keyword + Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    # Navigate to the second page of search results
    #second_page = browser.find_element(By.LINK_TEXT, '2')
    
    # Wait for the element to be present
    second_page = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, '2')))

    second_page.click()

    # Wait for the second page to load
    time.sleep(5)

    # Print the results on the second page
    print(f"Results for '{keyword}' on the second page:")
    print_results_and_count_domains(browser)

# List of keywords
keywords = ['Selenium']
# 'Xiaoxiuying', 'Selenium', 'Standard Chartered Bank'

# Initialize Chrome browser
browser = webdriver.Chrome()

# Open the website
browser.get('https://www.ianzhang.cn/bing/')

# Wait a few seconds to ensure the alert appears
time.sleep(5)

# Handle the alert
try:
    alert = Alert(browser)
    alert.accept()  # Accept the alert
    print("Alert handled")
except:
    print("No alert found")

# Iterate through each keyword and perform search and print results
for keyword in keywords:
    print(f"========='{keyword}'=============================")
    search_and_print_results(browser, keyword)

# Close the browser
browser.quit()
