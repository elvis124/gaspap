#importing all the modules needed to run functions
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'multisamples', '1')
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
from easygui import msgbox
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
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
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.graphics.vertex_instructions import RoundedRectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.interactive import InteractiveLauncher
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.core.image import Image
from kivy.graphics import Color,Rectangle, Line
from kivy.uix.listview import ListItemButton, ListView, ListItemLabel
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
from kivy.storage.jsonstore import JsonStore
EventLoop.window.title = 'G-Pap'
from kivy.loader import Loader
from kivy.uix.modalview import ModalView
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton
from kivy.uix.spinner import Spinner
import MySQLdb

host='127.0.0.1'
port=3306 
user='root'
password='binoctal'

#class for managing the orders
class OrderingScreen(Screen):
    def __init__(self, **kwargs):
        super(OrderingScreen, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(0,0,0,1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
    def search(self,*args):
        self.manager.current='search'
        connection = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
        conn = connection.cursor()
        ttype = self.ids['n_type'].text 
        weight = self.ids['weight'].text 
        units= self.ids['units'].text
        location=self.ids['where_to'].text
        conn.execute("SELECT Shopname,Type,Weight,Price,location FROM stock WHERE Type=%s AND Weight=%s OR location=%s", [(ttype), (weight), (location)])
        if conn:
            self.row = conn.fetchall()
            for rows in self.row:
                for cols in rows:
                    self.label = Button(text='%s'%cols, size_hint=(.2, .2))
                    self.ids['displays'].add_widget(self.label)
        else:
            self.label = Label(text='no result found')
            self.ids['displays'].add_widget(self.label)


    def activity_search(self, *args):
        print('nice things')

#class for searching

class Search(Screen):
    def __init__(self, **kwargs):
        super(Search, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos


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
        self.label = Label(text='to order gas click customer', underline=True, color=[.0, .4, .4, 1])
        self.label2 = Label(text='to register outlet click shop',underline=True,  color=[.0, .4, .4, 1])
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
    def login(self, *args):
        self.number = self.ids['n_number'].text
        self.n_password = self.ids['n_password'].text
        connection = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
        conn = connection.cursor()
        if self.ids['n_number'].text=="" and self.ids['n_password'].text=="":
            pop = Popup(title='error', title_align='center',title_color=[.0, .4, .4,1],separator_color=[.0,.4,.4,1],content=Label(text='input empty', underline=True), size_hint=(.3, .2), background_color=[1,1,1,0])
            pop.open()
            Clock.schedule_once(pop.dismiss, 1)

        else:
            results = conn.execute("SELECT * FROM customers WHERE phone_number=%s AND password=%s", [(self.number), (self.n_password)])
            if results:
                self.manager.current='customerorderingscreen'
            else:
                shop_owner = conn.execute("SELECT  * FROM shopregistry WHERE phone_number=%s AND password=%s", [(self.number),(self.n_password)])
                if shop_owner:
                    store = JsonStore('shop.json')
                    store.put('details', password=str(self.n_password), phone_number=str(self.number))
                    self.manager.current='shopmanagement'
                else:
                    self.grid=GridLayout(cols=1, size=self.size, pos=self.pos)
                    self.lb = Label(text='Reset password ')
                    self.ll = Label(text='otherwise signup')
                    self.grid.add_widget(self.lb)
                    self.grid.add_widget(self.ll)
                    self.pop = Popup(title='wrong details provided !!!', title_align='center',auto_dismiss=False,separator_color=[.0,.4,.4,1], title_color=[.0,.4,.4,1], content=self.grid,  size_hint=(.3, .2))
                    self.pop.open()
                    Clock.schedule_once(self.pop.dismiss, 2)

    def password(self, *args):
        self.grid = GridLayout(size_hint=(1, 1), background_color=[0,1,0,1],cols=1, orientation='vertical')
        self.textpas = TextInput(hint_text='email address', border=[0,1,0,1])
        self.butt = Button(text='continue', background_color=[.0,.4,.4,1], on_press=self.n_password)
        self.grid.add_widget(self.textpas)
        self.grid.add_widget(self.butt)
        self.p = Popup(title='password Recovery', title_align='center', title_color=[0,1,0,1], auto_dismiss=True, content=self.grid, size_hint=(.5, .2))
        self.p.open()
    def n_password(self, *args):
        self.p.dismiss()
        self.pemail = self.textpas.text
        connection = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
        conn = connection.cursor()
        e=conn.execute(" " "SELECT password FROM customers WHERE email_address=%s" " ", (self.pemail,))
        if e:
            self.content = Label(text='pass--->:  %s' %e )
            self.po =Popup(title='Here is your password', title_align='center', title_color=[.0,.4,.4,1],content=self.content, size_hint=(.4, .3))
            self.po.open()
            Clock.schedule_once(self.po.dismiss, 10)
        else:
            d = conn.execute(" " "SELECT password FROM shopregistry WHERE email_address=%s" " ", (self.pemail,))
            if d:
                self.content = Label(text='pass-->:  %s' %d )
                self.po =Popup(title='Here is your password', title_align='center', title_color=[.0,.4,.4,1],content=self.content, size_hint=(.4, .3))
                self.po.open()
                Clock.schedule_once(self.po.dismiss, 10)
            else:
                self.grid =GridLayout(size_hint=(1,1), cols=1,size=self.size, pos=self.pos)
                self.label=Label(text='Your email address')
                self.label2 = Label(text='was wrong,try again')
                self.grid.add_widget(self.label)
                self.grid.add_widget(self.label2)
                self.pas = Popup(title='error', title_align='center', content=self.grid, size_hint=(.5, .2), background_color=[1,1,1,0])
                self.pas.open()
                Clock.schedule_once(self.pas.dismiss, 2)



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
        if self.ids['n_password'].text==self.ids['n_confirm_password'].text:
            connection = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
            conn = connection.cursor()
            conn.execute("CREATE TABLE IF NOT EXISTS customers(id INT PRIMARY KEY AUTO_INCREMENT, phone_number varchar(30), email_address varchar(45) ,password varchar(30), confirm_password varchar(30))")
            conn.execute("INSERT INTO customers VALUES (%s, %s,%s,%s)",[self.ids['n_phone_number'].text, self.ids['n_email_address'].text, self.ids['n_password'].text, self.ids['n_confirm_password'].text])
            connection.commit()
            self.pop = Popup(title='succesfull', title_color=[.0,.4,.4,1],separator_color=[.0, .4, .4,1], content=Label(text='succcefull', font_size=20,color=[0,1,0,1]), size_hint=(.3, .2))
            self.pop.open()
            self.manager.current='loginscreen'
            Clock.schedule_once(self.pop.dismiss, 2)
        else:
            self.pp = Popup(title='error', title_align='center',separator_color=[.0, .4, .4,1], content=Label(text='passwords do not match',font_size=20, color=[0,1,0,1]), size_hint=(.3, .2))
            self.pp.open()
            Clock.schedule_once(self.pp.dismiss, 2)
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
        if self.ids['n_password'].text==self.ids['n_confirm_password'].text:
            connection = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
            conn = connection.cursor()
            conn.execute("CREATE TABLE IF NOT EXISTS shopregistry (id INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,shopname varchar(40), shop_owner varchar(30), email_address varchar(30), phone_number varchar(20), country varchar(30), county  varchar(20), consituency varchar(30), ward varchar(45), password varchar(20))")
            conn.execute("INSERT INTO shopregistry VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",[self.ids['n_shop_name'].text, self.ids['n_shop_owner'].text, self.ids['n_email_address'].text, self.ids['n_phone_number'].text, self.ids['n_country'].text, self.ids['n_county'].text, self.ids['n_consituency'].text, self.ids['n_ward'].text, self.ids['n_password'].text])
            connection.commit()
            self.pop = Popup(title='succesfull', title_color=[.0,.4,.4,1],separator_color=[.0, .4, .4,1], content=Label(text='Welcome', font_size=20,color=[0,1,0,1]), size_hint=(.3, .2))
            self.pop.open()
            self.manager.current='loginscreen'
            Clock.schedule_once(self.pop.dismiss, 3)
        else:
            self.pp = Popup(title='error', title_align='center',separator_color=[.0, .4, .4,1], content=Label(text='passwords do not match',font_size=20, color=[0,1,0,1]), size_hint=(.3, .2))
            self.pp.open()
            Clock.schedule_once(self.pp.dismiss, 2)

    def back(self, *args):
        self.manager.current='loginscreen'
#class for selctable buttons
class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def on_press(self):
        popup = TextInputPopup(self)
        popup.open()

    def update_changes(self, txt):
        self.text = txt

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
      pass



class Grid1(GridLayout):
    def __init__(self, **kwargs):
        super(Grid1, self). __init__(**kwargs)
        self.bind(minimum_height = self.setter('height'))


class Grid2(GridLayout):
    def __init__(self, **kwargs):
        super(Grid2, self). __init__(**kwargs)
        self.bind(minimum_height = self.setter('height'))


class Grid3(GridLayout):
    def __init__(self, **kwargs):
        super(Grid3, self). __init__(**kwargs)
        self.bind(minimum_height = self.setter('height'))

    

class Grid4(GridLayout):
    def __init__(self, **kwargs):
        super(Grid4, self). __init__(**kwargs)
        self.bind(minimum_height = self.setter('height'))




#class for shop manager
class ShopManager(Screen):
    listitems = ListProperty([])
    def __init__(self, **kwargs):
        super(ShopManager, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before: 
            Color(0,0,0,0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
    def _update_rec(self, *args):
        self.rect.size=self.size
        self.rect.pos = self.pos
    def orders(self, *args):
        self.ids['orderbuttons'].clear_widgets()
        self.label = Button(text='Click here to view order and refresh',on_press=self.orderss,size_hint=(.1, .1), color=[0,1,0,1])
        self.ids['orderbuttons'].add_widget(self.label)
    def stock(self, *args):
        self.ids['orderbuttons'].clear_widgets()
        self.butt = Button(text='Add stock', size_hint=[.1, .1],on_press=self.add_stock,color=[0,1,0,1])
        self.ids['orderbuttons'].add_widget(self.butt)
        self.tt = Button(text='update_stock', size_hint=(.1,.1),on_press=self.update_stock, color=[0,1,0,1])
        self.ids['orderbuttons'].add_widget(self.tt)


    def add_stock(self, *args):
        self.ids['screenlayout'].clear_widgets()
        self.stack = StackLayout(orientation='tb-lr', size_hint=(1, .3), spacing=9,padding=10, size=self.size, pos=self.pos, cols=1)
        self.grid=GridLayout(orientation='vertical', cols=1, size_hint=(1, .1))
        self.type = TextInput(hint_text='Type(example Total', size_hint=(1, .1))
        self.weight = TextInput(hint_text='weight(example 30kg)', size_hint=(1, .1))
        self.price = TextInput(hint_text='price', size_hint=(1, .1))
        self.units = TextInput(hint_text='units(example 20 of them)', size_hint=(1, .1))
        self.sbut = Button(id='button1',text='Add', size_hint=(1,.1), on_press=self.add)
        self.stack.add_widget(self.grid)
        self.stack.add_widget(self.type)
        self.stack.add_widget(self.weight)
        self.stack.add_widget(self.price)
        self.stack.add_widget(self.units)
        self.stack.add_widget(self.sbut)
        self.ids['screenlayout'].add_widget(self.stack)

        
    def add(self, value, *args):
        store = JsonStore('shop.json')
        self.nn_number =str(store.get('details')['phone_number'])
        self.nn_password =str(store.get('details')['password'])
        connection  = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
        conn = connection.cursor()
        if self.type.text=='':
            self.pop = Popup(title='! error; no input ',separator_color=[.0,.4,.4,1], title_color=[.0,.4,.4,1], content=Label(text='Type empty', color=[0,1,0,1]), size_hint=(.2,.2))
            self.pop.open()
            Clock.schedule_once(self.pop.dismiss, 2)
        elif self.weight.text=='':
            self.pop = Popup(title='! error; no input ',separator_color=[.0,.4,.4,1], title_color=[.0,.4,.4,1], content=Label(text='Weight empty', color=[0,1,0,1]), size_hint=(.2,.2))
            self.pop.open()
            Clock.schedule_once(self.pop.dismiss, 2)
        elif self.price.text=='':
            self.pop = Popup(title='! error; no input ',separator_color=[.0,.4,.4,1], title_color=[.0,.4,.4,1], content=Label(text='Price empty', color=[0,1,0,1]), size_hint=(.2,.2))
            self.pop.open()
            Clock.schedule_once(self.pop.dismiss,2)
        elif self.units.text=='':
            self.pop = Popup(title='! error; no input ',separator_color=[.0,.4,.4,1], title_color=[.0,.4,.4,1], content=Label(text='Units empty', color=[0,1,0,1]), size_hint=(.2,.2))
            self.pop.open()
            Clock.schedule_once(self.pop.dismiss, 2)
        elif True:
            self.shop_name = conn.execute(" SELECT shop_name FROM shopregistry WHERE phone_number=%s AND password=%s", [(self.nn_number), (self.nn_password)])
            self.ward = conn.execute(" SELECT ward FROM shopregistry WHERE phone_number=%s AND password=%s" , [(self.nn_number), (self.nn_password)])
            print(self.shop_name + self.ward)
            conn.execute(" CREATE TABLE IF NOT EXISTS stock(id INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,Shopname varchar(30) , location varchar(40), phone_number int(100) , Type varchar(30), Weight varchar(30), Price varchar(30), units varchar(40) )")
            conn.execute("INSERT INTO stock(Shopname, location,phone_number, Type,Weight, Price,units) VALUES (%s,%s,%s,%s,%s,%s,%s)",[self.shop_name,self.ward,self.nn_number,self.type.text,self.weight.text,self.price.text,self.units.text])
            connection.commit()
            text = 'Added'
            value.text=text
            value.background_color=(0,1,0,1)
            self.pop = Popup(title='Added',separator_color=[.0,.4,.4,1], title_color=[.0,.4,.4,1], content=Label(text='Added to your stock', color=[0,1,0,1]),background_color=[1,1,1,0], size_hint=(.5,.2))
            self.pop.open()
            Clock.schedule_once(self.pop.dismiss, 1)
            self.type.text=''
            self.weight.text=''
            self.price.text=''
            self.units.text=''
            text = 'Add'
            value.text=text
            value.background_color=(1,1,1,1)
    def update_stock(self, *args):
        self.ids['screenlayout'].clear_widgets()

        store = JsonStore('shop.json')
        self.nn_number =str(store.get('details')['phone_number'])
        connection  = MySQLdb.connect(host=host, port=port, user=user, password=password, db='Registredcustomer')
        conn = connection.cursor()


        self.grid = GridLayout(cols=4, size=self.size, pos=self.pos)
        self.ids['screenlayout'].add_widget(self.grid)


        self.stack1 = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), padding=5)
        self.grid.add_widget(self.stack1) 
        self.stack2 = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),padding=5)
        self.grid.add_widget(self.stack2)
        self.stack3  = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),padding=5)
        self.grid.add_widget(self.stack3)
        self.stack4  = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),padding=5)
        self.grid.add_widget(self.stack4)

        self.stack11 = Grid1(cols=1, orientation='vertical', spacing=5,size_hint=(1, 1))
        self.stack1.add_widget(self.stack11)
        self.stack22 = Grid2(cols=1, orientation='vertical',spacing=5, size_hint=(1, 1))
        self.stack2.add_widget(self.stack22)
        self.stack33  = Grid3(cols=1, orientation='vertical',spacing=5, size_hint=(1, 1))
        self.stack3.add_widget(self.stack33)
        self.stack44  = Grid4(cols=1, orientation='vertical',spacing=5, size_hint=(1, 1))
        self.stack4.add_widget(self.stack44)

        conn.execute("SELECT Type From stock WHERE phone_number=%s ", [(self.nn_number),])
        self.rows = conn.fetchall()
        for row in self.rows:
            for cols in row:
                self.but = Button(text='%s' %cols, size_hint=(.2, .2))
                self.stack11.add_widget(self.but)

        conn.execute("SELECT Weight From stock WHERE phone_number=%s ", [(self.nn_number),])
        self.rows = conn.fetchall()
        for row in self.rows:
            for cols in row:
                self.but = Button(text='%s' %cols, size_hint=(.2,.2))
                self.stack22.add_widget(self.but)

        conn.execute("SELECT Price From stock WHERE phone_number=%s ", [(self.nn_number),])
        self.rows = conn.fetchall()
        for row in self.rows:
            for cols in row:
                self.but = Button(text='%s' %cols, size_hint=(.2,.2))
                self.stack33.add_widget(self.but)

        conn.execute("SELECT units From stock WHERE phone_number=%s ", [(self.nn_number),])
        self.rows = conn.fetchall()
        for row in self.rows:
            for cols in row:
                self.but = Button(text='%s' %cols, size_hint=(.2, .2))
                self.stack44.add_widget(self.but)



        connection.commit()
    def orderss(self, *args):
        self.ids['screenlayout'].clear_widgets()
        for i in range(7):
            self.but = Button(text='disss', size_hint=(1, .2))
            self.ids['screenlayout'].add_widget(self.but)

    def logout(self, *args):
        self.manager.current='loginscreen'



#class for managing the screens
class Screenmanager(ScreenManager):
    pass

kv_file = Builder.load_file('home.kv')
#class for compling the app
class G_papApp(App):
    def build(self, *args):
        self.title='G-Pap'
        self.icon='first.jpg'
        self.use_kivy_settings=False
        return kv_file
    def order(self, *args):
        self.root.current='sendingorder'


if __name__=='__main__':
    G_papApp().run()











 