from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import datetime
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Use WebDriver Manager to automatically manage ChromeDriver
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
@given('I open the enterprise resumption application page')
def step_impl(context):
    browser.get('https://jinshuju.net/templates/detail/Dv9JPD')

# Select the unit situation
@when('I select "连续生产/开工类企事业单位" in the "请选择贵单位情况" option group')
def step_impl(context):
    option = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@value="连续生产/开工类企事业单位"]'))
    )
    option.click()

# Take a screenshot of the first page
@when('I take a screenshot of the first page')
def step_impl(context):
    time.sleep(5)  
    browser.save_screenshot('first_page.png')

# Click the next page button
@when('I click the next page button')
def step_impl(context):
    next_button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="下一页"]'))
    )
    next_button.click()

# Take a screenshot of the second page
@when('I take a screenshot of the second page')
def step_impl(context):
    time.sleep(5) 
    browser.save_screenshot('second_page.png')

# Fill in the details on the second page
@when('I fill in the following details on the second page')
def step_impl(context):
    # Get the New Year's Day date of the current year
    new_year_date = datetime.date(datetime.datetime.now().year, 1, 1).strftime('%Y-%m-%d')
    
    application_date = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, 'application_date'))
    )
    application_date.send_keys(new_year_date)
    
    applicant = browser.find_element(By.NAME, '申请人')
    applicant.send_keys('自动化')
    
    contact = browser.find_element(By.NAME, '联系方式')
    contact.send_keys('1388888888')

# Click the next page button again
@when('I click the next page button again')
def step_impl(context):
    next_button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="下一页"]'))
    )
    next_button.click()

# Take a screenshot of the third page
@when('I take a screenshot of the third page')
def step_impl(context):
    time.sleep(5)  
    browser.save_screenshot('third_page.png')

# Fill in the details on the third page
@when('I fill in the following details on the third page')
def step_impl(context):
    # Get the current date
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    reporting_unit = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.NAME, '报备单位'))
    )
    reporting_unit.send_keys('测试公司')
    
    on_duty_number = browser.find_element(By.NAME, '在岗人数')
    on_duty_number.send_keys('99')
    
    reporting_date = browser.find_element(By.NAME, '报备日期')
    reporting_date.send_keys(current_date)
    
    hubei_related = browser.find_element(By.NAME, '湖北籍员工、前往湖北以及与湖北人员密切接触的员工（人数）')
    hubei_related.send_keys('0')
    
    unit_leader = browser.find_element(By.NAME, '单位负责人')
    unit_leader.send_keys('您的姓名')
    
    contact_number = browser.find_element(By.NAME, '联系方式')
    contact_number.send_keys('13888888888')
    
    prevention_plan = browser.find_element(By.NAME, '疫情防控方案')
    prevention_plan.send_keys('测试内容')

# Take a screenshot of the third page again
@when('I take a screenshot of the third page again')
def step_impl(context):
    time.sleep(5)  
    browser.save_screenshot('third_page_filled.png')

# Click the submit button
@when('I click the submit button')
def step_impl(context):
    submit_button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="提交"]'))
    )
    submit_button.click()

# Verify submission success and take a screenshot
@then('the form should be submitted successfully and take a screenshot of the result page')
def step_impl(context):
    success_message = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "提交成功")]'))
    )
    assert success_message is not None
    browser.save_screenshot('submission_result.png')

# Generate HTML test report
def generate_html_report():
    html_content = """
    <html>
    <head>
        <title>测试报告</title>
    </head>
    <body>
        <h1>测试报告</h1>
        <h2>First Page</h2>
        <img src="first_page.png" alt="First Page Screenshot">
        <h2>Second Page</h2>
        <img src="second_page.png" alt="Second Page Screenshot">
        <h2>Third Page</h2>
        <img src="third_page.png" alt="Third Page Screenshot">
        <h2>Third Page Filled</h2>
        <img src="third_page_filled.png" alt="Third Page Filled Screenshot">
        <h2>Submission Result</h2>
        <img src="submission_result.png" alt="Submission Result Screenshot">
    </body>
    </html>
    """
    with open("test_report.html", "w", encoding="utf-8") as file:
        file.write(html_content)

# Close the browser and generate the report
def after_all(context):
    browser.quit()
    generate_html_report()
