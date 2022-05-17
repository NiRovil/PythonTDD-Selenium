from django.test import LiveServerTestCase
from selenium import webdriver

class AnimalTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_navegador(self):
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()