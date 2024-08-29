import direct.directbase.DirectStart

"""
    Window examle show how to get a single window on screen
"""
from gui.core import GUI
from gui.theme import Theme
from gui.controls import Form, Vec2

base.disableMouse()

# create main gui class
GUI(theme=Theme("data/affgui.png"))


class FreeFloating(Form):
    """ 
        this is a free floating form on which to put
        widgits or controls  
    
    """

    def __init__(self):
        # call the super constructor 
        # all gui objects take pos and size as attributes 
        # and many also take default text as the first operand
        Form.__init__(self, "Simple window", pos=Vec2(45, 45), size=Vec2(200, 400))
        # adds window to the gui - 
        # you can add windows to most container objects
        gui.add(self)

    # create the form


FreeFloating()
run()
