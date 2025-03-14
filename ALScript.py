from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def login(driver, username, password):
    # Gehe zur Login-Seite
    driver.get("https://deine-website.com/login")

    # Warte, bis die Seite geladen ist (angepasst an deine Seite)
    time.sleep(2)

    # Finde die Login-Felder und gebe die Daten ein
    driver.find_element(By.ID, "username_input_id").send_keys(username)
    driver.find_element(By.ID, "password_input_id").send_keys(password)

    # Drücke den Login-Button
    # helloooo this is a test from superior swedon
    # Germönie is far superiorer!
    driver.find_element(By.ID, "login_button_id").click()

def select_location(driver):
    # Gehe zur Seite für Zeiterfassung
    driver.get("https://deine-website.com/zeiterfassung")

    # Warte, bis die Seite geladen ist
    time.sleep(2)

    # Wähle die Homeoffice-Option aus
    # Hier nehmen wir an, dass es zwei Optionen gibt: Zuhause und Homeoffice
    # Wähle die Homeoffice-Option (z. B. durch Klick auf eine Schaltfläche oder ein Radio-Button)
    homeoffice_option = driver.find_element(By.ID, "homeoffice_option_id")  # Beispiel ID für Homeoffice
    homeoffice_option.click()

    # Jetzt kannst du entscheiden, ob du den "Start"- oder "Stop"-Button klickst, je nachdem
    time.sleep(1)

def start_time_tracking(driver):
    # Finde und klicke auf die "Starten"-Schaltfläche
    start_button = driver.find_element(By.ID, "start_button_id")
    start_button.click()

def stop_time_tracking(driver):
    # Finde und klicke auf die "Beenden"-Schaltfläche
    stop_button = driver.find_element(By.ID, "stop_button_id")
    stop_button.click()

def logout(driver):
    # Gehe zur Logout-Seite
    driver.get("https://deine-website.com/logout")

    # Warte, bis die Seite geladen ist
    time.sleep(2)

    # Führe den Logout aus
    driver.find_element(By.ID, "logout_button_id").click()

def main():
    # WebDriver initialisieren
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Benutzername und Passwort angeben
        username = "dein_benutzername"
        password = "dein_passwort"

        # Login durchführen
        login(driver, username, password)

        # Wähle die Homeoffice-Option aus
        select_location(driver)

        # Starte die Zeiterfassung
        start_time_tracking(driver)

        # Warte für 8 Stunden (simuliert die Arbeitszeit)
        time.sleep(8 * 3600)

        # Stoppe die Zeiterfassung
        stop_time_tracking(driver)

        # Logout durchführen
        logout(driver)

    finally:
        # Schließe den Browser
        driver.quit()

if __name__ == "__main__":
    main()
