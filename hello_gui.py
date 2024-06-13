import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World App")

# Set green background for the main window
root.configure(bg="green")

# Create and place the widgets with a green theme and increased size
entry_label = tk.Label(
    root, text="Enter your name:", bg="green", fg="white", font=("Arial", 24)
)
entry_label.pack(pady=10)

entry = tk.Entry(root, bg="white", fg="green", font=("Arial", 24), width=20)
entry.pack(pady=10)


def say_hello():
    name = entry.get()
    label.config(text=f"Hello, {name}!", font=("Arial", 24))


button = tk.Button(
    root,
    text="Say Hello",
    command=say_hello,
    bg="white",
    fg="green",
    font=("Arial", 24),
)
button.pack(pady=10)

label = tk.Label(root, text="", bg="green", fg="white", font=("Arial", 24))
label.pack(pady=10)

# Start the main event loop
root.mainloop()
