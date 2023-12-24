from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import random

Builder.load_file('design.kv')

class MyScreen(Screen):
    def play(self):
        diceface = random.choice(["dice_1.png", "dice_2.png", "dice_3.png", "dice_4.png",
                                             "dice_5.png", "dice_6.png"])
        filename = "assets/" + diceface
        self.ids.dice_state.source = filename


class MainApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return RootWidget()


class RootWidget(ScreenManager):
    pass

if __name__ == "__main__":
    MainApp().run()
#ma = MainApp()
#ma.run()



