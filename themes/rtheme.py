from gui.theme import *

# configure theme image and data    
    
class RTheme(Theme):
    
    TEXTURE = "data/r.png"
    
    b = 1 
    
    DARK_BLACK_BORDER = TileBorder(18,18,76,76,b)
    MED_BLACK_BORDER = TileBorder(18,114,76,76,b)
    LIGHT_BLACK_BORDER = TileBorder(18,210,76,76,b)
    LIGHT_WHITE_BORDER = TileBorder(18,306,76,76,b)
    HEAVY_WHITE_BORDER = TileBorder(18,402,76,76,b)
    
    DARK_BLACK_WHITE_BORDER = TileBorder(114,18,76,76,b)
    MED_BLACK_WHITE_BORDER = TileBorder(114,114,76,76,b)
    LIGHT_BLACK_WHITE_BORDER = TileBorder(114,210,76,76,b)
    FULL_GRAY_WHITE_BORDER = TileBorder(114,210,76,76,b)
    
    BROWN = Stretch(114,402,76,76)
    GREEN = Stretch(210,18,76,76)
    YELLOW = Stretch(306,18,76,76)
    RED = Stretch(402,18,76,76)
    BLUE = Stretch(308,114,76,76)
    
    HEAVY_BLACK = Stretch(210,114,76,76)
    HEAVY_BRAY = Stretch(210,210,76,76)
    HEAVY_WHITE = Stretch(210,308,76,76)

    CHECKON = GREEN
    CHECKOFF = BROWN
    RADIOON = GREEN
    RADIOOFF = BROWN
    
    INPUT = MED_BLACK_WHITE_BORDER
    
    X = RED
    DRAG = BLUE
    
    FRAME = LIGHT_BLACK_BORDER
    FORM = MED_BLACK_BORDER
    FRAMEBAR = MED_BLACK_WHITE_BORDER
    BUTTON = DARK_BLACK_WHITE_BORDER
    MENU  = LIGHT_BLACK_BORDER
    PROGRESS_BAR = FULL_GRAY_WHITE_BORDER
    
    DOWN = HEAVY_BLACK
    
    TEXTCOLOR = (1,1,1,1)
    LABLECOLOR = TEXTCOLOR
    INPUTCOLOR = TEXTCOLOR
    
    SELECT_OPTION_COLOR = (.6,1,.6,1)

    VSCROLL = HEAVY_WHITE
    VSCROLL_UP = HEAVY_BLACK
    VSCROLL_CENTER = HEAVY_BLACK
    VSCROLL_DOWN = HEAVY_BLACK
    
    HSCROLL = HEAVY_WHITE
    HSCROLL_UP = HEAVY_BLACK
    HSCROLL_CENTER = HEAVY_BLACK
    HSCROLL_DOWN = HEAVY_BLACK
            
    SELECT_BG = LIGHT_WHITE_BORDER
    SELECT_HIGHLIGHT = YELLOW
