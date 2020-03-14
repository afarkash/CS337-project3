import transform_recipe
import scraper.py

class Chatbot:
    def __init__(self):
        transformer = RecipeTransformer()
        rf = RecipeFetcher()
        url = ''
        title = ''
        ingredients = []
        directions = []
        got_recipe = True
        directions_dict = {}


    def get_url(self, url):
        self.url = url

    def get_recipe(self):
        recipe_dict = rf.scrape_recipe(self.url)
        self.title = recipe_dict["title"]
        self.ingredients = recipe_dict["ingredients"]
        self.directions = recipe_dict["directions"]

    def print_ingredients(self):
        if(got_recipe):
            for ing in self.ingredients:
                print(ing)

    def print_directions(self):
        if(got_recipe):
            for i in range(len(self.ingredients) - 1):
                self.directions_dict[i] = self.directions[i]
                print(str(i) + ". " + self.directions[i])
    


        
