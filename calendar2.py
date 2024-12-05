import tkinter as tk
import calendar

window = tk.Tk()
window.geometry("300x300")


calendar2 = tk.Label(text = "CALENDAR", background = "white", fg="black")
calendar2.place(x=140,y=20)

year = tk.Label(text = "Enter The Year:",background = "white", fg="black")
year.place(x=133,y=45)

box = tk.Entry(window,width=5)
box.place(x=146,y=70)

def display(): 
    window2 = tk.Tk()
    window2.geometry("600x600")
    user = int(box.get())  
    store = calendar.calendar(user)
    text = tk.Text(window2,width =150, height = 150)
    text.insert("1.3",store)
    text.pack(padx=30,pady=30)
    scroll = tk.Scrollbar(window2,command=text.yview)
    scroll.pack(side="right", fill="y")
    text.config(yscrollcommand=scroll.set)






button = tk.Button(window, text = "Submit", background = "White", command=display)
button.place(x=140,y=90)

















window.mainloop()