import tkinter as tk
from tkinter import ttk

import requests


def get_crypto_rates(crypto_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": crypto_id, "vs_currencies": "eur"}
    response = requests.get(url, params=params)
    return response.json().get(crypto_id, {}).get("eur", 0)


def convert_currency():
    crypto_id = crypto_dropdown.get()
    amount = float(amount_entry.get())
    rate = get_crypto_rates(crypto_id)
    result = amount * rate
    result_label.config(text=f"{amount} {crypto_id} is worth {result:.2f} EUR")


# Create main window
root = tk.Tk()
root.title("Crypto to EUR Converter")

# Create frames
form_frame = tk.Frame(root)
form_frame.grid(row=0, column=0, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, padx=10, pady=10)

# Create and grid the widgets in the form frame
crypto_label = tk.Label(form_frame, text="Select cryptocurrency:")
crypto_label.grid(row=0, column=0, padx=10, pady=10)
crypto_dropdown = ttk.Combobox(form_frame, values=["bitcoin", "ethereum", "litecoin"])
crypto_dropdown.grid(row=0, column=1, padx=10, pady=10)
crypto_dropdown.current(0)

amount_label = tk.Label(form_frame, text="Enter amount:")
amount_label.grid(row=0, column=2, padx=10, pady=10)
amount_entry = tk.Entry(form_frame)
amount_entry.grid(row=0, column=3, padx=10, pady=10)


# def on_key_release(event):
#     print(event.char)


# amount_entry.bind("<KeyRelease>", on_key_release)

# Create and grid the button in the button frame
convert_button = tk.Button(button_frame, text="Convert", command=convert_currency)
convert_button.grid(row=0, column=0, padx=10, pady=10)

# Create and grid the result label in the main window
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, pady=10)

# Run the main event loop
root.mainloop()
