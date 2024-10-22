from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()

# Initialize the WebDriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Open the desired website
driver.get("https://forms.gle/biVo1ZBx6MeFCSnQ8")

for i in range(30):
    next = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    next.click()

    # Section 2
    time.sleep(2)
    randemail = fake.email()
    Email = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    Email.send_keys(randemail)


    # Find the dropdown element by its class name
    dropdown = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/span")
    # Click on the dropdown to open the options
    dropdown.click()
    # Wait for the options to become visible
    time.sleep(2)
    # Get all dropdown options
    options = driver.find_elements(By.CSS_SELECTOR, "div[role='option']")
    time.sleep(2)
    filtered_options = [option for option in options if "choose" not in option.text.lower()]
    # Select a random option from the filtered list
    if filtered_options:
        random_option = random.choice(filtered_options)
        random_option.click()

    # Define the date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    # Function to generate a random date within a range
    def random_date(start, end):
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)
    # Generate a random date
    random_date_value = random_date(start_date, end_date).strftime('%Y-%m-%d')
    # Locate the date input field
    date_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input"))
    )
    time.sleep(2)
    # Input the date
    date_input.send_keys(random_date_value)
    time.sleep(2)

    # Generate a random time between 08:00 AM and 09:00 PM
    def random_time():
        start_time = datetime.strptime("08:00 AM", "%I:%M %p")
        end_time = datetime.strptime("09:00 PM", "%I:%M %p")
        random_seconds = random.randint(0, int((end_time - start_time).total_seconds()))
        random_time_value = start_time + timedelta(seconds=random_seconds)
        return random_time_value.strftime('%I:%M %p')
    random_time_value = random_time()
    # Locate the time input field (assuming it is a text box) and input the time
    time_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input"))
    )
    time_input.send_keys(random_time_value)

    num = random.randint(1,2)
    xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[" + str(num) + "]/label/div"
    radio_button = driver.find_element(By.XPATH, xp)
    radio_button.click()

    num = random.randint(1,7)
    xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[" + str(num) + "]/label/div"
    radio_button = driver.find_element(By.XPATH, xp)
    radio_button.click()

    next = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
    next.click()

    # Section 3
    num = random.randint(1,5)
    xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[" + str(num) + "]/label/div"
    radio_button = driver.find_element(By.XPATH, xp)
    radio_button.click()

    num = random.randint(1,7)
    for i in range(num):
        while i>=0:
            k = random.randint(1,7)
            xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[" + str(k) + "]/label"
            checkbox = driver.find_element(By.XPATH, xp)
            checkbox.click()
            i = i-1


    next = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
    next.click()

    time.sleep(2)

    # Section 4
    for i in range(2,6):
        num = random.randint(1, 5)
        xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[" + str(i) + "]/div/div/div[2]/div/span/div/label[" + str(num) + "]/div[2]/div/div/div[3]/div"
        # Wait for the element to be clickable
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
        radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
        # Click the radio button
        driver.execute_script("arguments[0].click();", radio_button)

    num = random.randint(1,2)
    xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[" + str(num) + "]/label/div"
    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
    # Click the radio button
    driver.execute_script("arguments[0].click();", radio_button)

    next = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
    next.click()
    time.sleep(2)

    # Section 5
    time.sleep(2)
    num = random.randint(1, 2)
    xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[" + str(num) + "]/label/div/div[1]/div/div[3]/div"
    # Wait for the element to be clickable
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
    # Click the radio button
    driver.execute_script("arguments[0].click();", radio_button)

    for i in range(3,6):
        num = random.randint(1, 5)
        xp = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[" + str(i) + "]/div/div/div[2]/div/span/div/label[" + str(num) + "]/div[2]/div/div/div[3]/div"
        # Wait for the element to be clickable
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
        radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, xp)))
        # Click the radio button
        driver.execute_script("arguments[0].click();", radio_button)

    time.sleep(2)
    submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
    submit.click()

    another = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another.click()

    print("Done")








