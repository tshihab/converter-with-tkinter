from tkinter import *

# Creating Screen
screen = Tk()
screen.geometry('1050x700')
screen.title("Temperature Converter")


def convert_temp():
    # Getting The value and converting them
    far = round(float(take_value.get()) * 9/5 + 32, 2)
    kel = round(float(take_value.get()) + 273.15, 2)

    # getting new input and delete the old one
    far_out_label.delete("1.0", END)
    far_out_label.insert(END, far)

    kel_out_label.delete("1.0", END)
    kel_out_label.insert(END, kel)


def kg_to_gram():
    # Converting KG to Gram
    gram = round(float(get_value.get())) * 1000

    # Converting KG to Pound
    pound = round(float(get_value.get()) * 2.20462, 2)

    # Converting KG to Ounce
    ounce = round(float(get_value.get()) * 35.274, 2)

    # Entering The weight to the widgets
    gram_out.delete("1.0", END)
    gram_out.insert(END, gram)

    pound_out.delete("1.0", END)
    pound_out.insert(END, pound)

    ounce_out.delete("1.0", END)
    ounce_out.insert(END, ounce)


def clear_all():
    # Clearing all data according to user input
    take_value.set('')
    far_out_label.delete("1.0", END)
    kel_out_label.delete("1.0", END)


def clear_weight():
    get_value.set('')  # Clear the entry label
    # get_value.delete(0, END) // will also clear the entry label
    gram_out.delete("1.0", END)
    pound_out.delete("1.0", END)
    ounce_out.delete("1.0", END)


# Creating Frame by Labels
temp_label = Label(screen, text="TEMPERATURE CONVERTER", font=('Times', 20, "bold"), )
temp_label.grid(row=0, column=1, pady=30)

# Labels and Buttons of Input Area
input_label = Label(screen, text='Enter Temperature in Celsius: ', font=('Times', 20, "bold"))
# Getting Value Using String Variable Through a Box
take_value = StringVar()
# Input Box & Buttons
read_input = Entry(screen, font=('Times', 20, "bold"), textvariable=take_value)
# Temperature Convert Button
convert_btn = Button(screen, text="CONVERT", font=('Times', 20, "bold"), bg='black', fg='white', command=convert_temp)
# Temperature Clear Button
clear_btn = Button(screen, text="CLEAR", font=('Times', 20, "bold"), bg='black', fg='white', command=clear_all)

# Name Labels
fahrenheit_label = Label(screen, text="FAHRENHEIT", font=('Castellar', 20, "normal"))
kelvin_label = Label(screen, text="KELVIN", font=('Castellar', 20, "normal"))

# Labels that show the output in a box
far_out_label = Text(screen, height=1, width=15, font=('Times', 20, "bold"))
kel_out_label = Text(screen, height=1, width=15, font=('Times', 20, "bold"))

# Placing The Elements in our window using grid() function
input_label.grid(row=1, column=0)
read_input.grid(row=1, column=1)
convert_btn.grid(row=1, column=2, padx=20)

# Label placement
fahrenheit_label.grid(row=2, column=0, pady=10)
kelvin_label.grid(row=2, column=2, pady=10)

# output placement
far_out_label.grid(row=3, column=0)
kel_out_label.grid(row=3, column=2)

# clear button placement
clear_btn.grid(row=4, column=1, sticky='', pady=20)


""" UNIT CONVERTER PART """
separation = Label(screen, text='UNIT CONVERTER', font=('Times', 20, "bold"))
separation.grid(row=5, column=1, pady=30)

# Labels of input area
entry_label = Label(screen, text="Enter Weight in KG:", font=('Times', 20, "bold"))
# Getting Value Using String Variable Through a Box
get_value = StringVar()
weight_input_label = Entry(screen, font=('Times', 20, "bold"), textvariable=get_value)
# Weight Convert Button
cnvrt_btn = Button(screen, text="CONVERT", font=('Times', 20, 'bold'), bg='dimgray', fg='white', command=kg_to_gram)
# Weight Clear Button
clear_button = Button(screen, text="CLEAR", font=('Times', 20, "bold"), bg='dimgray', fg='white', command=clear_weight)

# Name Labels
gram_label = Label(screen, text="GRAMS", font=('Castellar', 20, "normal"))
pound_label = Label(screen, text="POUNDS", font=('Castellar', 20, "normal"))
ounce_label = Label(screen, text="OUNCE", font=('Castellar', 20, "normal"))

# Labels that show outputs in box
gram_out = Text(screen, height=1, width=15, font=('Times', 20, "bold"))
pound_out = Text(screen, height=1, width=15, font=('Times', 20, "bold"))
ounce_out = Text(screen, height=1, width=15, font=('Times', 20, "bold"))

# Place The Elements using row and columns

# Input Label
entry_label.grid(row=6, column=0)
weight_input_label.grid(row=6, column=1)
cnvrt_btn.grid(row=6, column=2)

# Name Label
gram_label.grid(row=7, column=0)
pound_label.grid(row=7, column=1)
ounce_label.grid(row=7, column=2)

# Output Box Label
gram_out.grid(row=8, column=0, padx='10')
pound_out.grid(row=8, column=1, padx='10')
ounce_out.grid(row=8, column=2, padx='10')

clear_button.grid(row=9, column=1, sticky='', pady='10px')

# executing the program
screen.mainloop()
