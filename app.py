from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Extended sample recipes with full ingredient lists and impact metrics
sample_recipes = [
    {
        "name": "Leftover Vegetable Stir Fry",
        "description": "A quick stir-fry that transforms leftover vegetables into a delicious meal.",
        "co2_savings": 10,
        "money_saved": 5,
        "image": "https://via.placeholder.com/400?text=Vegetable+Stir+Fry",
        "ingredients": ["broccoli", "carrot", "bell pepper", "soy sauce", "garlic", "ginger"]
    },
    {
        "name": "Bread Pudding",
        "description": "Uses stale bread to create a comforting dessert.",
        "co2_savings": 8,
        "money_saved": 3,
        "image": "https://via.placeholder.com/400?text=Bread+Pudding",
        "ingredients": ["bread", "milk", "egg", "cinnamon", "vanilla extract", "raisins"]
    },
    {
        "name": "Soup of the Day",
        "description": "A hearty soup that repurposes a variety of leftovers.",
        "co2_savings": 12,
        "money_saved": 6,
        "image": "https://via.placeholder.com/400?text=Soup+of+the+Day",
        "ingredients": ["tomato", "onion", "carrot", "celery", "garlic", "bay leaf", "olive oil"]
    },
    {
        "name": "Pasta Frittata",
        "description": "A savory frittata using leftover pasta, eggs, and cheese.",
        "co2_savings": 9,
        "money_saved": 4,
        "image": "https://via.placeholder.com/400?text=Pasta+Frittata",
        "ingredients": ["pasta", "egg", "cheddar cheese", "spinach", "parmesan", "black pepper"]
    },
    {
        "name": "Rice Pilaf with Leftover Vegetables",
        "description": "A flavorful rice pilaf that incorporates your leftover veggies.",
        "co2_savings": 11,
        "money_saved": 5,
        "image": "https://via.placeholder.com/400?text=Rice+Pilaf",
        "ingredients": ["rice", "carrot", "peas", "bell pepper", "onion", "vegetable broth", "parsley"]
    },
    {
        "name": "Chickpea Curry",
        "description": "A hearty and spicy chickpea curry using pantry staples and leftovers.",
        "co2_savings": 14,
        "money_saved": 7,
        "image": "https://via.placeholder.com/400?text=Chickpea+Curry",
        "ingredients": ["chickpeas", "tomato", "onion", "garlic", "ginger", "curry powder", "coconut milk", "spinach"]
    },
    {
        "name": "Mixed Leftover Salad",
        "description": "A refreshing salad made with assorted leftover vegetables and fruits.",
        "co2_savings": 7,
        "money_saved": 3,
        "image": "https://via.placeholder.com/400?text=Mixed+Salad",
        "ingredients": ["lettuce", "tomato", "cucumber", "bell pepper", "apple", "walnuts", "olive oil", "lemon juice"]
    },
    {
        "name": "Fruit Smoothie Bowl",
        "description": "A vibrant smoothie bowl using leftover fruits and yogurt.",
        "co2_savings": 6,
        "money_saved": 2,
        "image": "https://via.placeholder.com/400?text=Smoothie+Bowl",
        "ingredients": ["banana", "strawberry", "blueberry", "yogurt", "honey", "granola"]
    }
]

@app.route('/')
def index():
    # Overall summary stats (dummy data)
    summary = {
        'co2_savings': 150,  # in kilograms
        'money_saved': 75,   # in dollars
        'recipes_used': 10   # number of recipes tried
    }
    return render_template('index.html', summary=summary, recipes=sample_recipes)

@app.route('/search', methods=['GET'])
def search():
    ingredients_str = request.args.get('ingredients', '')
    # Create a list from comma-separated string, trimmed and lowercased
    user_ingredients = [ing.strip().lower() for ing in ingredients_str.split(',') if ing.strip()]
    matching_recipes = []
    for recipe in sample_recipes:
        recipe_ingredients = [ing.lower() for ing in recipe.get('ingredients', [])]
        # Include recipe if any user ingredient is found in the recipe's ingredients
        if any(ingredient in recipe_ingredients for ingredient in user_ingredients):
            matching_recipes.append(recipe)
    return jsonify(matching_recipes)

if __name__ == '__main__':
    app.run(debug=True)
