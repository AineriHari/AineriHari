import io
import logging
import os
import smtplib
from pathlib import Path
from dotenv import load_dotenv
from email.message import EmailMessage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.remote.webelement import WebElement

debugging = True

log_stream = io.StringIO()
log_format = "%(message)s"

logging.basicConfig(stream=log_stream, level=logging.INFO, format=log_format)

load_dotenv()

LOGIN_PAGE = os.get('LOGIN_PAGE')
ACCOUNT_NUMBER = os.get('ACCOUNT_NUMBER')
LAST_NAME = os.get('LAST_NAME')
CARD_NUM = os.get('CARD_NUM')
CARD_MONTH = os.get('CARD_MONTH')
CARD_YEAR = os.get('CARD_YEAR')
CARD_CVV = os.get('CARD_CVV')
PHONE_NUMBER = os.get('PHONE_NUMBER')
APP_PASSWORD = os.get('APP_PASSWORD')

script_directory = Path(__file__).resolve().parent
driver_path = script_directory.joinpath("ChromeDriver-mac-ard64", "chromeDriver")

# script_directory = os.path.abspath(__file__)
# driver_path = os.path.join(script_directory, "ChromeDriver-mac-ard64", "chromeDriver")

chrome_options = Options()
if debugging:
    chrome_options.add_experimental_option('detach', True)
else:
    chrome_options.add_argument('--headless')

def set_field_to_password(driver: webdriver.Chrome, element_id: str) -> None:
    """Set the field to password

    Args:
        driver (webdriver.Chrome): Chrome driver
        element_id (str): web element id
    """
    driver.execute_script(f"document.getElementById('{element_id}').type = 'password'")

def wait_for_element(driver: webdriver.Chrome, by: By, element_identifier: str, timeout: int = 5) -> WebElement:
    """wait for element

    Args:
        driver (webdriver.Chrome): Chrome
        by (By): By
        element_identifier (str): element identifier
        timeout (int, optional): timeout. Defaults to 5.

    Returns:
        WebElement: webelement
    """
    try:
        element_presence = EC.presence_of_element_located((by, element_identifier))
        WebDriverWait(driver, timeout).until(element_presence)
    except TimeoutException:
        logging.info(f"Timed out waiting for {element_identifier}")
        return None
    return driver.find_element(by, element_identifier)


def login_to_account(driver: webdriver.Chrome) -> None:
    """login to account

    Args:
        driver (webdriver.Chrome): Chrome
    """
    driver.get(LOGIN_PAGE)

    account_input = wait_for_element(driver, By.ID, 'Account')
    name_input = wait_for_element(driver, By.ID, 'Name')

    if account_input:
        set_field_to_password(driver, 'Account')
        set_field_to_password(driver, 'Name')
        account_input.send_keys(ACCOUNT_NUMBER)
        name_input.send_keys(LAST_NAME)

    submit_button = wait_for_element(driver, By.XPATH, '//input[@type="submit"][@name="Submit"]')

    if submit_button:
        submit_button.click()


def submit_payment(driver: webdriver.Chrome) -> bool:
    """submit payment

    Args:
        driver (webdriver.Chrome): Chrome

    Returns:
        bool: True or False
    """
    num_input = wait_for_element(driver, By.ID, "cardnumber")
    month_input = wait_for_element(driver, By.ID, "month")
    year_input = wait_for_element(driver, By.ID, "year")
    cvv_input = wait_for_element(driver, By.ID, "cvv")
    payment_amt = wait_for_element(driver, By.ID, "payment")
    confirm_checkbox = wait_for_element(driver, By.ID, "confirm")
    submit_button = wait_for_element(driver, By.ID, "submitbtn")

    if payment_amt:
        payment_amt_str = payment_amt.get_attribute("value")
        logging.info(f"Payment amount: {payment_amt_str}")
        try:
            payment_amount = float(payment_amt_str)
            if payment_amount <= 0.00:
                logging.info("No payment due.")
                return False
            elif payment_amount > 300.00:
                logging.info("Payment amount high. Check manually.")
                return False
        except ValueError:
            logging.info("Invalid payment amount")
            return False 

    if (
        num_input
        and month_input
        and year_input
        and cvv_input
        and confirm_checkbox
        and submit_button
    ):
        num_input.send_keys(CARD_NUM)
        month_input.send_keys(CARD_MONTH)
        year_input.send_keys(CARD_YEAR)
        cvv_input.send_keys(CARD_CVV)

        confirm_checkbox.click()
        submit_button.click()

    try:
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//body"), "Thank you for your payment"
            )
        )
        return True
    except TimeoutException:
        logging.info("Payment failed.")
        return False


def send_message(subject: str, receiver: str):
    sender = 'abc@gmail.com'
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(log_stream.getvalue())

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login(sender, APP_PASSWORD)
         smtp.send_message(msg)


def main():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login_to_account(driver)
        payment_success = submit_payment(driver)
        if payment_success:
            message = "Sucessful payment."
            logging.info(message)
            send_message(message, 'abc@gmail.com')
            send_message(message, f'{PHONE_NUMBER}@mms.att.net')
        else:
            message = "Failed payment."
            logging.info(message)
            send_message(message, 'abc@gmail.com')
            send_message(message, f'{PHONE_NUMBER}@mms.att.net')
    except WebDriverException as e:
        logging.info(f"General WebDriver error: {e}")
        send_message(message, 'abc@gmail.com')
        send_message(message, f'{PHONE_NUMBER}@mms.att.net')
    finally:
        if debugging:
            print(log_stream.getvalue())
        else:
            driver.quit()


if __name__ == '__main__':
    main()