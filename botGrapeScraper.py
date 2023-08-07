from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random
import smtplib
from email.message import EmailMessage
import smtplib
from getpass import getpass
from twilio.rest import Client

from twilio.rest import Client

account_sid = '*****'
auth_token = '*****'

notification_bol = False
counter = 0
while notification_bol == False:
    def notification_email():
        notification_bol = True
        print("sending email ...")
        msg = EmailMessage()
        msg['Subject'] = 'GrapeFestival'
        msg['From'] = 'Sebastian Klinovsky'
        msg['To'] = 'slavka.kurjak@gmail.com'
        msg.set_content('GrapeFestival - open positions 2')
        myServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        myServer.login('sebastian.klin@gmail.com', '*****')
        myServer.send_message(msg)
        msg2 = EmailMessage()
        msg2['Subject'] = 'GrapeFestival'
        msg2['From'] = 'Sebastian Klinovsky'
        msg2['To'] = 'sebastian.klin@gmail.com'
        msg2.set_content('GrapeFestival - open positions 2')
        myServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        myServer.login('sebastian.klin@gmail.com', '*******')
        myServer.send_message(msg2)
        myServer.quit()
        ######### WHATSAPP MSG ############
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='GrapeFestival, UZ TO JE OTVORENE TAK SA TAM PRIHLASUJ na https://volunteers.grapefestival.sk/',
        to='whatsapp:+32488728519'
        )
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='GrapeFestival, UZ TO JE OTVORENE TAK SA TAM PRIHLASUJ na https://volunteers.grapefestival.sk/',
        to='whatsapp:+421907403712'
        )

    #Option to hide driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #Getting driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://volunteers.grapefestival.sk/login/")

    username = "sebastian.klin@gmail.com"
    password = "************"

    # Fill in username and password and click on login
    wait = WebDriverWait(driver, 30)
    # time.sleep(random.randint(1, 3))
    username_input = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
    username_input.send_keys(username)

    # time.sleep(random.randint(1, 3))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "id_password")))
    password_input.send_keys(password)


    #<button type="submit" class="btn btn'default">Prihlásiť sa</button>
    time.sleep(random.randint(1, 3))
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    #open next page        
    # time.sleep(random.randint(1, 10))

    next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(normalize-space(), 'Prihlasovanie na pozície')]")))
    next_page.click()

    #go to THE PAGE FOR POSITION 2 
    driver.get("https://volunteers.grapefestival.sk/position/2")

    # class="card mb-3"
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    txt = soup.find_all("div", class_="card mb-3")

    if len(txt) > 0:
        notification_email()
        driver.quit()
        break
    else:
        time.sleep(random.randint(250, 350))
        counter += 1
        print("counter: ", counter)
        continue

    
