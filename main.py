import requests
import smtplib
from bs4 import BeautifulSoup

BUY_PRICE = 175
MY_EMAIL = ""
MY_PASSWORD = ""

URL = ""

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.159 Safari/537.36 ",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
title = soup.find(id="productTitle").getText().strip()


price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )