from sys import exit
import webbrowser

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def cosmic_knowledge():
    raw_input('Say it > ')
    webbrowser.open_new(url)
    exit(1)

cosmic_knowledge()
