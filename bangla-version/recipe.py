import random
import tkinter as tk
from tkinter import messagebox
import webbrowser

# ========== উপাদানসমূহ এবং তাদের বর্তমান মূল্য ========== #
ingredients = {
    "চাল": {"quantity": "১ কাপ", "price_per_unit": 40, "calories_per_unit": 200},
    "মাংস": {"quantity": "২০০ গ্রাম", "price_per_unit": 150, "calories_per_unit": 300},
    "সবজি": {"quantity": "৩০০ গ্রাম", "price_per_unit": 50, "calories_per_unit": 80},
    "ডাল": {"quantity": "১ কাপ", "price_per_unit": 35, "calories_per_unit": 150},
    "দই": {"quantity": "২ চামচ", "price_per_unit": 30, "calories_per_unit": 20},
    "টমেটো": {"quantity": "২টি", "price_per_unit": 20, "calories_per_unit": 15},
    "পেঁয়াজ": {"quantity": "১টি", "price_per_unit": 12, "calories_per_unit": 10},
    "রসুন": {"quantity": "৩ কোয়া", "price_per_unit": 8, "calories_per_unit": 5},
    "মশলা": {"quantity": "১ চামচ", "price_per_unit": 8, "calories_per_unit": 10},
    "নুন": {"quantity": "স্বাদ অনুযায়ী", "price_per_unit": 4, "calories_per_unit": 0},
    "চিনি": {"quantity": "১ চামচ", "price_per_unit": 8, "calories_per_unit": 20},
    "আলু": {"quantity": "২টি", "price_per_unit": 16, "calories_per_unit": 50}
}

# ========== রান্নার পদ্ধতি ========== #
cooking_methods = [
    "ভাজা", "সেদ্ধ", "তেলে ভাজা", "কাবাব", "পেঁয়াজ দিয়ে রান্না", "রান্নার মিশ্রণ"
]

# ========== রান্নার ধাপ ========== #
cooking_steps = {
    "পোলাও": [
        "চাল ধুয়ে ২০ মিনিট পানি ফেলে রাখুন।",
        "পেঁয়াজ এবং মাংস কেটে নিন।",
        "তেল গরম করে মাংস ও পেঁয়াজ ভেজে নিন।",
        "চাল, মশলা, পানি দিয়ে রান্না করুন।"
    ],
    "বিরিয়ানি": [
        "চাল ধুয়ে ৩০ মিনিট পানিতে ভিজিয়ে রাখুন।",
        "মাংস, মশলা, পেঁয়াজ কেটে রাখুন।",
        "মাংস এবং মশলা মিশিয়ে কিছু সময় ম্যারিনেট করুন।",
        "চাল, মাংস, এবং মশলা একসাথে ঢেলে রান্না করুন।"
    ],
    "খিচুড়ি": [
        "চাল ধুয়ে ১৫ মিনিট পানিতে ভিজিয়ে রাখুন।",
        "পানি ফুটিয়ে চাল যোগ করুন এবং সেদ্ধ হতে দিন।"
    ],
    "সবজি তরকারি": [
        "সবজি কেটে নিন।",
        "পেঁয়াজ, রসুন, মশলা দিয়ে তেল গরম করে ভাজুন।",
        "সবজি দিয়ে কিছু সময় রান্না করুন।"
    ],
    "ডাল ভাত": [
        "ডাল সেদ্ধ করতে রাখুন।",
        "ভাত রান্না করুন।",
        "ডালের সাথে গরম মশলা দিয়ে ঝোল তৈরি করুন।"
    ],
    "গরুর মাংস": [
        "গরুর মাংস সেদ্ধ করে রাখুন।",
        "পেঁয়াজ, রসুন, মশলা দিয়ে মাংস রান্না করুন।",
        "গরম মশলা দিয়ে কারি তৈরি করুন।"
    ],
    "মুরগির মাংস": [
        "মুরগির মাংস ধুয়ে কেটে নিন।",
        "পেঁয়াজ, রসুন, আদা কুচি করে মাংসে মাখিয়ে কিছু সময় ম্যারিনেট করুন।",
        "তেল গরম করে পেঁয়াজ, রসুন, আদা ভেজে মুরগির মাংস যোগ করুন।",
        "মাংস সেদ্ধ হলে, মশলা দিয়ে রান্না করুন।",
        "গরম মশলা দিয়ে মুরগির মাংস পরিবেশন করুন।"
    ]
}

# ========== রান্নার সময় এবং তাপমাত্রা ========== #
cooking_time = {
    "পোলাও": {"time": "৩০ মিনিট", "temperature": "মাঝারি তাপ"},
    "বিরিয়ানি": {"time": "৪৫ মিনিট", "temperature": "মাঝারি তাপ"},
    "খিচুড়ি": {"time": "২০ মিনিট", "temperature": "মাঝারি তাপ"},
    "সবজি তরকারি": {"time": "২৫ মিনিট", "temperature": "মাঝারি তাপ"},
    "ডাল ভাত": {"time": "৩০ মিনিট", "temperature": "মাঝারি তাপ"},
    "গরুর মাংস": {"time": "৪০ মিনিট", "temperature": "মাঝারি তাপ"},
    "মুরগির মাংস": {"time": "৪৫ মিনিট", "temperature": "মাঝারি তাপ"}
}

# ========== উপাদানের খরচ দেখান ========== #
def show_ingredient_prices():
    prices_text = "বর্তমান বাজার অনুযায়ী উপাদানের মূল্য:\n\n"
    for item, details in ingredients.items():
        prices_text += f"{item} ({details['quantity']}): {details['price_per_unit']} টাকা\n"
    return prices_text

# ========== ভিডিও URL (Web Browser) ========== #
video_urls = {
    "পোলাও": "https://youtu.be/OQWCirmPotc?t=3",
    "বিরিয়ানি": "https://youtu.be/v-55n1M05IE?t=4",
    "খিচুড়ি": "https://youtu.be/3KqFWcFlxcI?t=5",
    "সবজি তরকারি": "https://youtu.be/tchbuipZ88k?t=3",
    "ডাল ভাত": "https://youtu.be/1QF0KAgkZEI?t=2",
    "গরুর মাংস": "https://youtu.be/1x8IF78ztvU",
    "মুরগির মাংস": "https://youtu.be/g4xgTP447pE?t=3"
}

# ========== রান্নার প্রক্রিয়া ========== #
def generate_recipe(dish_choice, servings):
    dish = dish_choice
    
    # Get the specific ingredients for the selected dish
    if dish == "পোলাও":
        selected_ingredients = ["চাল", "মাংস", "পেঁয়াজ", "মশলা"]
    elif dish == "বিরিয়ানি":
        selected_ingredients = ["চাল", "মাংস", "পেঁয়াজ", "মশলা"]
    elif dish == "খিচুড়ি":
        selected_ingredients = ["চাল", "ডাল", "পেঁয়াজ", "মশলা"]
    elif dish == "সবজি তরকারি":
        selected_ingredients = ["সবজি", "পেঁয়াজ", "রসুন", "মশলা"]
    elif dish == "ডাল ভাত":
        selected_ingredients = ["চাল", "ডাল", "পেঁয়াজ", "মশলা"]
    elif dish == "গরুর মাংস":
        selected_ingredients = ["মাংস", "পেঁয়াজ", "রসুন", "মশলা"]
    elif dish == "মুরগির মাংস":
        selected_ingredients = ["মাংস", "পেঁয়াজ", "রসুন", "মশলা"]
# মোট খরচ ও ক্যালোরি কাউন্টার হিসাব করার ফাংশন
  
    # Adjust quantities based on servings
    selected_ingredients_with_quantity = []
    total_cost = 0
    total_calories = 0

    for ingredient in selected_ingredients:
        ingredient_quantity = ingredients[ingredient]["quantity"]
        price_per_unit = ingredients[ingredient]["price_per_unit"]
        calories_per_unit = ingredients[ingredient]["calories_per_unit"]
        # Adjusting ingredient quantities based on servings
        adjusted_quantity = f"{int(servings)}x {ingredient_quantity}"
        selected_ingredients_with_quantity.append(f"{ingredient} ({adjusted_quantity})")
        total_calories += calories_per_unit * servings
        total_cost += price_per_unit * servings

    method = random.choice(cooking_methods)
    time = cooking_time[dish]["time"]
    temperature = cooking_time[dish]["temperature"]
    steps = cooking_steps[dish]
    
    recipe = f"🔸 আজকের রেসিপি: {dish}\n\n" \
             f"🔹 উপাদানসমূহ:\n" + "\n".join([f"- {ingredient}" for ingredient in selected_ingredients_with_quantity]) + "\n" \
             f"🔸🔸🔸 উপাদানের পরিমান {servings} জন মানুষের হিসাব অনুযায়ি পরিমান মত দিতে হবে\n\n\n" \
             f"🔹 রান্নার পদ্ধতি: {method}\n" \
             f"🔹 রান্নার সময়: {time}\n" \
             f"🔹 রান্নার তাপমাত্রা: {temperature}\n\n" \
             f"🔸 রান্নার ধাপসমূহ:\n"\
             
    for idx, step in enumerate(steps, 1):
        recipe += f"{idx}. {step}\n"

    # Add total cost
    recipe += f"\n🔸 মোট খরচ: {total_cost} টাকা\n"
    recipe += f"🔸 মোট ক্যালোরি: {total_calories} ক্যালোরি\n"
    return recipe

# ========== ভিডিও চালানোর প্রক্রিয়া ========== #
def play_video(dish_choice):
    video_url = video_urls.get(dish_choice)  # Get the corresponding video URL for the selected dish
    if video_url:
        webbrowser.open(video_url)  # Open the video URL in the default web browser
    else:
        messagebox.showerror("Error", "ভিডিও URL পাওয়া যায়নি!")

# ========== GUI তৈরি ========== #
def show_recipe():
    selected_dish = dish_var.get()  
    servings = servings_entry.get()
    
    if not servings.isdigit() or int(servings) <= 0:
        messagebox.showwarning("Warning", "অনুগ্রহ করে সঠিক সংখ্যা দিন!")
        return
    
    servings = int(servings)
    
    if selected_dish == "":
        messagebox.showwarning("Warning", "অনুগ্রহ করে একটি খাবার নির্বাচন করুন!")
        return

    recipe = generate_recipe(selected_dish, servings)
    
    recipe_text.delete(1.0, tk.END)
    recipe_text.insert(tk.END, recipe)
    
    # Show the video button after recipe is generated
    video_button.pack(pady=5)

def show_prices():
    prices_info = show_ingredient_prices()
    messagebox.showinfo("উপাদানের মূল্য তালিকা", prices_info)

# ========== Tkinter GUI সেটআপ ========== #
root = tk.Tk()
root.title("খাদ্য রেসিপি জেনারেটর")
root.geometry("500x700")
root.configure(bg="#f7e8c8")

# GUI Elements
title_label = tk.Label(root, text="রেসিপি তৈরি", font=("Arial", 16, "bold"), fg="#4a403a", bg="#f7e8c8")
title_label.pack(pady=10)

dish_label = tk.Label(root, text="খাবারের ধরন নির্বাচন করুন:", font=("Arial", 12, "bold"), fg="#4a403a", bg="#f7e8c8")
dish_label.pack(pady=5)

dish_var = tk.StringVar()
dish_menu = tk.OptionMenu(root, dish_var, "পোলাও", "বিরিয়ানি", "খিচুড়ি", "সবজি তরকারি", "ডাল ভাত", "গরুর মাংস", "মুরগির মাংস")
dish_menu.configure(bg="#b4a7a1", fg="black", font=("Arial", 10))
dish_menu.pack(pady=5)

servings_label = tk.Label(root, text="কতজন মানুষের জন্য?", font=("Arial", 12, "bold"), fg="#4a403a", bg="#f7e8c8")
servings_label.pack(pady=5)

servings_entry = tk.Entry(root, font=("Arial", 12), width=10)
servings_entry.pack(pady=5)

generate_button = tk.Button(root, text="রেসিপি তৈরি করুন", command=show_recipe, font=("Arial", 12, "bold"), bg="#d4a373", fg="white", activebackground="#d49973")
generate_button.pack(pady=15)

# New Button to Show Prices
prices_button = tk.Button(root, text="উপাদানের মূল্য দেখুন", command=show_prices, font=("Arial", 12, "bold"), bg="#d4a373", fg="white")
prices_button.pack(pady=5)

video_button = tk.Button(root, text="ভিডিও দেখুন", command=lambda: play_video(dish_var.get()), font=("Arial", 12, "bold"), bg="#d4a373", fg="white")
recipe_text = tk.Text(root, width=50, height=18, font=("Arial", 10, "bold"), wrap="word", bg="#fffaf0", fg="#4a403a")
recipe_text.pack(padx=20, pady=10)

root.mainloop()
