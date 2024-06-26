# Import necessary libraries
import tkinter as tk
from tktooltip import ToolTip
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
from src.helpers import add_item, save_list, update_food_items, check_expiration, clear_widgets
from tkmacosx import Button, CircleButton

# Create main Tkinter window
root = tk.Tk()
ico = Image.open('images/fridgeicon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.geometry('400x700')
root.title('Too Good To Waste')

# Creating a frame (f1) to contain an image label
f1 = tk.Frame(root)
# Opening an image file from the 'images' folder
img = Image.open('images/home_fridge.png')
# Resize the image to fit the frame
img = img.resize((450, 700), Image.LANCZOS)
# Converting the resized image to a Tkinter-compatible format
pic = ImageTk.PhotoImage(img)
# Creating a label (lab) within the frame (f1) to display the image
Lab = tk.Label(f1, image=pic)
# Packing the frame (f1) to place it in the main Tkinter window
f1.pack()
# Packing the image label (lab) within the frame to display the image
Lab.pack()

# Setting up name label for user input
name_label = tk.Label(root, text='Enter your name:', font='Quicksand 14 bold', fg='white', bg='#D4A9D4')
name_label.place(x=150, y=45)

# Creating an entry box to store the users name
name = tk.StringVar()  # This variable will store the name of user

# Creating an entry box for user input
name_box = tk.Entry(root, textvar=name, font='Quicksand 11 bold', fg='#D695CF', bg='white')
name_box.place(x=137, y=80)
ToolTip(name_box, msg='Enter your name in the Box')

def home():
    # Global declarations for variables used in multiple functions
    global Lab, f2, f3, calender, protein_button, dairy_button, veggie_button, name, fridge_button, \
        home_button, seasonalcalender, fridge
    # Destroying previous frames and widgets
    clear_widgets(root)

    # Setting up the Home page
    root.title('Home')
    root.geometry('400x700')
    f2 = tk.Frame(root)
    img = Image.open('images/home_fridge.png')
    img = img.resize((450, 700), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f2, image=pic)
    Lab.pack()
    f2.pack()

    # Creating and placing buttons
    fridge_button = tk.Button(root, text='Open Your Fridge', font='Quicksand 11 bold', bg='#D4A9D4',
                              bd='0', fg='#D695CF', command=open_fridge)
    fridge_button.place(x=165, y=100)

    # Displaying a welcome message with the user's name
    welcome_name = tk.Label(root, text=f"{name.get()}'s fridge", foreground='black', bg='#D4A9D4',
                            font='Quicksand 15 bold')
    welcome_name.place(x=170, y=60)

    # Creating a button for adding items to the shopping list
    shopping_list = tk.Button(root, text='Add to your Shopping List!', font='Quicksand 8 bold',
                              bg='#D4A9D4', bd='0', fg='#D695CF', width=16, command=shoppinglist)
    shopping_list.place(x=165, y=300)
    ToolTip(shopping_list, msg='Do you want to write something on your Shopping List? Click here!')

    root.mainloop()

def open_fridge():
    # Global declarations for variables used in multiple functions
    global Lab, f1, f2, f3, calender, protein_button, dairy_button, veggie_button, name, fridge_button, home_button, seasonalcalender, fridge
    # Destroying previous frames and widgets
    clear_widgets(root)
    root.title('Open Fridge')
    root.geometry('520x900')
    f3 = tk.Frame(root)
    img = Image.open('images/open_fridge.png')
    img = img.resize((490, 710), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f3, image=pic)
    Lab.pack()
    f3.pack()

    # Creating buttons for different food compartments to open pop up later
    dairy_button = Button(root, text='Dairy', font='Quicksand 13', bg='#D4A9D4', fg='white', width=50,
                             command=dairy_page)
    dairy_button.place(x=68, y=605)
    ToolTip(dairy_button, msg='Check what´s in your Dairy compartment!')

    protein_button = Button(root, text='Protein', font='Quicksand 13', bg='#D4A9D4', fg='white', width=60,
                               command=protein_page)
    protein_button.place(x=158, y=605)
    ToolTip(protein_button, msg='Check what´s in your Protein compartment!')

    veggie_button = Button(root, text='Veggies', font='Quicksand 13', bg='#D4A9D4', fg='white', width=65,
                              command=veggie_page)
    veggie_button.place(x=258, y=605)
    ToolTip(veggie_button, msg='Check what´s in your Veggie compartment!')

    # Welcome Label with a message to welcome the user
    welcome_name = tk.Label(root, text=f'Welcome, {name.get()}', bd='0',
                            fg='#CC8EC5', font='Quicksand 14 bold')
    welcome_name.place(x=68, y=98)

    # Menu buttons
    # Home button to get back to home page

    home_button = Button(text='Home', font='Quicksand 16', bg='#D4A9D4', fg='white', width= 60,
                         command=home)
    home_button.place(x=68, y=50)

    # Seasonal Calender button to view seasonal vegetable calender
    seasonalcalender = Button(text='Calender', font='Quicksand 16', bg='#D4A9D4', fg='white', width=80,
                              command=calender_page)
    seasonalcalender.place(x=180, y=50)

    # Button for expiration date checker
    expirationdate = Button(text='Check Expiration', font='Quicksand 16', bg='#D4A9D4', fg='white', width=140,
                            command=expiration_checker)
    expirationdate.place(x=312, y=50)

    # Creating information button to open web browser later
    info_button = CircleButton(text='i', font='Quicksand 13 bold', width=30, bg='#D4A9D4',
                               bd='0', fg='white', command=info)
    info_button.place(x=475, y=10)
    ToolTip(info_button, font='Quicksand 11', msg='Click here for more information about Foodsharing!')

    root.mainloop()

def instructions():
    global next, root
    if name.get() == "":
        popup = tk.Toplevel()
        popup.geometry('200x100')
        popup.title('Instructions')
        go_back = tk.Button(popup, text='Go back', font='Quicksand 12 bold', fg='#D695CF',
                            bd=0, command=popup.destroy)
        go_back.place(relx=0.5, rely=0.7, anchor="center")
        instruction_label = tk.Label(popup, text=f"Please enter your name first.",
                                     font='Quicksand 13')
        instruction_label.place(relx=0.5, rely=0.4, anchor="center")
    else:
        submit.destroy()
        name_box.destroy()
        name_label.destroy()
        # Displaying a welcome message with the user's name
        welcome_name = tk.Label(root, text=f"{name.get()}'s fridge", foreground='black', bg='#D4A9D4',
                                font='Quicksand 15 bold')
        welcome_name.place(x=170, y=60)
        fridge_button = tk.Button(root, text='Open Your Fridge', font='Quicksand 11 bold', bg='#D4A9D4', bd='0',
                                  fg='#D695CF', command=open_fridge)
        fridge_button.place(x=165, y=100)
        ToolTip(fridge_button, msg='Do you want to open your fridge? Click here!')
        # Creating a button for adding items to the shopping list
        shopping_list = tk.Button(root, text='Add to your Shopping List!', font='Quicksand 8 bold', bg='#D4A9D4',
                                  bd='0',
                                  fg='#D695CF', width=16, command=shoppinglist)
        shopping_list.place(x=165, y=300)
        ToolTip(shopping_list, msg='Do you want to write something on your Shopping List? Click here!')
        popup = tk.Toplevel()
        popup.geometry('300x190')
        popup.title('Instructions')
        T=tk.Text(popup, font='Quicksand 13')
        T.pack()
        text= '''Welcome to “Too Good to Waste”!

Here, you can track what’s in your fridge, 
get ideas for new recipes, add items to your 
shopping list, and learn about seasonal foods 
(and much more!). 

Open your fridge to find out what’s inside!'''
        T.insert(tk.END, text)
        T.configure(state='disabled')
        go_back = Button(popup, text='Okay!', font='Quicksand 13 bold', fg='#D695CF', command=popup.destroy)
        go_back.place(relx=0.5, rely=0.85, anchor='center')

submit = tk.Button(root, text='submit', font='Quicksand 12 bold', fg='#D695CF', bd=0, command=instructions)
submit.place(x=185, y=120)
ToolTip(submit, msg='Click here to open your fridge!')

# Creating frames for organization
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f5 = tk.Frame(root)

# Creating buttons with different functionalities and placeholders
fridge_button = tk.Button()
home_button = tk.Button()
fridge = tk.Button()
seasonalcalender = tk.Button()
calender = tk.Button()
protein_button = tk.Button()
dairy_button = tk.Button()
veggie_button = tk.Button()
recipe_card1 = tk.Button()
recipe_card2 = tk.Button()
recipe_card3 = tk.Button

# Creating the page for Shoppinglist on home page
def shoppinglist():
    # Create new top-level window for the shopping list
    root = tk.Toplevel()
    root.title('Shopping List')
    root.geometry('500x550')
    # Load and resize the shopping list image
    img = Image.open('images/shopping_list.png')
    img = img.resize((750, 550), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    lab = tk.Label(root, image=pic)
    lab.pack()

    # list to store shopping items
    shopping_list = []

    # Create and pack widgets
    label = tk.Label(root, text='Shopping List:', font='Quicksand 22 bold', foreground='#D4A9D4', bg='white')
    label.place(x=175, y=85)

    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=21, height=15)
    listbox.place(x=157, y=166)

    # Create an entry for adding new items to the shopping list
    add_entry = tk.Entry(root, width=22)
    add_entry.place(x=150, y=127)
    ToolTip(add_entry, msg='Fill in the item you want to add:')

    # Create a button to add items using the add_item function
    # The lambda command is used to pass parameters to the command function
    add_button = tk.Button(root, text='Add Item', font='Quicksand 12 bold', bg='#D4A9D4', bd='0', fg='#D695CF',
                           command=lambda: add_item(add_entry=add_entry,
                                                    listbox=listbox,
                                                    shopping_list=shopping_list,
                                                    messagebox=messagebox))
    add_button.place(x=160, y=432)

    # Create a button to save the shopping list using the save_list function
    save_button = tk.Button(root, text='Save List', font='Quicksand 12 bold', bg='#D4A9D4', bd='0', fg='#D695CF',
                            command=lambda: save_list(listbox=listbox,
                                                      messagebox=messagebox,
                                                      shopping_list=shopping_list))
    save_button.place(x=260, y=432)

    # Run the main loop for the shopping list window
    root.mainloop()


def info():
    # Open the link when the info button is clicked
    webbrowser.open('https://foodsharing.de/?page=fairteiler&bid=158')

def info2():
    # Open the link when the info button is clicked
    webbrowser.open('https://www.eufic.org/en/explore-seasonal-fruit-and-vegetables-in-europe')

# Creating the Seasonal calender page as part of the open fridge menu
def calender_page():
    # Create a new top-level window for the seasonal calendar
    root = tk.Toplevel()
    root.title('Seasonal Calender')
    root.geometry('500x500')
    # Load and resize the seasonal calendar image
    img = Image.open('images/seasonal_calender.png')
    img = img.resize((500, 500), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)

    # Create a label to display the seasonal calendar image
    lab = tk.Label(root, image=pic)
    lab.pack()

    info_button2 = CircleButton(root, text='i', font='Quicksand 13 bold', width=30, bg='#D4A9D4',
                                bd='0', fg='white', command=info2)
    info_button2.place(x=10, y=10)
    ToolTip(info_button2, msg='Click here for more information about seasonal foods')

    root.mainloop()


# The following code for the expirationdatechecker is mainly AI generated and only used for prototype purpose
# Creating page for expiration date checker
def expiration_checker():
    # Food groups with examples and associated expiration periods (in days) for the expiration date checker
    food_groups = {
        'Dairy': {
            'Butter': 91,
            'Cheese': 91,
            'Cottage Cheese': 7,
            'Cream': 30,
            'Feta Cheese': 60,
            'Milk': 7,
            'Yogurt': 14,
            'Sour Cream': 21,
            'Ricotta Cheese': 7,
            'Whipped Cream': 30,
        },
        'Fruits': {
            'Apple': 21,
            'Banana': 7,
            'Grapes': 14,
            'Orange': 28,
            'Strawberries': 7,
            'Pineapple': 5,
            'Mango': 7,
            'Watermelon': 14,
            'Kiwi': 28,
        },
        'Protein': {
            'Beef': 5,
            'Chicken': 5,
            'Eggs': 35,
            'Fish': 4,
            'Lentils': 365,
            'Tofu': 35,
            'Salmon': 6,
            'Turkey': 5,
        },
        'Veggies': {
            'Broccoli': 5,
            'Carrots': 28,
            'Cucumbers': 14,
            'Spinach': 7,
            'Tomatoes': 14,
            'Bell Peppers': 14,
            'Zucchini': 14,
            'Sweet Potatoes': 35,
            'Onions': 60,
        },
    }  # more food groups and examples can be added as needed

    # Create the main window for the expiration date checker
    root = tk.Tk()
    root.title('Expiration Date Checker')
    root.geometry('300x270')
    root.configure(background='#D4A9D4')

    # Create and pack widgets
    label_food_group = tk.Label(root, text='Select Food Group:', font='Quicksand 12 bold', bg='#D4A9D4', bd='0',
                                fg='white')
    label_food_group.pack(pady=10)

    # Create a variable to store selected food group
    food_group_var = tk.StringVar(root)
    food_group_var.set(list(food_groups.keys())[0])  # Set default value

    # Create a dropdown menu for selecting the food group
    food_group_menu = tk.OptionMenu(root, food_group_var, *food_groups.keys(),
                                    command=lambda _: update_food_items(food_group_var=food_group_var,
                                                                      food_groups=food_groups,
                                                                      food_item_menu=food_item_menu,
                                                                      food_item_var=food_item_var,
                                                                      entry_purchase_date=entry_purchase_date))
    food_group_menu.pack(pady=10)

    # Create a variable to store selected food item
    food_item_var = tk.StringVar(root)
    food_group = food_group_var.get()
    food_item_var.set(list(food_groups[food_group].keys())[0])  # Set default value

    label_food_item = tk.Label(root, text='Select Food Item:', font='Quicksand 12 bold', bg='#D4A9D4', bd='0',
                               fg='white')
    label_food_item.pack(pady=5)

    # Create a dropdown menu for selecting the food item
    food_item_menu = tk.OptionMenu(root, food_item_var, *food_groups[food_group].keys())
    food_item_menu.pack(pady=10)

    label_purchase_date = tk.Label(root, font='Quicksand 12 bold', bg='#D4A9D4', bd='0', fg='white',
                                   text="Enter Purchase Date (DD.MM.YYYY):")
    label_purchase_date.pack(pady=5)

    # Create an entry box for entering the purchase date
    entry_purchase_date = tk.Entry(root, width=20)
    entry_purchase_date.pack(pady=5)

    # Create a button to trigger the expiration check
    check_button = tk.Button(root, text='Check Expiration', font='Quicksand 12 bold', bg='#D4A9D4', bd='0',
                             fg='#D4A9D4', command=lambda: check_expiration(food_group_var=food_group_var,
                                                                            food_item_var=food_item_var,
                                                                            entry_purchase_date=entry_purchase_date,
                                                                            messagebox=messagebox,
                                                                            food_groups=food_groups))
    check_button.pack(pady=10)

    # Run the main loop for the expiration date checker window
    root.mainloop()

# Creating dairy page for food compartment
def dairy_page():
    # Global variable to store the recipe card button
    global recipe_card1
    # Create a new window for the dairy compartment
    root = tk.Toplevel()
    root.geometry('580x300')
    root.title('Dairy Compartment')
    # Load and display an image for the dairy compartment
    img = Image.open('images/dairy_compartment.png')
    img = img.resize((670, 300), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    # Create a button in the food compartment popup for the recipe card
    recipe_card1 = tk.Button(root, text='Recipe Card: Chocolate Chip Cookies', font='Quicksand 9 bold', bg='#D4A9D4',
                             bd='0', fg='#D695CF', width=22, command=recipe_cookie)
    recipe_card1.place(x=41, y=15)

    root.mainloop()

# Create protein page
def protein_page():
    # Create a new window for the protein compartment
    root = tk.Toplevel()
    root.geometry('580x300')
    root.title('Protein Compartment')
    # Load and display an image for the protein compartment
    img = Image.open('images/protein_compartment.png')
    img = img.resize((670, 300), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    # Create a button in the food compartment popup for the recipe card
    recipe_card4 = tk.Button(root, text='Recipe Card: Veggie Tofu Bowl', font='Quicksand 9 bold', bg='#D4A9D4', bd='0',
                             fg='#D695CF', width=18, command=recipe_tofu)
    recipe_card4.place(x=30, y=15)

    root.mainloop()

# Create veggie page
def veggie_page():
    # Global variables to store recipe card buttons
    global recipe_card2, recipe_card3
    # Create a new window for the veggie compartment
    root = tk.Toplevel()
    root.geometry('500x320')
    root.title('Veggie Compartment')
    # Load and display an image for the veggie compartment
    img = Image.open('images/veggie_compartment.png')
    img = img.resize((510, 300), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    # Create buttons in the food compartment popup for recipe cards
    recipe_card2 = tk.Button(root, text='Recipe Card: Cauliflower Zing', font='Quicksand 9 bold', bg='#D4A9D4', bd='0',
                             fg='#D695CF', width=18, command=recipe_cauliflower)
    recipe_card2.place(x=10, y=257)

    recipe_card3 = tk.Button(root, text='Recipe Card: Zucchini Fries', font='Quicksand 9 bold', bg='#D4A9D4', bd='0',
                             fg='#D695CF', width=17, command=recipe_zucchini)
    recipe_card3.place(x=10, y=280)

    root.mainloop()


# Create pop up in food compartment for recipe card
def recipe_cookie():
    # Create a new window for the recipe card
    root = tk.Toplevel()
    root.geometry('600x400')
    root.title('Recipe Card: Chocolate Chip Cookies')
    # Load and display an image for the recipe card
    img = Image.open('images/Recipe_Card1.png')
    img = img.resize((600, 400), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    root.mainloop()

# Create pop up in food compartment for recipe card
def recipe_cauliflower():
    # Create a new window for the recipe card
    root = tk.Toplevel()
    root.geometry('600x400')
    root.title('Recipe Card: Cauliflower Zing')
    # Load and display an image for the recipe card
    img = Image.open('images/Recipe_Card2.png')
    img = img.resize((600, 400), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    root.mainloop()

# Create pop up in food compartment for recipe card
def recipe_zucchini():
    # Create a new window for the recipe card
    root = tk.Toplevel()
    root.geometry('600x400')
    root.title('Recipe Card: Zucchini Fries')
    # Load and display an image for the recipe card
    img = Image.open('images/Recipe_Card3.png')
    img = img.resize((600, 400), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    root.mainloop()

# Create pop up in food compartment for recipe card
def recipe_tofu():
    # Create a new window for the recipe card
    root = tk.Toplevel()
    root.geometry('600x400')
    root.title('Recipe Card: Veggie Tofu Bowl')
    # Load and display an image for the recipe card
    img = Image.open('images/Recipe_Card4.png')
    img = img.resize((600, 400), Image.LANCZOS)
    pic = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=pic)
    label.pack()

    root.mainloop()

# Running the main loop for GUI
root.mainloop()