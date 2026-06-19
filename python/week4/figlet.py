import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font="standard")
elif  len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
     figlet.setFont(font=sys.argv[2])
else:
     sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))