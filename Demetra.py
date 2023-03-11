import time
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

# Declare both screens

kv = '''
StartScreen:   #Общий
        id:fl1
        orientation: 'vertical'
        canvas:
                Rectangle:
                        source: 'Fon.jpg'
                        size: self.size
                        pos: self.pos
        #rows: 6'''


class StartScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.wimage = Image(source="fon.png")
        self.layout.add_widget(self.wimage)

        self.label = Label(text='Settings Screen')
        self.layout.add_widget(self.label)

        self.button = Button(text='Go To Menu', size_hint=(.5, .10), pos=(20, 20))
        self.button.bind(on_press=self.change_screen)
        self.layout.add_widget(self.button)

    def change_screen(self, event):
        # sm.current = 'menu'
        self.manager.transition.direction = 'right'
        self.manager.transition.duration = 0.5  # 0.5 second
        self.manager.current = 'menu'


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout()
        self.add_widget(self.layout)

        # self.label = Label(text='Menu Screen', size_hint=(.5, .10), pos=(20, 20))
        # self.layout.add_widget(self.label)

        self.button = Button(text='Go To Timer', size_hint=(.5, .10), pos=(20, 20))
        self.button.bind(on_press=self.change_screen)
        self.layout.add_widget(self.button)

        self.button = Button(text='Go To StartScreen',
                             size_hint=(.5, .10), pos=(20, 20))
        self.button.bind(on_press=self.change_screen_start)
        self.layout.add_widget(self.button)

    def change_screen(self, event):
        # sm.current = 'settings'
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5  # 3 seconds
        self.manager.current = 'timer'

    def change_screen_start(self, event):
        # sm.current = 'settings'
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5  # 3 seconds
        self.manager.current = 'start'


class TimerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.count = 50000
        self.timer_started = False

        self.layout = BoxLayout()
        self.add_widget(self.layout)

        # self.label = Label(text='Menu Screen', size_hint=(.5, .10), pos=(20, 20))
        # self.layout.add_widget(self.label)

        self.button = Button(text='Start Timer', size_hint=(.15, .15), pos=(20, 20))
        self.button.bind(on_press=self.start_timer)
        self.layout.add_widget(self.button)

        self.button = Button(text='Go To Settings', size_hint=(.15, .15), pos=(20, 20))
        self.button.bind(on_press=self.change_screen)
        self.layout.add_widget(self.button)

    def start_timer(self, event):
        if not self.timer_started:
            self.myLabel = Label(text='Waiting for updates...',
                                 size_hint=(.15, .15), pos=(20, 500))
            Clock.schedule_interval(self.Callback_Clock, 1)
            self.layout.add_widget(self.myLabel)
            self.timer_started = True

            return self.myLabel

    def Callback_Clock(self, dt):
        self.count = self.count - 1
        self.myLabel.text = "Updated % d...times" % self.count

    def change_screen(self, event):
        # sm.current = 'settings'
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5  # 3 seconds
        self.manager.current = 'menu'


# Create the screen manager

sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(TimerScreen(name='timer'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    app = TestApp()
    TestApp().run()
