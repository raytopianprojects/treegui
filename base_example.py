import direct.directbase.DirectStart
"""
    This is empty example that shows the tree gui
    without any thing on screen
"""
from gui.core import GUI
from gui.theme import Theme
base.disableMouse()

# create main gui class
GUI(theme=Theme("data/affgui.png"))

run()