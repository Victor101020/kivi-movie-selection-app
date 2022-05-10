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

Config.set('graphics', 'width', 315)
Config.set('graphics', 'height', 560)

films = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish', 'bourn',
         'bridge', 'ceti', 'char', 'cityvor', 'coll', 'cool', 'craft', 'crash', 'crazy', 'dark', 'darkfields',
         'darko', 'dep', 'dragon', 'equ', 'expend', 'expendtwo', 'fish', 'fury', 'glad', 'gonebabygone', 'gray',
        'greenmil', 'hard', 'henkok', 'here', 'hobbit', 'holidays', 'home', 'imperator', 'india', 'ironman',
         'killbill', 'king', 'land', 'legend', 'mad', 'manon', 'megamozg', 'mert', 'million', 'mindhunters',
        'mirrors', 'monstro', 'nebo', 'night', 'lovewith', 'noeye', 'oceans', 'ocoboe', 'oper', 'panda',
        'paris', 'pch', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid', 'ratata']

#первый экран с приветсвием и кнопкой продолжить
class ListOne(Screen):
    def __init__(self, **kw):
        super(ListOne, self).__init__(**kw)
        btn = Button(background_normal='next.png', on_press=lambda x: set_screen('ListTwo'),
                     size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        label = Label(text='[size=18sp]Добро пожаловать в приложение\n'
                           'по подбору фильмов[/size]\n'
                           '[size=14sp]Для этого достаточно просто\n'
                           'выбратьсимпатизирующий вам цвет\n'
                           'Также в функции приложения входят\n'
                           'подбор случайно выбранного фильма\n'
                           'и просмотр информации о фильме,\n'
                           'представленном на экране.\n\n\n[/size]'
                           '[size=12sp]Чтобы перейти дальше,\n'
                           'нажмите продолжить[/size]', markup=True, halign='center')

        box = FloatLayout()
        img = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        box.add_widget(img)

        fl = RelativeLayout()
        fl.add_widget(label)
        box.add_widget(fl)
        box.add_widget(btn)
        self.add_widget(box)


#Вторая страница с выбором 9-и фильмов, кнопки продолжить и кнопкой рандомный фильм
class ListTwo(Screen):#второй экран где можно выбратт рандомный фильм, фильм из предложенного или продолжение
    def __init__(self, **kw):
        super(ListTwo, self).__init__(**kw)

    def on_enter(self):
        background = Image(source='background.png', allow_stretch=True, keep_ratio=False)

        label0 = Label(text='ВЫБОР ФИЛЬМА', font_size='20sp', halign='center')
        btn_test = Button(size_hint_x=.2, background_normal='random.png',
                          on_press=lambda x: set_screen('rand')) #text='Рандом',

        button_next = Button(on_press=lambda x: set_screen('ListTree'), background_normal='films.png',
                             size_hint=(0.8, 0.8), pos_hint={'x': 0.1, 'y': 0.1})

        box_next = BoxLayout(size_hint=(1, 0.2), pos_hint={'x': 0, 'y': 0})
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


#Третья страница с выбора: фильм с детьми или фильм без детей
class ListTree(Screen):
    def __init__(self, **kw):
        super(ListTree, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана

        button_no_adult = Button(on_press=lambda x: set_screen('filmnoadult'),
                             size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.6},
                             background_normal='deti.png')
        button_adult = Button(background_normal='nodeti.png', on_press=lambda x: set_screen('filmadult'), size_hint=(.5, .1),
                              pos_hint={'center_x': 0.5, 'center_y': 0.4})

        img = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='ВЫБОР ФИЛЬМА', font_size='20sp', halign='center')
        btn_test = Button( background_normal='basic_back.png', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_box = BoxLayout(orientation='vertical')

        box = BoxLayout(size_hint=(1, .05), orientation='horizontal')

        box.add_widget(label0)
        box.add_widget(btn_test)

        root = FloatLayout()

        root.add_widget(img)
        root.add_widget(button_no_adult)
        root.add_widget(button_adult)

        super_box.add_widget(box)
        super_box.add_widget(root)

        self.add_widget(super_box)


#эта страница открывается, когда со второго листа нажимается кнопка рандомный фильм
class Rand(Screen):
    def __init__(self, **kw):
        super(Rand, self).__init__(**kw)

    def on_enter(self):
        film = random.choice(films)
        set_screen(film)


#КЛАССЫ ФИЛЬМОВ КЛАССЫ ФИЛЬМОВ КЛАССЫ ФИЛЬМОВ КЛАССЫ ФИЛЬМОВ
#эта страница открывается, когда на втором листе нажали на иконку фильма Адвен
#TODO:проверить все окна с фильмами, некоторые окна падают!!!
class Adven(Screen):
    def __init__(self, **kw):
        super(Adven, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='adven.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True, size_hint=(0.5, .5),
                       pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp', halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(background_normal='basic_back.png', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Artist(Screen):
    def __init__(self, **kw):
        super(Artist, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='artist.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(background_normal='basic_back.png', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Astral(Screen):
    def __init__(self, **kw):
        super(Astral, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='astral.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(background_normal='basic_back.png', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Badboys(Screen):
    def __init__(self, **kw):
        super(Badboys, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='badboys.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Bandaizny(Screen):
    def __init__(self, **kw):
        super(Bandaizny, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='bandaizny.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Batman(Screen):
    def __init__(self, **kw):
        super(Batman, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='batman.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Batmanbegin(Screen):
    def __init__(self, **kw):
        super(Batmanbegin, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='batmanbegin.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Baton(Screen):
    def __init__(self, **kw):
        super(Baton, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='baton.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Bigfish(Screen):
    def __init__(self, **kw):
        super(Bigfish, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='bigfish.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='[color=ff3333]Hello[/color][color=3333ff]World[/color]', markup=True,
                       size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, font_size='20sp',
                       halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')
        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')#слой с текстом описания фильма и кнопкой назад
        box1.add_widget(label0)
        box1.add_widget(btn_test)
        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)
        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)
        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Bourn(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Bourn, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='bourn.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Bridge(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Bridge, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='bridge.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Ceti(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Ceti, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='ceti.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Char(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Char, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='char.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Cityvor(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Cityvor, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='cityvor.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Coll(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Coll, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='coll.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Cool(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Cool, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='cool.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Craft(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Craft, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='craft.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Crash(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Crash, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='crash.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Crazy(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Crazy, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='crazy.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Dark(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Dark, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='dark.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Darkfields(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Darkfields, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='darkfields.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Darko(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Darko, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='darko.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)

class Dep(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Dep, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='dep.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Dragon(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Dragon, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='dragon.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Equ(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Equ, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='equ.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5},halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Expend(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Expend, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='expend.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Expendtwo(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Expendtwo, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='expendtwo.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Fish(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Fish, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='fish.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Fury(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Fury, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='fish.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Glad(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Glad, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='glad.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Gonebabygone(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Gonebabygone, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='gonebabygone.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Gray(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Gray, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='gray.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Greenmil(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Greenmil, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='greenmil.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Hard(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Hard, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='hard.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Henkok(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Henkok, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='henkok.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Here(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Here, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='here.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Hobbit(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Hobbit, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='hobbit.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Holidays(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Holidays, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='holidays.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Home(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Home, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='home.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Imperator(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Imperator, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='imperator.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class India(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(India, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='india.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Ironman(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Ironman, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='ironman.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Killbill(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Killbill, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='killbill.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class King(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(King, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='king.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Land(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Land, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='land.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Legend(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Legend, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='legend.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Lovewith(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Lovewith, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='lovewith.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Mad(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Mad, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='mad.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Manon(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Manon, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='manon.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Megamozg(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Megamozg, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='megamozg.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Mert(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Mert, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='mert.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Million(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Million, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='million.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Mindhunters(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Mindhunters, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='mindhunters.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Mirrors(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Mirrors, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='mirors.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        self.add_widget(super_layout)
        box2.add_widget(super_box)


class Monstro(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Monstro, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='monstro.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Nebo(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Nebo, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='nebo.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Night(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Night, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='night.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Noeye(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Noeye, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='noeye.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Oceans(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Oceans, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='oceans.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Ocoboe(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Ocoboe, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='ocoboe.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Oper(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Oper, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='oper.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Panda(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Panda, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='panda.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Paris(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Paris, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='backgrund.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='paris.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Pch(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Pch, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='pch.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Planeta(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Planeta, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='backgrund.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='planeta.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Pras(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Pras, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='pras.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Pravoonkill(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Pravoonkill, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='backgrund.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='pravoonkill.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Prestish(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Prestish, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='prestish.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Pride(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Pride, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='pride.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Prit(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Prit, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='prit.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Pyli(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Pyli, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='pyli.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(
            text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\nИмя Фамилия\nАктеры\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\nИмя Фамилия\n',
            size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Raid(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Raid, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='raid.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\n',size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


class Ratata(Screen):#экран с рандомным фильмом со второго экрана
    def __init__(self, **kw):
        super(Ratata, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        img2 = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        img1 = Image(source='ratata.jpg', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Название фильма', font_size='20sp', halign='center')
        label1 = Label(text='Дата выхода\nРоссия:28.00.00\nСША:28.00.00\nРежисер\n',size_hint=(0.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')
        label2 = Label(text='Сюжет\ntext text text textt\ntext text  text text text\n'
                            'text text text text text\ntext text text text text text\ntext t text text text\n'
                            'text tet text text text\ntext text ext text text\ntext text tetext text text\n',
                       size_hint=(0.5, 0.), pos_hint={'center_x': 0.5, 'center_y': 0.5}, halign='center')

        btn_test = Button(text='Назад', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        super_layout = BoxLayout(orientation='vertical')  # ,size_hint_y=None, height=dp(40)

        # верхняя часть с кнопкой назaд
        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        # второй слой где расположены картинка, параметры фильма и описание
        box2 = FloatLayout()
        box2.add_widget(img2)

        # главный слой, в нем расположеныы верхняя полоса и основной слой
        super_layout.add_widget(box1)
        super_layout.add_widget(box2)

        super_box = BoxLayout(
            orientation='vertical')  # слой в  который положим картинка+ параметры и описание, т.е. две сущности
        box_image_params = BoxLayout(orientation='horizontal')  # слой основа для картинки и параметров
        bx_image = BoxLayout()  # Слой с картинкой
        bx_image.add_widget(img1)
        bx_params = BoxLayout()  # Слой с параметрами
        bx_params.add_widget(label1)
        box_image_params.add_widget(bx_image)
        box_image_params.add_widget(bx_params)
        bx_discription = BoxLayout()  # Слой с описанием
        bx_discription.add_widget(label2)
        super_box.add_widget(box_image_params)
        super_box.add_widget(bx_discription)
        box2.add_widget(super_box)
        self.add_widget(super_layout)


# КОНЕЦ КЛАССОВ ФИЛЬМОВ КОНЕЦ КЛАССОВ ФИЛЬМОВ КОНЕЦ КЛАССОВ ФИЛЬМОВ КОНЕЦ КЛАССОВ ФИЛЬМОВ КОНЕЦ КЛАССОВ ФИЛЬМОВ КОНЕЦ

# страница открывается, когда с третьего листа нажимают - без детей

class FilmAdult(Screen):#функция нажатия фильм без детей на третьем экране
    def __init__(self, **kw):
        super(FilmAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        background = Image(source='background.png', allow_stretch=True, keep_ratio=False)
        label0 = Label(text='Выберите цвет по настроению', font_size='12sp', halign='center')
        btn_test = Button(background_normal='basic_back.png', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))

        box1 = BoxLayout(size_hint=(1, .05), orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад size_hint_y=None, height=dp(30)

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        box2 = FloatLayout()

        box2.add_widget(background)

        layout_base = BoxLayout(orientation='vertical')
        # Создаем слой с 9 изображениями-ссылками
        layout = GridLayout(cols=2, padding=[70, 70, 70, 70], spacing=5)
        btn1 = Button(background_normal='darkblue.png', on_press=lambda x: set_screen('darkblueadult'),
                      background_down='blue.png')
        btn2 = Button(background_normal='yellow.png', on_press=lambda x: set_screen('yellowadult'),
                      background_down='blue.png')
        btn3 = Button(background_normal='green.png', on_press=lambda x: set_screen('greenadult'),
                      background_down='blue.png')
        btn4 = Button(background_normal='white.png', on_press=lambda x: set_screen('whiteadult'),
                      background_down='blue.png')
        btn5 = Button(background_normal='blue.png', on_press=lambda x: set_screen('blueadult'),
                      background_down='blue.png')
        btn6 = Button(background_normal='brown.png', on_press=lambda x: set_screen('brownadult'),
                      background_down='blue.png')
        btn7 = Button(background_normal='puple.png', on_press=lambda x: set_screen('pupleadult'),
                      background_down='blue.png')
        btn8 = Button(background_normal='pink.png', on_press=lambda x: set_screen('pinkadult'),
                      background_down='blue.png')
        btn9 = Button(background_normal='black.png', on_press=lambda x: set_screen('blackadult'),
                      background_down='blue.png')
        btn10 = Button(background_normal='orange.png', on_press=lambda x: set_screen('orangeadult'),
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
        layout.add_widget(btn10)

        box2.add_widget(layout)
        layout_base.add_widget(box1)
        layout_base.add_widget(box2)

        self.add_widget(layout_base)


# страница открывается, когда с третьего листа нажимают - с детьми
class FilmNoAdult(Screen):
    def __init__(self, **kw):
        super(FilmNoAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        label0 = Label(text='Выберите цвет по настроению', font_size='12sp', halign='center')
        btn_test = Button(background_normal='basic_back.png', size_hint_x=.2, on_press=lambda x: set_screen('ListTwo'))
        background = Image(source='background.png', allow_stretch=True, keep_ratio=False)

        box1 = BoxLayout(size_hint=(1, .05),
                         orientation='horizontal')  # слой с текстом описания фильма и кнопкой назад

        box1.add_widget(label0)
        box1.add_widget(btn_test)

        box2 = FloatLayout()
        box2.add_widget(background)

        layout_base = BoxLayout(orientation='vertical')
        # Создаем слой с 9 изображениями-ссылками
        layout = GridLayout(cols=1, padding=[70, 70, 70, 70], spacing=5)
        btn1 = Button(background_normal='yellow.png', on_press=lambda x: set_screen('yellownoadult'),
                      background_down='blue.png')
        btn2 = Button(background_normal='green.png', on_press=lambda x: set_screen('greennoadult'),
                      background_down='blue.png')
        btn3 = Button(background_normal='orange.png', on_press=lambda x: set_screen('orangenoadult'),
                      background_down='blue.png')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        box2.add_widget(layout)
        layout_base.add_widget(box1)
        layout_base.add_widget(box2)
        self.add_widget(layout_base)


# страница открывается, когда с листа с детьми нажимают на желтый квадрат
class YellowNoAdult(Screen):
    def __init__(self, **kw):
        super(YellowNoAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        #films_yellow_adult - список с фильмами которые выпадают при нажатии на ;tkne. кнопку на странице с детьми
        films_yellow_adult = ['bridge', 'fish', 'hobbit']
        film = random.choice(films_yellow_adult)
        set_screen(film)


# страница открывается, когда с листа с детьми нажимают на зеленый квадрат
class GreenNoAdult(Screen):
    def __init__(self, **kw):
        super(GreenNoAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        #films_green_adult - список с фильмами которые выпадают при нажатии на зеленую кнопку на странице с детьми
        films_green_adult = ['india', 'ironman', 'megamozg']
        film = random.choice(films_green_adult)
        set_screen(film)


# страница открывается, когда с листа с детьми нажимают на оранжевый квадрат
class OrangeNoAdult(Screen):
    def __init__(self, **kw):
        super(OrangeNoAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        #films_orange_adult- список с фильмами которые выпадают при нажатии на оранжевую кнопку на странице с детьми
        films_orange_adult = ['night', 'panda', 'pride']
        film = random.choice(films_orange_adult)
        set_screen(film)


#TODO: присвоисть каждому цвету выбор рандомного фильма
# страница открывается, когда с листа без детей нажимают на синий квадрат

# функция выдает рандомный детский фильм если кликнули на синий цвет
class DarkblueAdult(Screen):# функция выдает рандомный детский фильм если кликнули на оранжевый цвет
    def __init__(self, **kw):
        super(DarkblueAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_dark_adult - список с фильмами которые выпадают при нажатии на черную кнопку на странице без детей
        films_dark_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton',
                            'bigfish','bourn','bridge', ]
        film = random.choice(films_dark_adult)
        set_screen(film)


# функция выдает рандомный детский фильм если кликнули на желтый цвет
class YellowAdult(Screen):
    def __init__(self, **kw):
        super(YellowAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_yellow_adult - список с фильмами которые выпадают при нажатии на желтую кнопку на странице без детей
        films_yellow_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish',
                 'bourn', 'bridge', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_yellow_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на зеленый квадрат
class GreenAdult(Screen):
    def __init__(self, **kw):
        super(GreenAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_orange_adult - список с фильмами которые выпадают при нажатии на зеленую кнопку на странице без детей
        films_green_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish',
                 'bourn', 'char', 'cityvor', 'coll', 'cool', 'craft', 'crash', 'crazy', 'dark', 'darkfields',
                 'darko', 'dep', 'henkok', 'here', 'hobbit', 'holidays', 'home', 'imperator', 'india', 'ironman',
                 'killbill', 'king', 'land', 'legend', 'mad', 'manon', 'megamozg', 'mert', 'million', 'mindhunters',
                 'mirrors', 'monstro', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_green_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на белый квадрат
class WhiteAdult(Screen):
    def __init__(self, **kw):
        super(WhiteAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_white_adult - список с фильмами которые выпадают при нажатии на белую кнопку на странице без детей
        films_white_adult = ['adven', 'artist', 'char', 'cityvor', 'coll', 'cool', 'craft', 'crash', 'crazy', 'dark', 'darkfields',
                 'darko', 'dep', 'dragon', 'equ', 'expend', 'expendtwo', 'fish', 'fury', 'glad', 'gonebabygone', 'gray',
                 'greenmil']
        film = random.choice(films_white_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на голубой квадрат
class BlueAdult(Screen):
    def __init__(self, **kw):
        super(BlueAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_blue_adult - список с фильмами которые выпадают при нажатии на голубую кнопку на странице без детей
        films_blue_adult = ['pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_blue_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на коричневый квадрат
class BrownAdult(Screen):
    def __init__(self, **kw):
        super(BrownAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_brown_adult - список с фильмами которые выпадают при нажатии на коричневую кнопку на странице без детей
        films_brown_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish',
                 'bourn',
                 'bridge', 'ceti', 'char', 'cityvor', 'coll','megamozg', 'mert', 'million', 'mindhunters',
                 'mirrors', 'monstro', 'nebo', 'night', 'lovewith', 'noeye', 'oceans', 'ocoboe', 'oper', 'panda',
                 'paris', 'pch', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_brown_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на фиолетовый квадрат
class PupleAdult(Screen):
    def __init__(self, **kw):
        super(PupleAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_purple_adult - список с фильмами которые выпадают при нажатии на феолетовую кнопку на странице без детей
        films_puple_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish',
                 'bourn',
                 'bridge', 'ceti', 'char', 'cityvor', 'coll', 'cool', 'craft', 'crash', 'crazy', 'dark', 'darkfields',
                 'darko', 'dep', 'dragon', 'equ', 'expend', 'expendtwo', 'fish', 'fury', 'glad', 'gonebabygone', 'gray',
                 'greenmil', 'hard', 'henkok', 'here', 'hobbit', 'holidays', 'home', 'imperator', 'india', 'ironman',
                 'killbill', 'king', 'land', 'legend', 'mad', 'manon', 'megamozg', 'mert', 'million', 'mindhunters',
                 'mirrors', 'monstro', 'nebo', 'night', 'lovewith', 'noeye', 'oceans', 'ocoboe', 'oper', 'panda',
                 'paris', 'pch', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_puple_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на розовый квадрат
class PinkAdult(Screen):
    def __init__(self, **kw):
        super(PinkAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        # films_pink_adult - список с фильмами которые выпадают при нажатии на розовую кнопку на странице без детей
        films_pink_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish',
                 'bourn',
                 'bridge', 'ceti', 'char', 'cityvor', 'coll', 'cool', 'craft', 'crash', 'crazy', 'dark', 'darkfields',
                 'darko', 'dep', 'dragon', 'equ', 'expend', 'expendtwo', 'fish', 'fury', 'glad', 'gonebabygone', 'gray',
                 'greenmil', 'hard', 'henkok', 'here', 'hobbit', 'holidays', 'home', 'imperator', 'india', 'ironman',
                 'killbill', 'king', 'land', 'legend', 'mad', 'manon', 'megamozg', 'mert', 'million', 'mindhunters',
                 'mirrors', 'monstro', 'nebo', 'night', 'lovewith', 'noeye', 'oceans', 'ocoboe', 'oper', 'panda',
                 'paris', 'pch', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_pink_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на черный квадрат
class BlackAdult(Screen):
    def __init__(self, **kw):
        super(BlackAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        #films_black_adult - список с фильмами которые выпадают при нажатии на черную кнопку на странице без детей
        films_black_adult = ['adven', 'artist', 'astral', 'badboy', 'banzaizny', 'batman', 'batmanbegin', 'baton', 'bigfish',
                 'bourn',
                 'bridge', 'ceti', 'char', 'cityvor', 'coll', 'cool', 'craft', 'crash', 'crazy', 'dark', 'darkfields',
                 'darko', 'dep', 'dragon', 'equ', 'expend', 'expendtwo', 'fish', 'fury', 'glad', 'gonebabygone', 'gray',
                 'greenmil', 'hard', 'henkok', 'here', 'hobbit', 'holidays', 'home', 'imperator', 'india', 'ironman',
                 'killbill', 'king', 'land', 'legend', 'mad', 'manon', 'megamozg', 'mert', 'million', 'mindhunters',
                 'mirrors', 'monstro', 'nebo', 'night', 'lovewith', 'noeye', 'oceans', 'ocoboe', 'oper', 'panda',
                 'paris', 'pch', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',
                 'ratata']
        film = random.choice(films_black_adult)
        set_screen(film)


# страница открывается, когда с листа без детей нажимают на оранжевый квадрат
class OrangeAdult(Screen):
    def __init__(self, **kw):
        super(OrangeAdult, self).__init__(**kw)

    def on_enter(self):  # Будет вызвана в момент открытия экрана
        #films_orange_adult - список с фильмами которые выпадают при нажатии на оранжевуб кнопку на странице без детей
        films_orange_adult = ['adven', 'artist', 'astral', 'badboy', 'batman', 'batmanbegin', 'baton', 'bourn',
                 'bridge', 'ceti', 'char', 'cityvor','craft', 'crash', 'crazy', 'dark', 'darkfields',
                 'darko', 'dep', 'dragon', 'equ', 'expend', 'expendtwo',  'fury', 'glad', 'gonebabygone', 'gray',
                 'greenmil', 'hard', 'henkok', 'here',   'home', 'imperator', 'india', 'ironman',
                 'killbill', 'king', 'land', 'legend', 'mad', 'manon',  'mert', 'million', 'mindhunters',
                 'mirrors', 'monstro', 'nebo', 'night', 'lovewith', 'noeye', 'oceans', 'ocoboe', 'oper',
                 'paris', 'pch', 'planeta', 'pras', 'pravoonkill', 'prestish', 'pride', 'prit', 'pyli', 'raid',]
        film = random.choice(films_orange_adult)
        set_screen(film)


def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(ListOne(name='ListOne'))
sm.add_widget(ListTwo(name='ListTwo'))
sm.add_widget(ListTree(name='ListTree'))
sm.add_widget(Rand(name='rand'))

sm.add_widget(Adven(name='adven'))
sm.add_widget(Artist(name='artist'))
sm.add_widget(Astral(name='astral'))
sm.add_widget(Badboys(name='badboys'))
sm.add_widget(Bandaizny(name='bandaizny'))
sm.add_widget(Batman(name='batman'))
sm.add_widget(Batmanbegin(name='batmanbegin'))
sm.add_widget(Baton(name='baton'))
sm.add_widget(Bigfish(name='bigfish'))
sm.add_widget(Bourn(name='bourn'))
sm.add_widget(Bridge(name='bridge'))
sm.add_widget(Ceti(name='ceti'))
sm.add_widget(Char(name='char'))
sm.add_widget(Cityvor(name='cityvor'))
sm.add_widget(Coll(name='coll'))
sm.add_widget(Cool(name='cool'))
sm.add_widget(Craft(name='craft'))
sm.add_widget(Crash(name='crash'))
sm.add_widget(Crazy(name='crazy'))
sm.add_widget(Dark(name='dark'))
sm.add_widget(Darkfields(name='darkfields'))
sm.add_widget(Darko(name='darko'))
sm.add_widget(Dep(name='dep'))
sm.add_widget(Dragon(name='dragon'))
sm.add_widget(Equ(name='equ'))
sm.add_widget(Expend(name='expend'))
sm.add_widget(Expendtwo(name='expendtwo'))
sm.add_widget(Fish(name='fish'))
sm.add_widget(Fury(name='fury'))
sm.add_widget(Glad(name='glad'))
sm.add_widget(Gonebabygone(name='gonebabygone'))
sm.add_widget(Gray(name='gray'))
sm.add_widget(Greenmil(name='greenmil'))
sm.add_widget(Hard(name='hard'))
sm.add_widget(Henkok(name='henkok'))
sm.add_widget(Here(name='here'))
sm.add_widget(Hobbit(name='hobbit'))
sm.add_widget(Holidays(name='holidays'))
sm.add_widget(Imperator(name='imperator'))
sm.add_widget(India(name='india'))
sm.add_widget(Ironman(name='ironman'))
sm.add_widget(Killbill(name='killbill'))
sm.add_widget(King(name='king'))
sm.add_widget(Land(name='land'))
sm.add_widget(Legend(name='legend'))
sm.add_widget(Mad(name='mad'))
sm.add_widget(Manon(name='manon'))
sm.add_widget(Megamozg(name='megamozg'))
sm.add_widget(Mert(name='mert'))
sm.add_widget(Million(name='million'))
sm.add_widget(Mindhunters(name='mindhunters'))
sm.add_widget(Mirrors(name='mirrors'))
sm.add_widget(Monstro(name='Monstro'))
sm.add_widget(Nebo(name='nebo'))
sm.add_widget(Night(name='night'))
sm.add_widget(Lovewith(name='lovewith'))
sm.add_widget(Noeye(name='noeye'))
sm.add_widget(Oceans(name='oceans'))
sm.add_widget(Ocoboe(name='ocoboe'))
sm.add_widget(Oper(name='oper'))
sm.add_widget(Panda(name='panda'))
sm.add_widget(Paris(name='paris'))
sm.add_widget(Pch(name='pch'))
sm.add_widget(Planeta(name='planeta'))
sm.add_widget(Pras(name='pras'))
sm.add_widget(Pravoonkill(name='pravoonkill'))
sm.add_widget(Prestish(name='prestish'))
sm.add_widget(Pride(name='pride'))
sm.add_widget(Prit(name='prit'))
sm.add_widget(Pyli(name='pyli'))
sm.add_widget(Raid(name='raid'))
sm.add_widget(Ratata(name='ratata'))

sm.add_widget(Darkfields(name='darkfields'))
sm.add_widget(Expend(name='expend'))
sm.add_widget(Here(name='here'))
sm.add_widget(Imperator(name='imperator'))
sm.add_widget(Lovewith(name='lovewith'))
sm.add_widget(Noeye(name='noeye'))
sm.add_widget(Raid(name='raid'))

sm.add_widget(FilmAdult(name='filmadult'))
sm.add_widget(FilmNoAdult(name='filmnoadult'))
sm.add_widget(YellowNoAdult(name='yellownoadult'))
sm.add_widget(GreenNoAdult(name='greennoadult'))
sm.add_widget(OrangeNoAdult(name='orangenoadult'))
sm.add_widget(DarkblueAdult(name='darkblueadult'))
sm.add_widget(YellowAdult(name='yellowadult'))
sm.add_widget(GreenAdult(name='greenadult'))
sm.add_widget(WhiteAdult(name='whiteadult'))
sm.add_widget(BlueAdult(name='blueadult'))
sm.add_widget(BrownAdult(name='brownadult'))
sm.add_widget(PupleAdult(name='pupleadult'))
sm.add_widget(PinkAdult(name='pinkadult'))
sm.add_widget(BlackAdult(name='blackadult'))
sm.add_widget(OrangeAdult(name='orangeadult'))


#класс для запуска приложение, как будет называться этот класс, то имя будет отображено вверху экрана при запуске приложения
class OneApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    OneApp().run()
