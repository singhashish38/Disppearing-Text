from tkinter import *


TITLE_FONT = "Arial"
TITLE = "black"
WORD_FONT = "Times New Roman"
WORD = "red"
BACKGROUND = "grey"
count = 0

root = Tk()
root.title("Text Disappear")
root.config(padx=25, pady=25, bg=BACKGROUND)


def check_text():
    global count, current_text
    if len(text_entry.get()) > 0 and text_entry.get() == current_text:
        message_label.config(text=f"Deleting in: {count}")
        if count == 0:
            text_entry.delete(0, END)
            message_label.config(text=f"Start again...")
            root.after(1000, check_text)
        else:
            root.after(1000, check_text)
            count -= 1
    else:
        current_text = text_entry.get()
        count = 5
        root.after(1000, check_text)


current_text = ""
text_entry = Entry(font=(f"{WORD_FONT}", 20), width=40)
text_entry.grid(column=0, row=2, pady=30)
text_entry.focus()

title_label = Label(text="Text Disappear", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=BACKGROUND)
title_label.grid(column=0, row=0, pady=40)
message_label = Label(text="Start typing!", font=(WORD_FONT, 35), fg=WORD, bg=BACKGROUND)
message_label.grid(column=0, row=1)

if __name__ == "__main__":
    check_text()
    root.mainloop()