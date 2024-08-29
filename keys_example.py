import direct.directbase.DirectStart
"""
    because the gui system overrides some of the keys 
    it has a option to use a key configuraiton file
    you will find said file in the data keys.config
"""
from gui.core import GUI
from gui.keys import Keys
from gui.theme import Theme
from gui.controls import Lable,Vec2
base.disableMouse()

# the main key file it will route magic_key and other_key events
keys = Keys("data/keys.config")

# create main gui class passing it keys
GUI(keys=keys,theme=Theme("data/affgui.png"))

l = Lable('press A or B',pos=Vec2(200,200))

# create some functions to print out stuff
def magicKey():
    l.setText("""press A or B
        magic key pressed 
        (read viea the magic_key event mapping 
         in the  data/key.config) """)

# create some functions to print out stuff
def otherKey():
    l.setText("""press A or B
        other key pressed 
        (read viea the other_key event mapping 
         in the  data/key.config) """)

base.accept('magic_key',magicKey)
base.accept('other_key',otherKey)

gui.add(l)

run()