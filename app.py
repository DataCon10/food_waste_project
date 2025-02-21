from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Overall summary stats (dummy data)
    summary = {
        'co2_savings': 150,       # in kilograms
        'money_saved': 75,        # in dollars
        'recipes_used': 10        # number of recipes tried
    }

    # Sample recipes with impact metrics and image URLs (dummy data)
    sample_recipes = [
        {
            "name": "Leftover Vegetable Stir Fry",
            "description": "A quick stir-fry that transforms leftover vegetables into a delicious meal.",
            "co2_savings": 10,    # in kilograms per recipe
            "money_saved": 5,     # in dollars per recipe
            "image": "https://via.placeholder.com/400?text=Vegetable+Stir+Fry"
        },
        {
            "name": "Bread Pudding",
            "description": "Uses stale bread to create a comforting dessert.",
            "co2_savings": 8,
            "money_saved": 3,
            "image": "https://via.placeholder.com/400?text=Bread+Pudding"
        },
        {
            "name": "Soup of the Day",
            "description": "A hearty soup that repurposes a variety of leftovers.",
            "co2_savings": 12,
            "money_saved": 6,
            "image": "https://via.placeholder.com/400?text=Soup+of+the+Day"
        }
    ]

    return render_template('index.html', summary=summary, recipes=sample_recipes)

if __name__ == '__main__':
    app.run(debug=True)
