from tkinter import Button, Entry, Label, Tk
import helpers as helper

# Create main window
main_window = Tk()
main_window.geometry("300x400")
main_window.title("Treatment Text Tool")

# Add a label
label1 = Label(main_window, text="Select a Option:", font=("Arial", 20), foreground="blue")
label1.grid(column=0, row=0, padx=10, pady=30)


def format_text():
    print(entry1.get())
    helper.format_filename(entry1.get(), secondary_window1)


def remove_text():
    print("File name: " + entry2.get())
    print("Part to remove: " + entry3.get())
    helper.remove_extra_words_in_filename(entry2.get(), entry3.get(), secondary_window2)


def replace_text():
    print("File name: " + entry4.get())
    print("Part to remove: " + entry5.get())
    print("Part to replace: " + entry6.get())
    helper.replace_part_of_namefile(entry4.get(), entry5.get(), entry6.get(), secondary_window3)


def format_filename():
    global secondary_window1
    global entry1

    secondary_window1 = Tk()
    secondary_window1.title("Treatment Text Tool")

    label2 = Label(secondary_window1, text="Enter the filename:")
    label2.grid(column=0, row=0, padx=10, pady=10)

    entry1 = Entry(secondary_window1)
    entry1.grid(column=1, row=0, padx=10, pady=10)

    format_button = Button(secondary_window1, text="Execute", width=10, height=1, background="#55a", foreground="#fff", command=format_text)
    format_button.grid(column=2, row=0, padx=10, pady=10)

    secondary_window1.mainloop()


def remove_part_of_the_filename():
    global secondary_window2
    global entry2
    global entry3

    secondary_window2 = Tk()
    secondary_window2.title("Treatment Text Tool")

    label3 = Label(secondary_window2, text="Enter the filename:")
    label3.grid(column=0, row=0, padx=10, pady=10)

    entry2 = Entry(secondary_window2)
    entry2.grid(column=1, row=0, padx=10, pady=10)

    label4 = Label(secondary_window2, text="Enter the part of the text you want to remove from the file name:")
    label4.grid(column=0, row=1, padx=10, pady=10)

    entry3 = Entry(secondary_window2)
    entry3.grid(column=1, row=1, padx=10, pady=10)

    remove_text_button = Button(secondary_window2, text="Execute", width=10, height=1, background="#55a", foreground="#fff", command=remove_text)
    remove_text_button.grid(column=2, row=0, padx=10, pady=10)

    secondary_window2.mainloop()


def replace_part_of_the_filename():
    global secondary_window3
    global entry4
    global entry5
    global entry6

    secondary_window3 = Tk()
    secondary_window3.title("Treatment Text Tool")

    label5 = Label(secondary_window3, text="Enter the filename:")
    label5.grid(column=0, row=0, padx=10, pady=10)

    entry4 = Entry(secondary_window3)
    entry4.grid(column=1, row=0, padx=10, pady=10)

    label6 = Label(secondary_window3, text="Enter the part of the text you want to remove from the file name:")
    label6.grid(column=0, row=1, padx=10, pady=10)

    entry5 = Entry(secondary_window3)
    entry5.grid(column=1, row=1, padx=10, pady=10)

    label7 = Label(secondary_window3, text="Enter the text you want to add in place of the removed text:")
    label7.grid(column=0, row=2, padx=10, pady=10)

    entry6 = Entry(secondary_window3)
    entry6.grid(column=1, row=2, padx=10, pady=10)

    remove_text_button = Button(secondary_window3, text="Execute", width=10, height=1, bg="#55a", fg="#fff", command=replace_text)
    remove_text_button.grid(column=2, row=0, padx=10, pady=10)

    secondary_window3.mainloop()


def formatting_csv_file():
    secondary_window4 = Tk()
    secondary_window4.title("Treatment Text Tool")

    label5 = Label(secondary_window4, text="Not implemented yet:")
    label5.grid(column=0, row=0, padx=10, pady=10)

    exit_button3 = Button(secondary_window4, text="Close", width=10, height=1, background="#55a", foreground="#fff", command=secondary_window4.destroy)
    exit_button3.grid(column=1, row=0, padx=10, pady=10)

    secondary_window4.mainloop()


def hiding_sensitive_data():
    secondary_window5 = Tk()
    secondary_window5.title("Treatment Text Tool")

    label6 = Label(secondary_window5, text="Not implemented yet")
    label6.grid(column=0, row=0, padx=10, pady=10)

    exit_button4 = Button(secondary_window5, text="Close", width=10, height=1, background="#55a", foreground="#fff", command=secondary_window5.destroy)
    exit_button4.grid(column=1, row=0, padx=10, pady=10)

    secondary_window5.mainloop()


# Add a button list
button1 = Button(main_window, width="30", text="Formating File Name", background="#55a", foreground="#fff", command=format_filename)
button1.grid(column=0, row=1, padx=40, pady=5)

button2 = Button(main_window, width="30", text="Removing Part Of The File Name", background="#55a", foreground="#fff",  command=remove_part_of_the_filename)
button2.grid(column=0, row=2, padx=40, pady=5)

button3 = Button(main_window, width="30", text="Replace Part Of The File Name", background="#55a", foreground="#fff",  command=replace_part_of_the_filename)
button3.grid(column=0, row=3, padx=40, pady=5)

button4 = Button(main_window, width="30", text="Formating CSV File", background="#55a", foreground="#fff",  command=formatting_csv_file)
button4.grid(column=0, row=4, padx=40, pady=5)

button5 = Button(main_window, width="30", text="Hiding Sensitive Data", background="#55a", foreground="#fff",  command=hiding_sensitive_data)
button5.grid(column=0, row=5, padx=40, pady=5)

# Button to exit
exit_button0 = Button(main_window, text="Quit", background="#55a", foreground="#fff", command=main_window.destroy)
exit_button0.grid(column=0, row=6, padx=60, pady=30)

# Execute main loop
main_window.mainloop()