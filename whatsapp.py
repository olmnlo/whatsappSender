from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for manual QR code scan
input("Press Enter after scanning the QR code")

# List of numbers (with country code)
numbers = ["+966444444"]
msg = f"Hello world"
# msg you want to send
for person in range(len(numbers)):
    url = f'https://web.whatsapp.com/send?phone={numbers[person]}&text={msg}'
    driver.get(url)
    time.sleep(10)  # Wait for the chat to load

    try:
        # Use CSS selector to find the send button
        send_button = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="send"]')
        send_button.click()
        print(f"Message sent to {numbers[person]}")
        time.sleep(3)  # Wait before moving to the next number
    except Exception as e:
        print(f"Failed to send message to {numbers[person]}: {str(e)}")

driver.quit()
