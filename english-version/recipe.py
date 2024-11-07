import random
import tkinter as tk
from tkinter import messagebox

# ========== Ingredients and Their Quantities ========== #
ingredients = {
    "Rice": "1 cup",
    "Meat": "200 grams",
    "Vegetables": "300 grams",
    "Lentils": "1 cup",
    "Yogurt": "2 tablespoons",
    "Tomato": "2 pieces",
    "Onion": "1 piece",
    "Garlic": "3 cloves",
    "Spices": "1 tablespoon",
    "Salt": "To taste",
    "Sugar": "1 tablespoon",
    "Potato": "2 pieces"
}

# ========== Cooking Methods ========== #
cooking_methods = [
    "Fried", "Boiled", "Fried in oil", "Kebab", "Cooked with onions", "Cooking mix"
]

# ========== Cooking Steps ========== #
cooking_steps = {
    "Pulao": [
        "Wash the rice and let it sit in water for 20 minutes.",
        "Chop the onions and meat.",
        "Heat oil, then fry the meat and onions.",
        "Add rice, spices, water, and cook."
    ],
    "Biryani": [
        "Wash the rice and soak in water for 30 minutes.",
        "Chop the meat, spices, and onions.",
        "Marinate the meat with spices for some time.",
        "Add rice, meat, and spices together and cook."
    ],
    "Rice": [
        "Wash the rice and soak in water for 15 minutes.",
        "Boil water, add rice, and cook until done."
    ],
    "Vegetable Curry": [
        "Chop the vegetables.",
        "Fry onions, garlic, and spices in oil.",
        "Add vegetables and cook for a while."
    ],
    "Lentil and Rice": [
        "Cook the lentils until boiled.",
        "Cook the rice.",
        "Make a gravy with the lentils and hot spices."
    ]
}

# ========== Cooking Time and Temperature ========== #
cooking_time = {
    "Pulao": {"time": "30 minutes", "temperature": "Medium heat"},
    "Biryani": {"time": "45 minutes", "temperature": "Medium heat"},
    "Rice": {"time": "20 minutes", "temperature": "Medium heat"},
    "Vegetable Curry": {"time": "25 minutes", "temperature": "Medium heat"},
    "Lentil and Rice": {"time": "30 minutes", "temperature": "Medium heat"}
}

# ========== Recipe Generation ========== #
def generate_recipe(dish_choice):
    dish = dish_choice
    selected_ingredients = random.sample(list(ingredients.keys()), 4)
    selected_ingredients_with_quantity = [f"{ingredient} ({ingredients[ingredient]})" for ingredient in selected_ingredients]
    method = random.choice(cooking_methods)
    time = cooking_time[dish]["time"]
    temperature = cooking_time[dish]["temperature"]
    steps = cooking_steps[dish]
    recipe = f"🔸 Today's Recipe: {dish}\n\n" \
             f"🔹 Ingredients:\n" + "\n".join([f"- {ingredient}" for ingredient in selected_ingredients_with_quantity]) + "\n\n" \
             f"🔹 Cooking Method: {method}\n" \
             f"🔹 Cooking Time: {time}\n" \
             f"🔹 Cooking Temperature: {temperature}\n\n" \
             f"🔸 Steps:\n"
              
    for idx, step in enumerate(steps, 1):
        recipe += f"{idx}. {step}\n"
        
    return recipe

# ========== GUI Creation ========== #
def show_recipe():
    selected_dish = dish_var.get()  
    
    if selected_dish == "":
        messagebox.showwarning("Warning", "Please select a dish!")
        return
    
    recipe = generate_recipe(selected_dish)
    
    recipe_text.delete(1.0, tk.END)
    recipe_text.insert(tk.END, recipe)

# ========== Tkinter GUI Setup ========== #
root = tk.Tk()
root.title("Food Recipe Generator")
root.geometry("500x500")
root.configure(bg="#f7e8c8")

# ========== Styling ========== #
title_label = tk.Label(root, text="Food Recipe Generator", font=("Arial", 16, "bold"), fg="#4a403a", bg="#f7e8c8")
title_label.pack(pady=10)

dish_label = tk.Label(root, text="Select a Dish Type:", font=("Arial", 12, "bold"), fg="#4a403a", bg="#f7e8c8")
dish_label.pack(pady=5)

dish_var = tk.StringVar()
dish_menu = tk.OptionMenu(root, dish_var, "Pulao", "Biryani", "Rice", "Vegetable Curry", "Lentil and Rice")
dish_menu.configure(bg="#b4a7a1", fg="black", font=("Arial", 10))
dish_menu.pack(pady=5)

generate_button = tk.Button(root, text="Generate Recipe", command=show_recipe, font=("Arial", 12, "bold"), 
                            bg="#d4a373", fg="white", activebackground="#d49973")
generate_button.pack(pady=15)

recipe_text = tk.Text(root, width=50, height=18, font=("Arial", 10, "bold"), wrap="word", bg="#fffaf0", fg="#4a403a")
recipe_text.pack(padx=20, pady=10)

# ========== Tkinter GUI Execution ========== #
root.mainloop()
