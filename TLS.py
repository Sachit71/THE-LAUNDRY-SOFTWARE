import pyautogui
import time
################################################################################
def clothes_count():
    Rollno=pyautogui.prompt('Enter roll no:')
    pyautogui.write(Rollno,interval=0.25)
    Rollno=int(Rollno)
    pyautogui.press('tab')
    #################################################################################
    blockname=pyautogui.prompt("Block name here:")
    blockname=str(blockname)
    pyautogui.write(blockname,interval=0.5)
    pyautogui.press('tab')
    #################################################################################
    Pant=pyautogui.prompt('No. of Pants:')#######
    pyautogui.write(Pant,interval=0.25)###
    Pant=int(Pant)##
    pyautogui.press('tab')#
    ##################################################################################
    Pyjama=pyautogui.prompt('No. of pyjama:')#######
    pyautogui.write(Pyjama,interval=0.25)###
    Pyjama=int(Pyjama)##
    pyautogui.press('tab')#
    ##################################################################################
    Shirts=pyautogui.prompt('No. of shirts:')#######
    pyautogui.write(Shirts,interval=0.24)
    Shirts=int(Shirts)
    pyautogui.press('tab')
    ###################################################################################
    Pillow=pyautogui.prompt('No.of pillow covers:')
    pyautogui.write(Pillow,interval=0.23)
    Pillow=int(Pillow)
    pyautogui.press('tab')
    ####################################################################################
    Towel=pyautogui.prompt('No of Towels:')
    pyautogui.write(Towel,interval=0.24)
    Towel=int(Towel)
    pyautogui.press('tab')
    ####################################################################################
    Panche=pyautogui.prompt('No of Panches:')
    pyautogui.write(Panche,interval=0.24)
    Towel=int(Panche)
    pyautogui.press('tab')
    ####################################################################################
    Valli=pyautogui.prompt('No of Vallis:')
    pyautogui.write(Valli,interval=0.24)
    Towel=int(Valli)
    pyautogui.press('tab')
####################################################################################
clothes_count()
####################################################################################
def rep():
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
####################################################################################
rep()
clothes_count()
while(True):
    rep()
    clothes_count()
####################################################################################
