from selenium import webdriver
from selenium.webdriver.common.by import By


def validalas():
    # Hozz létre egy Firefox driver példányt!
    driver = webdriver.Firefox()

    # Töltse be az oldaladat
    driver.get("https://agnes-milia.github.io/urlap_validalas/")

    # A nevek alapján kerestessük meg az űrlap elemeit!
    name_field = driver.find_element(By.NAME, "nev")
    pw_field = driver.find_element(By.NAME, "jelszo")
    email_field = driver.find_element(By.NAME, "email")

    # ...
    # A következő elemet nem kell átírnod:
    submit_gomb = driver.find_element(By.XPATH, "//input[@type='submit']")

    # Add meg a működő - majd később a nem működő - teszt adatokat!
    name_field.send_keys("John Smith")
    email_field.send_keys("john.smith@example.hu")
    pw_field.send_keys("blaa")
    # ...

    #valid fájl
    validFajl = open("valid.txt", "r", encoding="utf-8")
    validFajl.readline()
    adatok = validFajl.readlines()
    i = 0
    while i < len(adatok):

    validFajl.close()

    # valid fájl
    nemValidFajl = open("valid.txt", "r", encoding="utf-8")
    nemValidFajl.close()

    # Kattints a submit gombra!
    submit_gomb.click()

    # Várunk egy keveset, hogy lássunk is valamit...
    driver.implicitly_wait(10)

    # Megnézzük, megjelent-e a div elemünk
    success_message = driver.find_element(By.XPATH, "//div[@class='success-message']")
    if success_message.is_displayed():
        print("Sikerült az űrlap küldése!")
    else:
        print("Nem sikerült az űrlap küldése!")

    # Csukjuk be a böngésző ablakot!
    driver.quit()
