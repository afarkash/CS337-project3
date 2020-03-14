import transform_recipe
import scraper

class Chatbot:
    def __init__(self):
        self.transformer = transform_recipe.RecipeTransformer()
        self.rf = scraper.RecipeFetcher()
        self.url = False
        self.title = ''
        self.ingredients = []
        self.directions = []
        self.got_recipe = False
        self.leave = False
        self.directions_dict = {}
        self.current_step = 0
        self.user_input = ''


    def get_url(self, url):
        if("https://www.allrecipes.com/recipe/" not in url):
            print("I only take URLs from allrecipes.com. Please try again.")
        else:
            self.url = url
            self.get_recipe()

    def get_recipe(self):
        recipe_dict = self.rf.scrape_recipe(self.url)
        self.title = recipe_dict["title"]
        self.ingredients = recipe_dict["ingredients"]
        self.directions = recipe_dict["directions"]
        self.got_recipe = True

    def print_ingredients(self):
        if(self.got_recipe):
            for ing in self.ingredients:
                print(ing)

    def print_directions(self):
        if(self.got_recipe):
            for i in range(len(self.directions) - 1):
                self.directions_dict[i] = self.directions[i]
                print(str(i) + ". " + self.directions[i])
    
    def next_step(self):
        if self.current_step < len(self.directions_dict) - 1:
            self.current_step +=1
            print(self.directions_dict[self.current_step])
        else:
            print("That was the last step!")

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -=1
            print(self.directions_dict[self.current_step])
        else:
            print("That was the first step!")

    def curr_step(self):
        print(self.directions_dict[self.current_step])

    def nth_step(self, n):
        print("Here it is:")
        self.current_step = n
        self.curr_step()

    def answer_how(self):
        query = self.user_input.replace(" ", "+")
        print("I have a video reference for you: " + "https://www.youtube.com/results?search_query=" + query)

    def answer_what(self):
        query = self.user_input.replace(" ", "+")
        print("I have a reference for you: " + "https://www.google.com/search?q=" + query)

    def introduction(self):
        print("Hi! I'm Pierce! I'm here to help you get cooking! Enter a URL from allrecipes.com to start. Enter 'exit' at any time to leave the chat.")

    def exit(self):
        print("Happy Cooking!")
        self.leave = True

    def run(self):
        self.introduction()
        while (self.leave == False):
            self.user_input = input().lower()

            if(self.url == False):
                self.get_url(self.user_input)
                print("Great! Let's cook " + self.title[0] + ". You can ask me to see the ingredients or the directions, or you can transform the recipe.")

            if("ingredients" in self.user_input):
                print("Here you go:")
                self.print_ingredients()

            if("directions" in self.user_input):
                print("Here you go:")
                self.print_directions()
                print("Would you like to go through them step-by-step?")

            if("yes" in self.user_input):
                self.curr_step()
                print("Let me know if you want to see the previous or next step.")

            if("previous" in self.user_input):
                print("Here you go:")
                self.prev_step()

            if("next" in self.user_input):
                print("Here you go:")
                self.next_step()

            if("exit" in self.user_input or "quit" in self.user_input):
                self.exit()

            if("how" in self.user_input):
                self.answer_how()

            if("what" in self.user_input):
                self.answer_what()

chatbot = Chatbot()
chatbot.run()

            
        

            



            
            
            
    
