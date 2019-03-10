import webbrowser
import sys

def keres(mit):
  webbrowser.open_new_tab("https://google.com/search?q=" + mit)

if len(sys.argv) > 1:
  keres(sys.argv[1])
else:
  keres("python")
