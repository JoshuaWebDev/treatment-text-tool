import tkinter as tk
import helpers as helper

# Create main window
window1 = tk.Tk()
window1.title("Treatment Text Tool")

# Add a label
label1 = tk.Label(window1, text="Select a Option:")
label1.grid(column=0, row=0, padx=100, pady=10)

def format_text():
    print(entry.get())
    helper.format_filename(entry.get(), window2)


def format_filename():
    window1.quit()

    global filename
    global window2
    global entry

    window2 = tk.Tk()
    window2.title("Treatment Text Tool")

    label2 = tk.Label(window2, text="Enter the filename:")
    label2.grid(column=0, row=0, padx=10, pady=10)

    entry = tk.Entry(window2)
    entry.grid(column=1, row=0, padx=10, pady=10)

    formatButton = tk.Button(window2, text="Execute", width=10, height=1, fg="white", bg="blue", command=format_text)
    formatButton.grid(column=2, row=0, padx=10, pady=10)

    window2.mainloop()


def remove_part_of_the_filename():
    pass


def replace_part_of_the_filename():
    pass


def formatting_csv_file():
    pass


def hiding_sensitive_data():
    pass


# Add a button list
button1 = tk.Button(window1, text="Formating File Name", command=format_filename)
button1.grid(column=0, row=1, padx=100, pady=5)

button2 = tk.Button(window1, text="Removing Part Of The File Name", command=remove_part_of_the_filename)
button2.grid(column=0, row=2, padx=100, pady=5)

button3 = tk.Button(window1, text="Replace Part Of The File Name", command=replace_part_of_the_filename)
button3.grid(column=0, row=3, padx=100, pady=5)

button4 = tk.Button(window1, text="Formating CSV File", command=formatting_csv_file)
button4.grid(column=0, row=4, padx=100, pady=5)

button5 = tk.Button(window1, text="Hiding Sensitive Data", command=hiding_sensitive_data)
button5.grid(column=0, row=5, padx=100, pady=5)

# Button to exit
exitButton = tk.Button(window1, text="Quit", command=window1.destroy)
exitButton.grid(column=0, row=6, padx=100, pady=5)

# Execute main loop
window1.mainloop()