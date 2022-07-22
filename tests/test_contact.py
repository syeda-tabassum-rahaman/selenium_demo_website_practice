from seleniumbase import BaseCase


class ContactTest(BaseCase):
    def test_contact_page(self):
        # open the url

        self.open("https://practice.automationbro.com/contact")

        # scroll to the empty form and take screenshot

        # self.scroll_to("#evf-form-277")
        # self.save_screenshot("empty_contact_form", "custom_screenshots")

        # fill in all the fields

        self.send_keys('.contact-name input', 'chowa')
        self.send_keys('.contact-email input', 'chowa@gmail.com')
        self.send_keys('.contact-phone input', '0123456789')
        self.send_keys('.contact-message textarea', 'chowa-kowa')

        # take screenshot when the form is filled

        # self.save_screenshot("filled_contact_form", "custom_screenshots")

        # click the submit button

        self.click('#evf-submit-277')

        # verify submit message

        self.assert_text('Thanks for contacting us! We will be in touch with you shortly', 'div[role = alert]')
