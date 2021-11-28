from time import sleep
import requests
from bs4 import BeautifulSoup
import smtplib
import cloudscraper

l0 = 'https://www.innvictus.com/mujeres/basket/tenis/nike/tenis-air-jordan-1-low-unc/p/000000000000161793'
l1 = 'https://www.innvictus.com/ninos/casual/tenis/nike/tenis-air-jordan-1-mid-light-smoke/p/000000000000161754'
l2 = 'https://www.innvictus.com/hombres/basket/tenis/jordan/tenis-air-jordan-1-mid-light-smoke-grey/p/000000000000160447'
l3 = 'https://www.innvictus.com/mujeres/basket/tenis/nike/tenis-air-jordan-1-low-spruce-aura/p/000000000000162364?utm_source=fb&utm_medium=social&utm_campaign=oct_2020j1lowspruce'
l4 = 'https://www.innvictus.com/mujeres/basket/tenis/nike/tenis-air-jordan-1-low-spruce-aura/p/000000000000162364?utm_source=fb&utm_medium=social&utm_campaign=oct_2020j1lowspruce'
l5 = 'https://www.innvictus.com/mujeres/basket/tenis/jordan/tenis-air-jordan-1-retro-high-og-satin-red/p/000000000000165312'
l6 = 'https://www.innvictus.com/ninos/basket/tenis/jordan/tenis-air-jordan-1-retro-high-og-gs-smoke-grey/p/000000000000164954'

u0 = 'https://www.innvictus.com/p/000000000000160601'
u1 = 'https://www.innvictus.com/ninos/basket/tenis/nike/air-jordan-1-retro-high-og-gs/p/000000000000164954'
u2 = 'https://www.innvictus.com/p/000000000000164954'
u3 = 'https://www.innvictus.com/ninos/basket/tenis/nike/air-jordan-1-retro-high-og-gs/p/000000000000164954'
u4 = 'https://www.innvictus.com/ninos/basket/tenis/jordan/tenis-air-jordan-1-retro-high-og-gs-smoke-grey/p/000000000000164954'

URL = [[l0, False], [l1, False], [l2, False], [l3, False], [l4, False], [l5, False], [l6, False]]
URL2 = [l0, l1, l2, l3, l4, l5, l6]
URL3 = [u0, u1, u2, u3, u4]
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'}


def snkcheck():
    c = 0
    while c < 7:
        scraper = cloudscraper.create_scraper()
        page = scraper.get(URL2[c]).text
        soup = BeautifulSoup(page, 'html.parser')
        title = soup.find(id="productName").get_text()
        price = soup.find(id="pdpCurrent_wholePart").get_text()
        converted_price = float(price[0:5].replace(',', '.'))
        strprice = str(converted_price)
        globalstate = soup.find('div', attrs={'id': 'js-stock-notification-container'})
        x = str(globalstate)
        z = x.split()

        if 'hidden"' in z:
            print(title)
            print("$", converted_price)
            print("Si hay!")
            if URL[c][1] == False:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()

                server.login('brandon.gamiz.tinoco@gmail.com', 'California15*')

                subject = 'INNVICTUS | Ya hay stock!'
                body = 'Ya hay stock de un par, ve y revisa el precio! Entra al link a comprar ' + URL2[c]

                msg = f"Subject: {subject}\n\n{body}"

                server.sendmail(
                    'brandon.gamiz.tinoco@gmail.com',
                    'brandonb.gt@outlook.com',
                    msg
                )
                print("HEY YA SE ENVIO EL CORREO")

                server.quit()

                URL[c][1] = True
        else:
            print(title)
            print("$", converted_price)
            print("No hay")
        c = c + 1

def snkcheck2():
    c = 0
    while c < 5:
        page = requests.get(URL3[c], headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        globalstate = soup.find('div', attrs={'class': 'pdp-notFound'}).get_text()
        x = globalstate.split()

        if "no" and "disponible" in x:
            print("Todavía no está disponible.")
        else:
            print("El estado de la página ya cambió, ve a revisar si todavía hay.")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('brandon.gamiz.tinoco@gmail.com', 'California15*')

            subject = 'INNVICTUS | El estado de la página cambió!'
            body = 'El estado de la página ya cambió, ve a revisar si todavía hay!' + URL3[c]

            msg = f"Subject: {subject}\n\n{body}"

            server.sendmail(
                'brandon.gamiz.tinoco@gmail.com',
                'brandonb.gt@outlook.com',
                msg
            )
            print("HEY YA SE ENVIO EL CORREO")

            server.quit()
        c = c + 1


while True:
    snkcheck()
    #snkcheck2()
    sleep(5)