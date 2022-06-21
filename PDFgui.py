import tkinter as tk
from TkinterDnD2 import DND_FILES, TkinterDnD
import PDFfuncs as f
from time import sleep

def remove_selected():
    x = inputBox.curselection()
    for i in inputBox.curselection():
        inputBox.delete(x[0])

def button_pressed(option = "convert"):
    try:
        totalString = ""
        for i in range(0, inputBox.index('end')):
            path = inputBox.get(i)
            totalString += path
        print(totalString.strip("\n"))
        if option == "convert":
            f.convert_and_save(totalString.strip("\n"))
        elif option == "merge":
            f.mergePDFs(totalString.strip("\n"))
    except TypeError:
        print("Error reading path")

def drop_inside_listbox(event):
    if "{" in event.data or "}" in event.data:
        event.data = event.data.strip("{}")
        events = event.data.split("} {")
        pass
    else:
        events = event.data.split(" ")
    events = sorted(events)
    for ev in events:
        ev += '\n'
        inputBox.insert("end", ev)
        inputBox.see(tk.END)

def mergeButton_pressed():
    for i in range(0, inputBox.index('end')):
        if '.pdf' not in inputBox.get(i):
            errLabel = tk.Label(
                    window, text="Error! Not all files are PDFs!\nFirst error found on line {}".format(i+1), 
                    font="arial 11")
            errLabel.pack(pady=10, padx=10)
            label.after(4000, errLabel.destroy)
            return
    button_pressed("merge")

window = TkinterDnD.Tk()
window.title("PDF App")
print("Application is running")
window.geometry("1000x720")
#window.resizable(False, False)

label = tk.Label(
    window, text="Enter paths of files required to be converted: ", 
    borderwidth=2, relief='raised', font = "arial 11 bold")
label.pack(pady = 10)

textFrame = tk.Frame(window)
textFrame.pack()

yScroller = tk.Scrollbar(textFrame)
yScroller.pack(side=tk.RIGHT, fill=tk.Y, pady=20)

inputBox = tk.Listbox(textFrame, width=120, height=30, yscrollcommand=yScroller.set, selectmode=tk.EXTENDED)
inputBox.pack(pady = 20)
inputBox.drop_target_register(DND_FILES)
inputBox.dnd_bind("<<Drop>>", drop_inside_listbox)
yScroller.config(command = inputBox.yview)

buttonFrame = tk.Frame(window)
buttonFrame.pack()
removeButton = tk.Button(buttonFrame, text='Remove Selected', width=25, command=remove_selected)
removeButton.pack(side=tk.LEFT, pady=10, padx=5)
button = tk.Button(buttonFrame, text='Convert All', width=25, command=button_pressed)
button.pack(side=tk.RIGHT, pady=10, padx=5)
mergeButton = tk.Button(buttonFrame, text='Merge PDFs', width=25, command=mergeButton_pressed)
mergeButton.pack(side=tk.RIGHT, pady=10, padx=5)

window.mainloop()
print("Closing 'Image to PDF'...")