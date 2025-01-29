from tkinter import Button, Entry, Label, Tk
import helpers as helper

# Create main window
mainWindow = Tk()
mainWindow.geometry("300x400")
mainWindow.title("Treatment Text Tool")

# Add a label
label1 = Label(mainWindow, text="Select a Option:", font=("Arial", 20), foreground="blue")
label1.grid(column=0, row=0, padx=10, pady=30)

def format_text():
    print(entry1.get())
    helper.format_filename(entry1.get(), secondaryWindow1)

def remove_text():
    print("File name: " + entry2.get())
    print("Part to remove: " + entry3.get())
    print("Part to add: " + entry4.get())
    helper.replace_part_of_namefile(entry2.get(), entry3.get(), entry4.get(), secondaryWindow2)

def format_filename():
    global secondaryWindow1
    global entry1

    secondaryWindow1 = Tk()
    secondaryWindow1.title("Treatment Text Tool")

    label2 = Label(secondaryWindow1, text="Enter the filename:")
    label2.grid(column=0, row=0, padx=10, pady=10)

    entry1 = Entry(secondaryWindow1)
    entry1.grid(column=1, row=0, padx=10, pady=10)

    formatButton = Button(secondaryWindow1, text="Execute", width=10, height=1, background="#55a", foreground="#fff", command=format_text)
    formatButton.grid(column=2, row=0, padx=10, pady=10)

    secondaryWindow1.mainloop()


def remove_part_of_the_filename():
    global secondaryWindow2
    global entry2
    global entry3
    global entry4

    secondaryWindow2 = Tk()
    secondaryWindow2.title("Treatment Text Tool")

    label3 = Label(secondaryWindow2, text="Enter the filename:")
    label3.grid(column=0, row=0, padx=10, pady=10)

    entry2 = Entry(secondaryWindow2)
    entry2.grid(column=1, row=0, padx=10, pady=10)

    label4 = Label(secondaryWindow2, text="Enter the part of the text you want to remove from the file name:")
    label4.grid(column=0, row=1, padx=10, pady=10)

    entry3 = Entry(secondaryWindow2)
    entry3.grid(column=1, row=1, padx=10, pady=10)

    label5 = Label(secondaryWindow2, text="Enter the text you want to add in place of the removed text:")
    label5.grid(column=0, row=2, padx=10, pady=10)

    entry4 = Entry(secondaryWindow2)
    entry4.grid(column=1, row=2, padx=10, pady=10)

    removeTextButton = Button(secondaryWindow2, text="Execute", width=10, height=1, background="#55a", foreground="#fff", command=remove_text)
    removeTextButton.grid(column=2, row=0, padx=10, pady=10)

    secondaryWindow2.mainloop()


def replace_part_of_the_filename():
    secondaryWindow3 = Tk()
    secondaryWindow3.title("Treatment Text Tool")

    label4 = Label(secondaryWindow3, text="Not implemented yet")
    label4.grid(column=0, row=0, padx=10, pady=10)

    exitButton2 = Button(secondaryWindow3, text="Close", width=10, height=1, background="#55a", foreground="#fff", command=secondaryWindow3.destroy)
    exitButton2.grid(column=1, row=0, padx=10, pady=10)

    secondaryWindow3.mainloop()


def formatting_csv_file():
    secondaryWindow4 = Tk()
    secondaryWindow4.title("Treatment Text Tool")

    label5 = Label(secondaryWindow4, text="Not implemented yet:")
    label5.grid(column=0, row=0, padx=10, pady=10)

    exitButton3 = Button(secondaryWindow4, text="Close", width=10, height=1, background="#55a", foreground="#fff", command=secondaryWindow4.destroy)
    exitButton3.grid(column=1, row=0, padx=10, pady=10)

    secondaryWindow4.mainloop()


def hiding_sensitive_data():
    secondaryWindow5 = Tk()
    secondaryWindow5.title("Treatment Text Tool")

    label6 = Label(secondaryWindow5, text="Not implemented yet")
    label6.grid(column=0, row=0, padx=10, pady=10)

    exitButton4 = Button(secondaryWindow5, text="Close", width=10, height=1, background="#55a", foreground="#fff", command=secondaryWindow5.destroy)
    exitButton4.grid(column=1, row=0, padx=10, pady=10)

    secondaryWindow5.mainloop()


# Add a button list
button1 = Button(mainWindow, width="30", text="Formating File Name", background="#55a", foreground="#fff", command=format_filename)
button1.grid(column=0, row=1, padx=40, pady=5)

button2 = Button(mainWindow, width="30", text="Removing Part Of The File Name", background="#55a", foreground="#fff",  command=remove_part_of_the_filename)
button2.grid(column=0, row=2, padx=40, pady=5)

button3 = Button(mainWindow, width="30", text="Replace Part Of The File Name", background="#55a", foreground="#fff",  command=replace_part_of_the_filename)
button3.grid(column=0, row=3, padx=40, pady=5)

button4 = Button(mainWindow, width="30", text="Formating CSV File", background="#55a", foreground="#fff",  command=formatting_csv_file)
button4.grid(column=0, row=4, padx=40, pady=5)

button5 = Button(mainWindow, width="30", text="Hiding Sensitive Data", background="#55a", foreground="#fff",  command=hiding_sensitive_data)
button5.grid(column=0, row=5, padx=40, pady=5)

# Button to exit
exitButton0 = Button(mainWindow, text="Quit", background="#55a", foreground="#fff", command=mainWindow.destroy)
exitButton0.grid(column=0, row=6, padx=60, pady=30)

# Execute main loop
mainWindow.mainloop()