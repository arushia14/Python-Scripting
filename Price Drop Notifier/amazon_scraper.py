import requests
from bs4 import BeautifulSoup
import smtplib
import time

def price_check():
    url = 'YOUR AMAZON PRODUCT LINK GOES HERE'

    headers = {
        'user-agent': 'YOUR USER AGENT GOES HERE' # To get your user agent, simply Google "what is my user agent"
    }

    page = requests.get(url, headers = headers)  # Requesting the content online
    soup = BeautifulSoup(page.content, 'html.parser') # Scraping the page content and parsing the HTML to string
    title = soup.find(id='productTitle').get_text().strip() # Finding the title of the product and getting only the text, and stripping the extra space
    price = soup.find(id='priceblock_ourprice').get_text().strip() # Doing the same for price
    
    ''' 
    The code below is subjective to Amazon.in where the prices are mentioned in Indian Rupees. 
    In case of a difference region or currency, please modify according to the comments mentioned.
    '''
    
    pricefloat = price[2:-3]     # Getting the actual cost and removing the currency symbol 
    pricefloat = float(pricefloat.replace(',', ''))  # Converting the value to float from string

    if pricefloat < 4000:  # 4000 here can be replaced by the price you want
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('* SENDER EMAIL ID *', '* PASSWORD SENDER EMAIL *')

    subject = "PRODUCT PRICE DOWN!"
    body = "The XYZ product is available for a cheaper price on Amazon. Check it out!, *ADD LINK HERE*"
    
    mail = (f'Subject: {subject} \n\n {body}')

    server.sendmail(
        '* SENDER EMAIL ID(from above) *',
        '* RECEIVER EMAIL ID *',
        mail
    )

    print("The email has been sent!")
    server.quit()

while (True):
    price_check()
    time.sleep(21600) # Runs this code every 6 hours