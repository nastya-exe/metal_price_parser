import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from bd_request import save_price_to_db, get_last_price
from config import url_gold, url_silver


def scrape_price_metal(url):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    info = WebDriverWait(driver=driver, timeout=5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.m-chart-legend-value"))
    )

    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    price_str = info.text
    price_float = float(price_str.replace(' ', ''))

    driver.quit()
    print(f'Запущен парсер, цена металла {price_str}')

    return date, price_str, price_float


def start():
    while True:
        time_now = datetime.now().time().strftime("%H:%M")
        for url, metal in [(url_gold, 'gold'), (url_silver, 'silver')]:
            date, price_str, price_float = scrape_price_metal(url)
            last_price = get_last_price(metal)[0]

            if last_price != price_float or '22:55' <= time_now <= '23:00':
                save_price_to_db(metal, price_float, date)

        if '22:38' <= time_now <= '23:00':
            time.sleep(240)
        else:
            time.sleep(1200)


if __name__ == '__main__':
    # start()
    scrape_price_metal(url_gold)
    scrape_price_metal(url_silver)


