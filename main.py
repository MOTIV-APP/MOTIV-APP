from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton

Builder.load_string('''
<MainScreen>:
    name: 'main'
    MDBottomNavigation:
        id: bottom_navigation
        MDBottomNavigationItem:
            name: 'steps'
            text: 'Шаги'
            icon: 'steps.png'
        MDBottomNavigationItem:
            name: 'game'
            text: 'Игра'
            icon: 'game.png'
        MDBottomNavigationItem:
            name: 'rewards'
            text: 'Награды'
            icon: 'rewards.png'
        MDBottomNavigationItem:
            name: 'settings'
            text: 'Настройки'
            icon: 'settings.png'
            MDCard:
                pos_hint: {'center_x': 0.5, 'center_y': 1.4}
                padding: 20
                spacing: 200
                orientation: 'vertical'
                MDFlatButton:
                    text: 'Сменить тему'
                    on_release: app.change_theme()
''')

class MainScreen(Screen):
    pass

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen())
        return screen_manager

    def change_theme(self):
        if self.theme_cls.theme_style == 'Dark':
            self.theme_cls.theme_style = 'Light'
            self.theme_cls.primary_palette = 'Blue'
        else:
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Blue'

TestApp().run()