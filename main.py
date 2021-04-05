import eel
from middleware.mid_convert import *

if __name__ = '__main__':
    eel.init('frontend')
    eel.browsers.set_path("chrome"), "E:\Downloads\chrome-win\chrome-win\chrome.exe"
    eel.start('frontend/index.html', mode="chrome", size=(760,760))
