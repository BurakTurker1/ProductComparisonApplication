import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

# Ürün özelliklerini depolamak için bir sözlük oluşturun
urun_ozellikleri = {}


class Testim(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_bir_sey(self):
        driver = self.driver
        driver.get("https://www.trendyol.com/")
        arama_cubugu = driver.find_element(By.CLASS_NAME, "V8wbcUhU")

        urun_adi = input("Ürün adını giriniz: ")  # Kullanıcıdan ürün adını alın
        arama_cubugu.send_keys(urun_adi)
        arama_cubugu.send_keys(Keys.ENTER)
        WebDriverWait(driver, 4).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "prc-box-dscntd"))
        )

        # Ürün fiyatlarını ve isimlerini al
        fiyatlar = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")
        urun_adlari = driver.find_elements(By.CLASS_NAME, "prdct-desc-cntnr-name.hasRatings")

        # Verileri düzenle ve sözlüğe ekle
        for index, (fiyat_elementi, ad_elementi) in enumerate(zip(fiyatlar, urun_adlari), start=1):
            urun_ozellikleri[f'Ürün {index}'] = {
                'İsim': ad_elementi.text,
                'Fiyat': fiyat_elementi.text
            }

        # Ürün bilgilerini yazdır
        for urun, detaylar in urun_ozellikleri.items():
            print(f'{urun}:')
            print(f'İsim: {detaylar["İsim"]}')
            print(f'Fiyat: {detaylar["Fiyat"]}')
            print('-' * 30)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
