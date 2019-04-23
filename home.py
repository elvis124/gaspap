#importing all the modules needed to run functions
from kivy.app import App
from kivy.config import Config
Config.set('input', 'multitouchscreen1', 'tuio,192.168.2.22:3306')
Config.set('postproc','desktop','1')
Config.set('kivy','exit_on_escape','1')
Config.set('kivy','log_enable','1')
Config.set('kivy', 'log_maxfiles', '-1')
Config.set('widgets', 'scroll_friction','float')
Config.set('widgets', 'scroll_distance', '4')
Config.set('graphics','borderless','0')
Config.set('graphics','rotation','0')
Config.set('graphics','full_screen','1')
Config.set('graphics','allow_screensaver','1')
Config.set('graphics','kivy_clock','free_all')
Config.set('widgets', 'scroll_distance', '4')
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.spelling import SpellingBase
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
Window.clearcolor=(0,0,0,0)
from kivy.uix.checkbox import CheckBox
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.switch import Switch
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen,  TransitionBase
import os
import sys
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.listview import ListItemButton, ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.interactive import InteractiveLauncher
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image
from kivy.graphics import Color,Rectangle, Line
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix. behaviors import ButtonBehavior
from kivy.uix.actionbar import ActionBar,ActionView,ActionGroup,ActionButton,ActionPrevious, ActionView,ActionOverflow, ContextualActionView
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.loader import Loader
from kivy.support import install_twisted_reactor
from kivy.adapters.models import SelectableDataItem
from kivy.storage.jsonstore import JsonStore
from kivy.uix.dropdown import DropDown
from kivy.graphics import Line, SmoothLine
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from kivy.uix.spinner import Spinner
from kivy.base import EventLoop
from kivy.factory import Factory
EventLoop.window.title = 'G-Pap'
from kivy.loader import Loader
#class for managing the orders
class OrderingScreen(Screen):
    def __init__(self, **kwargs):
        super(OrderingScreen, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(0,0,0,1)
            self.rect = Rectangle(size=self.size, pos=self.pos, source='icons/first.png')
    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
    def search(self,*args):
        for index in range(20000):
            btn = Button(text='Shops: &d' %index, size_hint=(1, .05))

            self.ids['displayofshops'].add_widget(btn)

    
#class used to manage the login screen
class Homelogin(Screen):
    def __init__(self, **kwargs):
        super(Homelogin, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(0,0,0,1)
            self.rect = Rectangle(size=self.size, pos=self.pos, source='icons/first.png')
    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
    def regitser(self, *args):
        self.grid = GridLayout(size_hint=(1,1), cols=1,rows=3, orientation='vertical')
        self.gridd = GridLayout(size_hint=(1, .2), cols=1)
        self.griidd = GridLayout(size_hint=(1, .2), cols=1)
        self.label = Label(text='to order gas click customer', color=[.0, .4, .4, 1])
        self.label2 = Label(text='to register outlet click shop', color=[.0, .4, .4, 1])
        self.gridd.add_widget(self.label)
        self.gridd.add_widget(self.label2)
        self.content = StackLayout(orientation='lr-tb', cols=2, size_hint=(1, .4))
        self.but = Button(text='customer', size_hint=(.5, .3),background_color=[.0, .4, .4,1], font_size=16,on_press=self.customer )
        self.butt = Button(text='shop', size_hint=(.5, .3),background_color=[.0, .4, .4,1],font_size=16, on_press=self.shop)
        self.grid.add_widget(self.gridd)
        self.grid.add_widget(self.griidd)
        self.grid.add_widget(self.content)
        self.content.add_widget(self.but)
        self.content.add_widget(self.butt)
        self.pop = Popup(title='Registration',title_color=[.0, .4, .4,1], auto_dismiss=False,title_align='center',separator_color=[.0, .4, .4,1],title_font='Roboto',content=self.grid, size_hint=(.5, .5))
        self.pop.open()
        Clock.schedule_once(self.pop.dismiss, 10)
    def customer(self, *args):
        self.pop.dismiss()
        self.manager.current='customerregistry'
    def shop(self, *args):
        self.pop.dismiss()
        self.manager.current='shopregister'
    def cancel(self, *args):
        self.pop.dismiss()
    def loginhome(self, *args):
        sm = Screenmanager()
        sm.transition.direction='center'
        self.manager.current='customerordering'
    def order(self, *args):
        self.manager.current='orderingscreen'
#class for registering the customers
class CustomerRegister(Screen):
    def __init__(self, **kwargs):
        super(CustomerRegister, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(0,0,0,0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
    def register(self, *args):
        print('hallow')
    def back(self, *args):
        self.manager.current='loginscreen'

#class for registering the shops
class ShopRegister(Screen):
    def __init__(self, **kwargs):
        super(ShopRegister, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(0,0,0,0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
    def register(self, *args):
        print('hallow')
    def back(self, *args):
        self.manager.current='loginscreen'
#class for odering 
class Shopmanager(Screen):
    def __init__(self, **kwargs):
        super(Shopmanager, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(0,0,0,0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
#class for managing the screens
class Screenmanager(ScreenManager):
    pass


kv_file = Builder.load_file('home.kv')
#class for compling the app
class G_papApp(App):
    def build(self, *args):
        self.title='G-Pap'
        self.icon='icons/th.jpg'
        self.use_kivy_settings=False
        return kv_file


if __name__=='__main__':
    G_papApp().run()
