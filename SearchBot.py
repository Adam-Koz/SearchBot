import requests
from bs4 import BeautifulSoup
import smtplib, time

URL = 'https://www.nike.com/pl/t/skarpety-treningowe-do-kostki-everyday-cushioned-lZ03sD/SX7667-010'

def CheckPrice():

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = 'pdp_product_title').get_text()
    price = soup.find_all("div", class_= "product-price css-11s12ax is--current-price")
    Price = ''.join(price[0])[0:5]
    ConvertedPrice = float(Price.replace(",", "."))
    print(ConvertedPrice)
    print(title)
    if(ConvertedPrice < 49.99):
        SendMail()

def SendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("koz.adamxd@gmail.com", "hxoodtgdbquywuvw")
    subject = "Dziwko cena skapet spadla"
    body = "Masz link: https://www.nike.com/pl/t/skarpety-treningowe-do-kostki-everyday-cushioned-lZ03sD/SX7667-010"
    msg = f"Subject: {subject}\n\n {body}"
    server.sendmail(
        'koz.adamxd@gmail.com',
        'koz.adam1@outlook.com',
        msg)
    server.sendmail(
        'koz.adamxd@gmail.com',
        'owocek30@gmail.com',
        msg)
    print("SENDED")
    server.quit()
while(True):
    CheckPrice()
    time.sleep(10)
