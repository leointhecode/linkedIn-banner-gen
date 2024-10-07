from get_banner import get_banner
from modify_html import modify_html

inputName = input('What it is your name?: ')
inputLine1 = input('What it is your first phrase? (We recommend min 40 char): ')
inputLine2 = input('What it is your second phrase? (We recommend max 40 char): ')
inputLine3 = input('What it is your third phrase? (We recommend max 35 char): ')

modify_html(name=inputName, line1=inputLine1, line2=inputLine2, line3=inputLine3)
get_banner()

