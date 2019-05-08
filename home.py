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
from kivy.uix.scrollview import ScrollView
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
        order = str(self.ids['n_type'].text +" "+ self.ids['weight'].text + " " + self.ids['units'] + " " + self.ids['where_to'].text)
        self.ids['displayofshops'].clear_widgets()
        self.ids['displayofshops'].adapter.data.extend(order)
        self.ids['displayofshops'].trigger_reset_populate()


    def n_type(self, *args):
        self.N_type = ScrollView(padding=4, do_scroll_y=True, do_scroll_x=True)
        self.box = BoxLayout(orientation='vertical', spacing=2)
        for i in ['hashi', 'Total','k-gas', 'dscujhw', 'dhbcweecw', 'xehwcuiwc', 'schui', 'ascscdwe', 'xaxwxd', 'sadqw', 'adqw','dqwdwq','dqwdqwed']:
            self.but = Button(text='%s'%i, on_press=self.nn_type, background_color=[1,1,1,0], color=[0,1,0,1])
            self.box.add_widget(self.but)
        self.N_type.add_widget(self.box)
        self.n = Popup(title='Type', title_align='center',title_color=[.0,.4,.4,1],separator_color=[.0,.4,.4,1], size_hint=(.3, .7), content=self.N_type, auto_dismiss=True, background_color=[1,1,1,0])
        self.n.open()
    def nn_type(self, *args):
        self.n.dismiss()
        self.ids['n_type'].text=self.but.text



         
#listitem button
class Listbutton(ListItemButton):
    def __init__(self, **kwargs):
        super(Listbutton, self). __init__(**kwargs)
        self.bind(size=self._update_rec, pos=self._update_rec)
        with self.canvas.before:
            Color(1,1,1,0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(on_press=self.order)
    def order(self, *args):
        self.grid = GridLayout(cols=1)
        self.l = Label(text='dfbhug')
        self.grid.add_widget(self.l)
        self.pop = Popup(title='Order', title_align='center',title_color=[.0,.4,.4,1],separator_color=[.9,.9,.9,1], content=self.grid, size_hint=(.7, .4))
        self.pop.open()
        Clock.schedule_once(self.pop.dismiss, 3)

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
            conn.execute("CREATE TABLE IF NOT EXISTS shopregistry (id INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,shopname varchar(22), shop_owner varchar(30), email_address varchar(30), phone_number varchar(20), country varchar(30), county  varchar(20), consituency varchar(30), ward varchar(30), password varchar(20))")
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
            conn.execute("INSERT INTO stock(Shopname, location,phone_number, Type,Weight, Price,units) VALUES (%s,%s,%s,%s,%s,%s,%s)",[self.shop_name, self.ward, self.nn_number, self.type.text, self.weight.text, self.price.text, self.units.text])
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
        conn.execute("SELECT Type, Weight,Price, units From stock WHERE phone_number=%s ", [(self.nn_number),])
        self.rows = conn.fetchall()
        for i in self.rows:
            for cols in i:
                self.listitems.append(cols)
        self.view = RecycleView(viewclass='SelectableButton', data=[{'text': str(x) for x in self.listitems}])
        self.select = SelectableRecycleGridLayout(cols=1, default_size=(1,1), default_size_hint=(1, None), size_hint_y=(None), orientation='vertical' , multiselect=True, touch_multiselect=True)
        self.view.add_widget(self.select)
        self.ids['screenlayout'].add_widget(self.view)

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











 