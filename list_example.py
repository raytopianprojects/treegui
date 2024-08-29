import direct.directbase.DirectStart
"""
    Window examle show how to get a single window on screen
"""
from gui.core import GUI
from gui.theme import Theme
from gui.controls import SelectList,Form,Vec2,VScroll
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
        Form.__init__(self,"Simple window",pos=Vec2(45,45),size=Vec2(200,400))
        
        # generate some random options
        options = ["option #%i"%i for i in range(38)]            
        
        # create a options list
        self.add(SelectList(options,pos=Vec2(10,30),size=Vec2(180,170)))
        
        # add FreeFloating form to the gui
        gui.add(self) 
        
# create the form
FreeFloating()
run()