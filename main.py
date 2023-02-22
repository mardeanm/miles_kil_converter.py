from tkinter import *


def miles_to_km():
    num_miles = miles.get()
    answer = float(num_miles) * 1.609
    km_result.config(text=f"{answer}")


window = Tk()
window.title("Miles to K, Converter")

#window.config(pady=20, padx=20)
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

miles = Entry(width=5)
miles.grid(column=1, row=0)

equal_to = Label(text="is equal to ")
equal_to.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

convert = Button(text="Calculate", command=miles_to_km)
convert.grid(column=1, row=2)
window.mainloop()
