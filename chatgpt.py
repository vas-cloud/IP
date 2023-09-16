
Link = "https://gpt4login.com/use-chatgpt-online-free/"

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

# Setting Up The Driver & Opening The Website :-

warnings.simplefilter("ignore")
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(Link)


# File Operations :- Writing, Reading

def FileReader():
    File = open("Chatnumber.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("Chatnumber.txt","w")
    File.write(Data)
    File.close()


def ChatGPTBrain(Query):
    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(FileReader())


# Getting Replies :- 

    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass


    AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

root = tk.Tk()
root.title("Image Generation")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)
style = ThemedStyle(theme="sandstone")

def image_generator():

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
        category_option = [
        "Choose Category",
    ]
        print("Enter Five(5) Keywords")
        for i in range(5):
            prompt = input(f"Enetr keywords Regarding Your Thumbnail: \n")
            category_option.append(prompt)

        category_var = tk.StringVar(value="Choose Category")
    
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

# Rest Of The Code 

print("Starting Trend Bot... ")
FileWriter(Data='3')

while True:
        
    try:
        Query = input("Enter Your Query : ")

        if Query == "quit":
            break

        elif Query == "create image" or Query== "generate image" or Query == "create thumbnail":
            image_generator()
            continue
                    
            
        else:
            print(ChatGPTBrain(Query=Query))

    except:
        pass