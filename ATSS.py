from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time


def login(driver, username, password):
    # Gehe zur Login-Seite
    driver.get("https://deine-website.com/login")

    # Warte, bis die Seite geladen ist
    time.sleep(2)

    # Finde die Login-Felder und gebe die Daten ein
    driver.find_element(By.ID, "username_input_id").send_keys(username)
    driver.find_element(By.ID, "password_input_id").send_keys(password)

    # Drücke den Login-Button
    driver.find_element(By.ID, "login_button_id").click()


def select_homeoffice(driver):
    # Gehe zur Zeiterfassungsseite
    driver.get("https://deine-website.com/zeiterfassung")

    # Warte, bis die Seite geladen ist
    time.sleep(2)

    # Finde beide Checkboxen
    homeoffice_checkbox = driver.find_element(By.ID, "homeoffice_checkbox_id")  # Richtige ID einfügen
    zuhause_checkbox = driver.find_element(By.ID, "zuhause_checkbox_id")  # Richtige ID einfügen

    # Stelle sicher, dass nur Homeoffice ausgewählt ist
    if not homeoffice_checkbox.is_selected():
        homeoffice_checkbox.click()  # Homeoffice aktivieren

    if zuhause_checkbox.is_selected():
        zuhause_checkbox.click()  # "Zuhause" deaktivieren, falls nötig

    time.sleep(1)


def start_time_tracking(driver):
    # Finde und klicke auf die "Starten"-Schaltfläche
    start_button = driver.find_element(By.ID, "start_button_id")  # Richtige ID einfügen
    start_button.click()


def stop_time_tracking(driver):
    # Finde und klicke auf die "Beenden"-Schaltfläche
    stop_button = driver.find_element(By.ID, "stop_button_id")  # Richtige ID einfügen
    stop_button.click()


def logout(driver):
    # Gehe zur Logout-Seite
    driver.get("https://deine-website.com/logout")

    # Warte, bis die Seite geladen ist
    time.sleep(2)

    # Führe den Logout aus
    driver.find_element(By.ID, "logout_button_id").click()


def main():
    # WebDriver für Firefox initialisieren
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        # Benutzername und Passwort
        username = "dein_benutzername"
        password = "dein_passwort"

        # Login
        login(driver, username, password)

        # Homeoffice-Checkbox auswählen
        select_homeoffice(driver)

        # Zeiterfassung starten
        start_time_tracking(driver)

        # Warte für 8 Stunden (Arbeitszeit)
        time.sleep(8 * 3600)

        # Zeiterfassung stoppen
        stop_time_tracking(driver)

        # Logout
        logout(driver)

    finally:
        # Schließe den Browser
        driver.quit()


if __name__ == "__main__":
    main()
