import customtkinter
from tkinter import *
from forex_python.converter import CurrencyRates
from PIL import Image, ImageTk
from tkinter import messagebox

frame = customtkinter.CTk()
frame.config(bg="#202630")
frame.config(cursor="hand2")
frame.geometry("400x450")
frame.title("Currency Converter")

original_img = Image.open("currency.png")
# Reduce the size of the image
resized_img = original_img.resize((140, 140))

# Convert the resized image to a PhotoImage object
img = ImageTk.PhotoImage(resized_img)

# Set the resized image as the window icon
frame.iconphoto(False, img)
Label(frame, image=img, bg="#202630").place(x=0, y=0)

# Create From label and To label
Label(frame, text="From", font=('Arial', 15, 'bold'), fg="white", bg='#202630').place(x=10, y=150)
Label(frame, text="To", font=('Arial', 15, 'bold'), fg="white", bg='#202630').place(x=248, y=150)

# Currency list
currency_list = ["USD", "INR","CAD", "AED", "EUR", "CNY", "GBP"]

variable1 = StringVar()  # From Currency
variable2 = StringVar()  # To Currency
txt = StringVar()  # Amount


# Convert Function

def convert():
    try:
        from_currency = variable1.get()
        to_currency = variable2.get()
        amount = float(amount_entry.get())

        c = CurrencyRates()
        rate = c.get_rate(from_currency, to_currency)

        if rate is not None:
            converted_amount = round(amount * rate, 4)
            txt.set(str(converted_amount))
            result_label = customtkinter.CTkLabel(frame, textvariable=txt, font=('Arial', 30, 'bold'),
                                                  fg_color="#202630", text_color="white")
            result_label.place(x=125, y=360)
        else:
            messagebox.showerror(title="Error", message="Invalid currency codes")

    except Exception as e:
        messagebox.showerror(title="Error", message="Enter valid input")


# Reset Function
def reset():
    amount_entry.delete(0, END)     # To clear entry text


# From and To ComboBox
from_manu = customtkinter.CTkComboBox(frame, variable=variable1, values=currency_list, font=('Arial', 15, 'bold'),
                                      fg_color="#FFFFFF", text_color="black", button_color="#710193",
                                      button_hover_color="#710193", dropdown_text_color="black")
from_manu.place(x=10, y=180)

to_manu = customtkinter.CTkComboBox(frame, variable=variable2, values=currency_list, font=('Arial', 15, 'bold'),
                                    fg_color="#FFFFFF", text_color="black", button_color="#710193",
                                    button_hover_color="#710193", dropdown_text_color="black")
to_manu.place(x=250, y=180)

# Entry Filed
amount_entry = customtkinter.CTkEntry(frame, font=('Arial', 20, 'bold'), text_color="black", justify=CENTER,
                                      width=370, fg_color="white", border_color="black")
amount_entry.place(x=18, y=240)

# Convert and Reset Button
convert_button = customtkinter.CTkButton(frame, command=convert, text="Convert", font=('Arial', 20, 'bold'),
                                         text_color="white", fg_color="#710193", hover_color="#710193", )
convert_button.place(x=50, y=300)

reset_button = customtkinter.CTkButton(frame, command=reset, text="Reset", font=('Arial', 20, 'bold'),
                                       text_color="white", fg_color="#bd5b15", hover_color="#bd5b15", )
reset_button.place(x=200, y=300)

# Start main loop
frame.mainloop()
