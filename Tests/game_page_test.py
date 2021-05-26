from game_page import GamePage
from base_test import BaseTest

class GamePageTest(BaseTest):    
    altdriver = BaseTest.altdriver

    def setUp(self):        
        self.game_page = GamePage(self.altdriver)
        self.game_page.load()        

    def test_button_press_causes_textbox_to_display_hello(self):
        self.game_page.press_my_button()
        expected_text = "Hello there"                                    
        actual_text = self.game_page.get_my_textbox_text()
        # print("actual: " + actual_text + " <VS> expected: " + expected_text )
        assert(expected_text == actual_text)
