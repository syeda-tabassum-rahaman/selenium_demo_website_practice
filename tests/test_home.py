from seleniumbase import BaseCase
from page_objects.home_page import HomePage


class HomeTest(BaseCase):

    def setUp(self):
        super().setUp()
        print("Running before each test")

        # open home page
        HomePage.open_page(self)

    def tearDown(self):
        print("Running after each test")
        super().tearDown()

    def test_home_page(self):
        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(HomePage.logo_icon)

        # click on the get started button and assert the url
        self.click(HomePage.get_started_btn)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)

        # get the text of the header and assert the value
        self.assert_text("Think different. Make different.", HomePage.heading_text)

        # scroll to bottom and assert the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", HomePage.copyright_text)

    def test_menu_links(self):
        # find menu links elements
        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

        menu_links_element = self.find_elements(HomePage.menu_links)

        for idx, menu_link in enumerate(menu_links_element):
            # print(idx, menu_link.text)
            self.assert_equal(expected_links[idx], menu_link.text)
