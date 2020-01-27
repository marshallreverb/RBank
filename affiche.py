import colorama
from colorama import Fore ,Back , Style
colorama.init()

def aff_(msg , *var_str):
    print("***************************************************************************")
    print("**",msg)
    for var in var_str:
        print("**{}".format(var))
    print("***************************************************************************")

def aff_err(msg):
    print("***************************************************************************")
    print(Fore.RED)
    print("**{}".format(msg))
    print(Style.RESET_ALL)
    print("***************************************************************************")
