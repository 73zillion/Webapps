import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/black/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price"})
string_price = element.text.strip() # "£129.00"
price_without_symbol = string_price[1:] # "129.00"

price = float(price_without_symbol)

if price < 200:
    print("You should buy the chair!")
    print("The current price is {}.".format(string_price))
else:
    print("Do not buy, it's too expensive!")

# <p class="price price--large"> £129.00 </p>

