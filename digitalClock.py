from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="steelblue")
Label = Label(window, text="Welcome", font=("arial black",78,"bold"), bg="steelblue", fg="white")
Label.pack(pady=100)
window.mainloop() 