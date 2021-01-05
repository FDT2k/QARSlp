# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing Script
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
 
import os, re
from libqtile.config import Key,Group, Match, Drag, Click, Rule
from libqtile.command import lazy
from hooks import *
from theme import *
from keys import *
#wmname = "LG3D"
wmname = "qtile"
