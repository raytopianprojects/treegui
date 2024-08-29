"""

    configure script for the UI

"""

class MainLayout:
    
    class GameMenu:
        pos = "left","top"
        size = 150,100
        style = "LIGHT_BLACK_BORDER" 
            
    class Chat:
        pos = "center","top"
        size = 500,150
        style = "DARK_BLACK_BORDER"
    
    class SmallChannelList:
        pos = "left of Chat","top"
        size = "grow till GameMenu","same as GameMenu"
        style = "MED_BLACK_BORDER"
        
    class Objective:
        pos = "right of Chat","top"
        size = "grow till Standing","same as GameMenu"
        style = "MED_BLACK_BORDER"
    
    class Standing:
        pos = "right","top"
        size = 150,"same as GameMenu"
        style = "LIGHT_BLACK_BORDER"
        
        class TotalStanding:
            pos = "left","top"
            size = 140,40
            type = "label"
            text = "0.0"
            style = "LIGHT_BLACK_BORDER"
            
        class DeltaStanding:
            pos = "left","bellow TotalStanding"
            size = 140,40
            type = "label"
            text = "0.0"
            style = "LIGHT_BLACK_BORDER"
       
    # --------------------------- top ---------------------------------   
       
       
    class ModeChanger:
        pos = "center","bottom"
        size = 200,25 
        style = "DARK_BLACK_BORDER"
        
    class ModeCommands:
        pos = "left","bottom"
        size = "grow till ModeChanger",25
        align = "right"
        style = "MED_BLACK_BORDER"
    
    class SelectionCommands:
        pos = "right","bottom"
        size = "grow till ModeChanger",25
        style = "MED_BLACK_BORDER"
        
    # expanded + fold out stuff    
        
    class ExpandedObjective:
        pos = "next to Objective","bellow Objective"
        size = 200,300
        hide = True
        style = "LIGHT_BLACK_BORDER"
        
    class ExpandedMenu:
        pos = "next to GameMenu","bellow GameMenu"
        size = 200,300
        hide = True
        style = "LIGHT_BLACK_BORDER"
            
    class Selection:
        pos = "left","above ModeChanger"
        size = "100%",300
        #hide = True
        style = "LIGHT_BLACK_BORDER"
        
    class BuildMenuLeft:
        pos = "left","bellow GameMenu"
        size = 300,"grow till ModeCommands"
        style = "LIGHT_BLACK_BORDER"
            
    class BuildMenuRight:
        pos = "right","bellow Standing"
        size = 300,"grow till SelectionCommands"
        style = "LIGHT_BLACK_BORDER"
        
    class GalaxyMenuLeft:
        pos = "left","below GameMenu"
        size = 200,"grow till ModeCommands"
        hide = True
        style = "LIGHT_BLACK_BORDER"
        
    class GalaxyMenuRight:
        pos = "right","bellow Standing"
        size = 200,"grow till SelectionCommands"
        hide = True
        style = "LIGHT_BLACK_BORDER"
            
