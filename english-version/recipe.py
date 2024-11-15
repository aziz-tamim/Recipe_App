import random
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Data for ingredients, recipes, and videos
ingredients = {
    "Rice": {"quantity": "1 cup", "price_per_unit": 40, "calories_per_unit": 200},
    "Meat": {"quantity": "200g", "price_per_unit": 150, "calories_per_unit": 300},
    "Vegetables": {"quantity": "300g", "price_per_unit": 50, "calories_per_unit": 80},
    "Lentils": {"quantity": "1 cup", "price_per_unit": 35, "calories_per_unit": 150},
    "Onion": {"quantity": "1 pc", "price_per_unit": 12, "calories_per_unit": 10},
    "Spices": {"quantity": "1 tbsp", "price_per_unit": 8, "calories_per_unit": 10},
}

cooking_steps = {
    "Pilaf": [
        "Rinse rice and soak for 20 minutes.",
        "Chop onion and meat.",
        "Heat oil, add meat and onion, and fry.",
        "Add rice, spices, water, and cook."
    ],
    "Biryani": [
        "Rinse rice and soak for 30 minutes.",
        "Marinate meat with spices.",
        "Cook meat with onion and tomatoes.",
        "Layer rice and meat, then cook on low heat."
    ]
}

cooking_time = {
    "Pilaf": {"time": "30 minutes", "temperature": "Medium heat"},
    "Biryani": {"time": "45 minutes", "temperature": "Low heat"}
}

video_urls = {
    "Pilaf": "https://youtu.be/OQWCirmPotc",
    "Biryani": "https://youtu.be/v-55n1M05IE"
}

# Functions for recipe generation and GUI actions
def show_ingredient_prices():
    prices_text = "Ingredient Prices:\n\n"
    for item, details in ingredients.items():
        prices_text += f"{item} ({details['quantity']}): {details['price_per_unit']} Taka\n"
    return prices_text

def generate_recipe(dish, servings):
    selected_ingredients = {
        "Pilaf": ["Rice", "Meat", "Onion", "Spices"],
        "Biryani": ["Rice", "Meat", "Onion", "Spices"]
    }.get(dish, [])

    ingredients_list = []
    total_cost = total_calories = 0

    for ingredient in selected_ingredients:
        data = ingredients[ingredient]
        cost = data["price_per_unit"] * servings
        calories = data["calories_per_unit"] * servings
        ingredients_list.append(f"{ingredient} ({data['quantity']})")
        total_cost += cost
        total_calories += calories

    recipe = f"Recipe for {dish}:\n\nIngredients:\n" + "\n".join(ingredients_list)
    recipe += f"\n\nCooking Steps:\n" + "\n".join(cooking_steps[dish])
    recipe += f"\n\nTime: {cooking_time[dish]['time']}, Temp: {cooking_time[dish]['temperature']}"
    recipe += f"\n\nTotal Cost: {total_cost} Taka\nTotal Calories: {total_calories} kcal"
    return recipe

def show_recipe():
    dish = dish_var.get()
    try:
        servings = int(servings_entry.get())
        if servings <= 0:
            raise ValueError
        recipe = generate_recipe(dish, servings)
        recipe_text.delete(1.0, tk.END)
        recipe_text.insert(tk.END, recipe)
        video_button.pack()
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number of servings.")

def show_prices():
    messagebox.showinfo("Ingredient Prices", show_ingredient_prices())

def play_video():
    dish = dish_var.get()
    url = video_urls.get(dish)
    if url:
        webbrowser.open(url)
    else:
        messagebox.showerror("Error", "Video not available.")

# GUI Setup
root = tk.Tk()
root.title("Recipe Generator")
root.geometry("500x600")

title_label = tk.Label(root, text="Food Recipe Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

dish_var = tk.StringVar()
dish_menu = tk.OptionMenu(root, dish_var, "Pilaf", "Biryani")
dish_menu.pack(pady=10)

servings_entry = tk.Entry(root, width=10)
servings_entry.pack(pady=5)
servings_entry.insert(0, "Servings")

generate_button = tk.Button(root, text="Generate Recipe", command=show_recipe)
generate_button.pack(pady=10)

price_button = tk.Button(root, text="Show Ingredient Prices", command=show_prices)
price_button.pack(pady=5)

recipe_text = tk.Text(root, wrap="word", height=15)
recipe_text.pack(pady=10)

video_button = tk.Button(root, text="Watch Video", command=play_video)

root.mainloop()
