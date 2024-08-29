import direct.directbase.DirectStart
"""
    Window example show how to get a single window on screen
    and attach many different controls to it
"""
from gui.core import GUI
from themes.rtheme import RTheme
from gui.controls import *
base.disableMouse()

base.setFrameRateMeter(True)

# create main gui class
GUI(theme=RTheme("data/r.png"))


class SampleForm(Form):   
    
    def __init__(self):
        
        Form.__init__(self,"Simple Form",Vec2(100,100),Vec2(500,500))
        
        self.add(Lable("Apples:",pos=Vec2(0,40)))
        self.powerShields = self.add(Button("get some",pos=Vec2(80,40),onClick=self.buttonEvent));
        self.add(Lable("Orishes:",pos=Vec2(0,80)))
        self.powerWeapons = self.add(Button("peel",pos=Vec2(80,80),onClick=self.buttonEvent));
        self.add(Lable("Bananas:",pos=Vec2(0,120)))
        self.powerEngine = self.add(Button("throw",pos=Vec2(80,120),onClick=self.buttonEvent));
        self.add(Lable("Trees:",pos=Vec2(0,160)))
        self.powerHyper = self.add(Button("look at",pos=Vec2(80,160),onClick=self.buttonEvent));
        
        self.add(Radio("look for Elvis",pos=Vec2(0,200)));
        self.add(Radio("pizza",pos=Vec2(0,220)));
        self.add(Radio("think of food",pos=Vec2(0,240)));
        
        self.add(Check("confused",pos=Vec2(0,280)));
        self.add(Check("lazy",pos=Vec2(0,300)));
        self.add(Check("very breain dead...",pos=Vec2(0,320)));
 
        self.add(Input("type!",pos=Vec2(250,40),size=Vec2(200,20)));
        self.add(Password("more type!",pos=Vec2(250,80),size=Vec2(220,20)));
        self.add(Input("and type!",pos=Vec2(250,120),size=Vec2(250,20)));
        self.add(Input("here type!",pos=Vec2(250,160),size=Vec2(300,20)));
        
        f = self.add(Frame(pos=Vec2(250,220),size=Vec2(200,200)));
        f.add(Lable( open("controls_example.py").read()[0:300] ,pos=Vec2(0,0)))
        
        icon = self.add(Icon(pos=Vec2(50,380)));
        icon.size=Vec2(100,120)
        icon.skinType = "PANDA"
        icon.onClick = icon.onDrag
            
    def buttonEvent(self,button,key,mouse):
        gui.add(SampleForm())
        
# create the form
gui.add(SampleForm())
run()