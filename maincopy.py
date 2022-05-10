from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import random

# Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 650)


class ListTwo(Screen):#второй экран
    def __init__(self, **kw):
        super(ListTwo, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        background = Image(source='background.png', allow_stretch=True, keep_ratio=False)

        label0 = Label(text='ВЫБОР ФИЛЬМА', font_size='20sp', halign='center')
        btn_test = Button(text='Рандом', size_hint_x=.17, on_press=lambda x: set_screen('rand'))

        button_next = Button(text='ВЫБРАТЬ', on_press=lambda x: set_screen('ListTree'),
                             background_color=[.32, .85, .94, 1], size_hint=(0.4, .4), pos_hint={'x': 0.2, 'y': 0.2})

        box_next = BoxLayout(size_hint=(0.4, 0.2), pos_hint={'x': 0.3, 'y': 0})
        box_next.add_widget(button_next)

        box = BoxLayout(size_hint=(1, 0.05), pos_hint={'x': 0, 'y': 0.95}, orientation='horizontal')
        box.add_widget(label0)
        box.add_widget(btn_test)


        layout = GridLayout(cols=3, padding=[40, 0, 40, 0], spacing=5, size_hint=(1, 0.7),
                            pos_hint={'x': 0, 'y': 0.2})

        btn1 = Button(background_normal='adven.jpg', on_press=lambda x: set_screen('adven'),
                      background_down='blue.png')
        btn2 = Button(background_normal='bourn.jpg', on_press=lambda x: set_screen('bourn'),
                      background_down='blue.png')
        btn3 = Button(background_normal='darkfields.jpg', on_press=lambda x: set_screen('darkfields'),
                      background_down='blue.png')
        btn4 = Button(background_normal='expend.jpg', on_press=lambda x: set_screen('expend'),
                      background_down='blue.png')
        btn5 = Button(background_normal='here.jpg', on_press=lambda x: set_screen('here'),
                      background_down='blue.png')
        btn6 = Button(background_normal='imperator.jpg', on_press=lambda x: set_screen('imperator'),
                      background_down='blue.png')
        btn7 = Button(background_normal='lovewith.jpg', on_press=lambda x: set_screen('lovewith'),
                      background_down='blue.png')
        btn8 = Button(background_normal='noeye.jpg', on_press=lambda x: set_screen('noeye'),
                      background_down='blue.png')
        btn9 = Button(background_normal='raid.jpg', on_press=lambda x: set_screen('raid'),
                      background_down='blue.png')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        layout.add_widget(btn7)
        layout.add_widget(btn8)
        layout.add_widget(btn9)

        super_layout = FloatLayout()

        super_layout.add_widget(background)
        super_layout.add_widget(layout)
        super_layout.add_widget(box_next)

        ultra_super_layoyt = BoxLayout(orientation='vertical')
        ultra_super_layoyt.add_widget(box)
        ultra_super_layoyt.add_widget(super_layout)

        self.add_widget(ultra_super_layoyt)



def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(ListTwo(name='two'))



class FoodOptionsApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    FoodOptionsApp().run()
