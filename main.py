import eel

eel.init('index.html')

@eel.expose
def search_srts():
    return True

eel.start('index.html')
