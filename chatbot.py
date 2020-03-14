from transform_recipe import RecipeTransformer
import scraper

class Chatbot(RecipeTransformer):
    def __init__(self, recipe):
        super().__init__()
        # self.transformer = RecipeTransformer()
        # self.rf = scraper.RecipeFetcher()
        # self.url = ''
        # self.title = ''
        self.ingredients = self.original_recipe(recipe)['ingredients']
        self.directions = self.original_recipe(recipe)['directions']
        # self.got_recipe = True
        # self.directions_dict = {}


    # def get_url(self, url):
    #     self.url = url
    #
    # def get_recipe(self):
    #     recipe_dict = self.rf.scrape_recipe(self.url)
    #     self.title = recipe_dict["title"]
    #     self.ingredients = recipe_dict["ingredients"]
    #     self.directions = recipe_dict["directions"]
    #
    # def print_ingredients(self):
    #     if self.got_recipe:
    #         for ing in self.ingredients:
    #             print(ing)
    #
    # def print_directions(self):
    #     if self.got_recipe:
    #         for i in range(len(self.ingredients) - 1):
    #             self.directions_dict[i] = self.directions[i]
    #             print(str(i) + ". " + self.directions[i])

cb = Chatbot('meat lasagna')
print(cb.ingredients)


        
