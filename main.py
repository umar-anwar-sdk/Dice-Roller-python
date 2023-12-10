import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller App by Omer")

        # Set background image
        image_path = os.path.join(os.path.dirname(__file__), "background.jpg")  # Replace with your image file
        if os.path.exists(image_path):
            background_image = Image.open(image_path)
            background_image = background_image.resize((500, 400))  # Set the desired width and height
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(master, image=background_photo)
            background_label.image = background_photo
            background_label.place(relwidth=1, relheight=1)

        # Apply a style for buttons
        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12, 'bold'))

        # Number of Dice label
        self.num_dice_label = tk.Label(master, text="Number of Dice:", font=('Helvetica', 14), bg='#b3e0ff')
        self.num_dice_label.pack(pady=10)

        # Number of Dice dropdown
        self.num_dice_var = tk.StringVar()
        self.num_dice_var.set("1")  # default value
        self.num_dice_dropdown = ttk.Combobox(master, textvariable=self.num_dice_var, values=["1", "2", "3", "4", "5"])
        self.num_dice_dropdown.pack()

        # Result label
        self.result_label = tk.Label(master, text="", font=('Helvetica', 18, 'bold'), bg='#b3e0ff')
        self.result_label.pack(pady=20)

        # Roll button
        self.roll_button = ttk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        # Quit button
        self.quit_button = ttk.Button(master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

    def roll_dice(self):
        num_dice = int(self.num_dice_var.get())
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        result_text = f"Result: {', '.join(map(str, dice_rolls))}"
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")  # Adjust the window size as needed
    app = DiceRollerApp(root)
    root.mainloop()
