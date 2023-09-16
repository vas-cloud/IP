import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle


root = tk.Tk()
root.title("Image Generation")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)
style = ThemedStyle(theme="sandstone")


def display_image(category):
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=NQ511kTo4svYUNc6Hg_xH6B_3b10oOkM0SH_9YT6WQc"

    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    photo = ImageTk.PhotoImage(
        Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS)
    )
    label.config(image=photo)
    label.image = photo 


def enable_button(*args):
    generate_button.config(
        state="normal" if category_var.get() != "Choose Category" else "disabled"
    )


def create_gui():
    global category_var, generate_button, label  # Fix the typo here
    prompt = input("Enetr Your Prompt: \n")

    category_var = tk.StringVar(value="Choose Category")
    category_option = [
        "Choose Category",
    ]
    category_option.append(prompt)
    category_dropdown = ttk.OptionMenu(
        root, category_var, *category_option, command=enable_button
    )
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    generate_button = ttk.Button(
        text="Generate Image",
        state="disabled",
        command=lambda: display_image(category_var.get())
    )
    generate_button.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

    label = tk.Label(root, background="white")  # Fix the typo here
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()


if __name__ == "__main__":
    create_gui()
