# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 

from funct import *
from theme import *
from key import *


##### End Mouse/Keyboard #####

colors = init_colors()
widget_defaults = init_widgets_defaults()
widgets_top = init_widgets_top()
widgets_bott = init_widgets_bott()
widgets_screen_top = init_widgets_screen_top()
widgets_screen_bot = init_widgets_screen_bot()
screens = init_screens()

#wmname = "LG3D"
wmname = "qtile"
