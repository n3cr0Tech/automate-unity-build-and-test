from base_page import BasePage
from altunityrunner import By

class GamePage(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene("SampleScene")

    @property
    def my_button(self):
        return self.altdriver.find_object(By.NAME, 'MyButton')

    @property
    def my_textbox(self):
        return self.altdriver.find_object(By.NAME, "MyTextbox")

    def press_my_button(self):
        self.my_button.tap()

    def get_my_textbox_text(self):
        return self.my_textbox.get_text()

    
