from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Book a court reservation')
parser.add_argument('--username', default="Vtata", help='Username for login')
parser.add_argument('--password', default="***", help='Password for login')
parser.add_argument('--guest', default="Ripudaman Nanda", help='Guest name')
parser.add_argument('--date', default="03/31/2025", help='Reservation date (MM/DD/YYYY)')
parser.add_argument('--first-time', default="7:00am", help='First preferred time slot')
parser.add_argument('--second-time', default="8:00am", help='Second preferred time slot')

# Parse arguments
args = parser.parse_args()

# Use command line arguments
USERNAME = args.username
PASSWORD = args.password
GUEST = args.guest
DATE = args.date
FIRST_TIME_SLOT = args.first_time
SECOND_TIME_SLOT = args.second_time

# Initialize the WebDriver (Ensure the correct path to the driver)
driver = webdriver.Chrome()  # or use webdriver.Firefox() for Firefox

try:
    # Open the login page
    driver.get("https://njac.clubautomation.com/")

     # Allow time for the page to load
    wait = WebDriverWait(driver, 10)

    # Allow time for page to load
    time.sleep(3)

    # Find and fill in the username field
    username_input = driver.find_element(By.ID, "login")  # Adjust if needed
    username_input.send_keys(USERNAME)

    # Find and fill in the password field
    password_input = driver.find_element(By.ID, "password")  # Adjust if needed
    password_input.send_keys(PASSWORD)

    # Submit the login form
    # Find and click the login button
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()

    # Allow time for the login process
    time.sleep(5)

    # Print success message
    print("Login successful!")

    # menu_reserve_a_court

   # Wait for the dashboard to load and click "Reserve a Court"
    reserve_court_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Reserve a Court')]")))
    reserve_court_link.click()

    # Allow time for the login process
    time.sleep(5)


     # Wait for the "Add Participant" div to appear
    addparticipant_div = driver.find_element(By.ID, "addParticipant")

    # Click the "Add Participant" div
    addparticipant_div.click()

    # Allow time for the login process
    time.sleep(5)

     # Wait for the "Add Participant" div to appear
    guest_text = driver.find_element(By.ID, "guest_1")
    guest_text.send_keys(GUEST)

    # Wait for the autocomplete dropdown to appear
    time.sleep(2)  # Sometimes, explicit waits don't work well with dropdowns, so a small delay helps

    # Press the Down Arrow key to select the first autocomplete option
    guest_text.send_keys(Keys.ARROW_DOWN)
    guest_text.send_keys(Keys.RETURN)  # Press Enter to select

    date_text = driver.find_element(By.ID, "date")
    date_text.clear()
    date_text.send_keys(DATE)

   # Wait for the radio buttons with name "interval" to be present
    # Wait for the radio button with name "interval" and select the one with id "interval-120"
    radio_buttons = wait.until(EC.presence_of_all_elements_located((By.NAME, "interval")))

    # Iterate through the list of radio buttons and click the one with id "interval-120"
    for radio_button in radio_buttons:
        if radio_button.get_attribute("id") == "interval-120":
            driver.execute_script("arguments[0].click();", radio_button)  # Use JavaScript click
            break


    

    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()


    # Wait for the reservation table to load
    wait.until(EC.presence_of_element_located((By.ID, "times-to-reserve")))

    # Try to find and click the first time slot
    try:
        first_slot = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{FIRST_TIME_SLOT}')]")))
        first_slot.click()
        print(f"{FIRST_TIME_SLOT} slot selected!")
        time.sleep(5)
        search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]")
        search_button.click()
    except:
        # If first time slot is not available, select second time slot
        try:
            second_slot = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{SECOND_TIME_SLOT}')]")))
            second_slot.click()
            print(f"{FIRST_TIME_SLOT} unavailable. {SECOND_TIME_SLOT} slot selected!")
            time.sleep(5)

            search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]")
            search_button.click()
        except:
            print(f"Neither {FIRST_TIME_SLOT} nor {SECOND_TIME_SLOT} is available.")
            

    

    print("Booked Appointment")

    time.sleep(30)


    
   
 
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser after execution
    time.sleep(3)
    driver.quit()
