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
        current_step = 0
        user_input = ''


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
    
    def next_step(self):
        if self.current_step < len(directions_dict) - 1:
            self.current_step +=1
            print(self.directions_dict[self.current_step])

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -=1
            print(self.directions_dict[self.current_step])

    def answer_how(self):
        query = self.user_input.replace(" ", "+")
        print("I have a video reference for you: " + "https://www.youtube.com/results?search_query=" + query)

    def answer_what(self):
        query = self.user_input.replace(" ", "+")
        print("I have a reference for you: " + "https://www.google.com/search?q=" + query)

    
       
        
