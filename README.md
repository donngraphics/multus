This code takes mutliple inputs from the user; the user is able to create a new folder onto the desktop (or just leave the default name). Next the user inputs the name of the folder they're trying to locate, and the PDF type. The script then makes a copy of the PDF onto newly created folder on the desktop. While this is built on Windows, the idea is to make changes to the path directories and use the code on any OS. There are two files right now - a pure CL script and a GUI version built with tKinter. The script works as intended, and the GUI version only takes one folder and one PDF type response from the user. The end goal is to have a GUI that takes up to ten different folders and PDF types from the user. Creating multiple entry boxes and radio buttons via for loops have proved problematic, but that's the last step before the GUI is finalized. I would like to keep the code DRY, but looping with tKinter widgets might not be the best idea. I will keep trying and update as I go.
