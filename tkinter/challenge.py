# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter
# mainWindow.winfo_height()
mainWindow = tkinter.Tk()

mainWindow.minsize(200,200)
mainWindow.maxsize(410,410)

mainWindow.title("Calculator")
mainWindow.geometry('360x360-8-200')

background = tkinter.Frame(mainWindow)
background.grid(row=1, column=0, sticky='w', columnspan=5)
background.config(border=5)
input_field = tkinter.Entry(mainWindow)
input_field.grid(row=0, column=0, sticky='we', columnspan=6)
input_field.rowconfigure(0, weight=500)


sign_1 = tkinter.Button(background, text="C", width=4)
sign_1.grid(row=1, column=0, sticky='ne')
sign_2 = tkinter.Button(background, text="CE", width=4)
sign_2.grid(row=1, column=1, sticky='ne')

sign_3 = tkinter.Button(background, text="7", width=4)
sign_3.grid(row=2, column=0, sticky='ne')
sign_4 = tkinter.Button(background, text="8", width=4)
sign_4.grid(row=2, column=1, sticky='ne')
sign_5 = tkinter.Button(background, text="9", width=4)
sign_5.grid(row=2, column=2, sticky='ne')
sign_6 = tkinter.Button(background, text="+", width=4)
sign_6.grid(row=2, column=3, sticky='ne')

sign_7 = tkinter.Button(background, text="4", width=4)
sign_7.grid(row=3, column=0, sticky='ne')
sign_8 = tkinter.Button(background, text="5", width=4)
sign_8.grid(row=3, column=1, sticky='ne')
sign_9 = tkinter.Button(background, text="6", width=4)
sign_9.grid(row=3, column=2, sticky='ne')
sign_10 = tkinter.Button(background, text="-", width=4)
sign_10.grid(row=3, column=3, sticky='ne')

sign_11 = tkinter.Button(background, text="1", width=4)
sign_11.grid(row=4, column=0, sticky='ne')
sign_12 = tkinter.Button(background, text="2", width=4)
sign_12.grid(row=4, column=1, sticky='ne')
sign_13 = tkinter.Button(background, text="3", width=4)
sign_13.grid(row=4, column=2, sticky='ne')
sign_14 = tkinter.Button(background, text="*", width=4)
sign_14.grid(row=4, column=3, sticky='ne')

sign_15 = tkinter.Button(background, text="0", width=4)
sign_15.grid(row=5, column=0, sticky='ne')
sign_16 = tkinter.Button(background, text="=", width=10)
sign_16.grid(row=5, column=1, columnspan=2)
sign_17 = tkinter.Button(background, text="/", width=4)
sign_17.grid(row=5, column=3, sticky='ne')


mainWindow['padx'] = 20

mainWindow.mainloop()