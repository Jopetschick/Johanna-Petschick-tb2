import os
import tkinter as tk
from datetime import datetime, timedelta

from PIL import Image,ImageTk

def set_background(root, image_file_path, screen_width, screen_height):

    img = Image.open(image_file_path)
    img = img.resize((screen_width, screen_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)


def clear_widgets(root):

    for i in root.winfo_children():
        i.destroy()

def add_item(add_entry, listbox, shopping_list, messagebox):
    # Function to add an item to the shopping list
    item = add_entry.get()
    if item:
        shopping_list.append(item)
        listbox.insert(tk.END, item)
        add_entry.delete(0, tk.END)
    else:
        # Show a warning message if the item entry is empty
        messagebox.showwarning('Warning', 'Please enter an item.')

# Function to reset the shopping list
def reset_list(listbox):
    global shopping_list
    shopping_list = []
    listbox.delete(0, tk.END)

def save_list(listbox, messagebox, shopping_list):
        # Function to save the shopping list to a text file
        if not shopping_list:
            # Show a warning message if the shopping list is empty
            messagebox.showwarning('Warning', 'Shopping list is empty.')
            return

        # Create a directory to store shopping lists if it doesn't exist
        if not os.path.exists('shopping_lists'):
            os.makedirs('shopping_lists')

        # Generate file name with the current date and time
        now = datetime.now()
        date_time = now.strftime('%Y_%m_%d')
        file_name = f'shopping_lists/shopping_list_{date_time}.txt'

        # Save the shopping list to text file
        with open(file_name, 'w') as file:
            for item in shopping_list:
                file.write(f'{item}\n')
        # Show a success message with the file name where the shopping list is saved
        messagebox.showinfo('Success', f'Shopping list saved to {file_name}')
        # Reset the shopping list and the displayed listbox
        reset_list(listbox)

def update_food_items(food_group_var, food_groups, food_item_menu, food_item_var, entry_purchase_date):
    # Update the food item menu based on the selected food group
    food_group = food_group_var.get()
    menu = food_item_menu['menu']
    menu.delete(0, 'end')
    # Create the food item menu with items from the selected food group
    for item in food_groups[food_group]:
        menu.add_command(label=item, command=lambda i=item: food_item_var.set(i))

def check_expiration(food_group_var, food_item_var, entry_purchase_date, messagebox, food_groups):
    # Function to check the expiration date of the selected food item
    food_group = food_group_var.get()
    food_item = food_item_var.get()

    try:
        # Parse the user-input purchase date
        purchase_date = datetime.strptime(entry_purchase_date.get(), '%d.%m.%Y')
    except ValueError:
        messagebox.showwarning('Warning', 'Invalid date format. Please use DD.MM.YYYY')
        return
    # Calculate expiration date based on the selected food group and item
    expiration_days = food_groups[food_group][food_item]
    expiration_date = purchase_date + timedelta(days=expiration_days)

    # Get the current date
    today = datetime.now()
    # Calculate remaining days until expiration
    remaining_days = (expiration_date - today).days

    # Display a message about the expiration status
    if remaining_days < 0:
        messagebox.showinfo('Expiration Check', f'{food_item} has expired.')
    else:
        messagebox.showinfo('Expiration Check', f'{food_item} is good for {remaining_days} more days.')



def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()