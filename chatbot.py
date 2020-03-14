from transform_recipe import RecipeTransformer
import scraper
import nltk

class Chatbot():
    def __init__(self):
        self.transformer = RecipeTransformer()
        self.full_recipe = {}
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
        self.full_recipe = recipe_dict
        self.title = recipe_dict["title"]
        self.ingredients = recipe_dict["ingredients"]
        self.directions = recipe_dict["directions"]
        self.got_recipe = True

    def update(self):
        self.ingredients = self.full_recipe["ingredients"]
        self.directions = self.full_recipe["directions"]

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

    def more_healthy(self):
        self.full_recipe = self.transformer.transform_health(self.full_recipe, True)
        self.update()
        print("The recipe is now healthier. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def less_healthy(self):
        self.full_recipe = self.transformer.transform_health(self.full_recipe, False)
        self.update()
        print("The recipe is now less healthy. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def vegetarian(self):
        self.full_recipe = self.transformer.transform_to_vegetarian(self.full_recipe)
        self.update()
        print("The recipe is now vegetarian. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def carnivore(self):
        self.full_recipe = self.transformer.transform_to_carnivore(self.full_recipe)
        self.update()
        print("The recipe is now non-vegetarian. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def russify(self):
        self.full_recipe = self.transformer.transform_to_cuisine(self.full_recipe, "Russian")
        self.update()
        print("The recipe is now Russian-inspired. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def italicize(self):
        self.full_recipe = self.transformer.transform_to_cuisine(self.full_recipe, "Italian")
        self.update()
        print("The recipe is now Italian-inspired. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def double(self):
        self.full_recipe = self.transformer.double_quantity(self.full_recipe)
        self.update()
        print("The recipe quantity is now doubled. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def halve(self):
        self.full_recipe = self.transformer.halve_quantity(self.full_recipe)
        self.update()
        print("The recipe quantity is now halved. You can ask me to see the ingredients or the directions, or you can transform the recipe again.")

    def run(self):
        self.introduction()
        while (self.leave == False):
            self.user_input = input().lower()

            if(self.url == False):
                self.get_url(self.user_input)
                if(self.url == False):
                    continue
                else:
                    print("Great! Let's cook " + self.title[0] + ". You can ask me to see the ingredients or the directions, or you can transform the recipe.")

            elif("ingredients" in self.user_input):
                print("Here you go:")
                self.print_ingredients()

            elif("directions" in self.user_input):
                print("Here you go:")
                self.print_directions()
                print("Would you like to go through them step-by-step?")

            elif("yes" in self.user_input or "yeah" in self.user_input or "okay" in self.user_input or "ok" in self.user_input):
                self.curr_step()
                print("Let me know if you want to see the previous or next step.")

            elif("previous" in self.user_input):
                print("Here you go:")
                self.prev_step()

            elif("next" in self.user_input):
                print("Here you go:")
                self.next_step()

            elif("exit" in self.user_input or "quit" in self.user_input):
                self.exit()

            elif("how" in self.user_input):
                self.answer_how()

            elif("what" in self.user_input and "step" not in self.user_input):
                self.answer_what()

            elif("transform" in self.user_input or "change" in self.user_input):
                print("I can make this recipe more healthy, less health, vegetarian, non-vegetarian. I can transform it into a Russian or Italian dish. I can also double or halve the quantity.")
            
            elif("healthier" in self.user_input or "more healthy" in self.user_input):
                self.more_healthy()

            elif("more unhealthy" in self.user_input or "less healthy" in self.user_input):
                self.more_unhealthy()

            elif("vegetarian" in self.user_input and "non" not in self.user_input):
                self.vegetarian()

            elif(("vegetarian" in self.user_input and "non" in self.user_input) or "carnivore" in self.user_input):
                self.carnivore()

            elif("russian" in self.user_input):
                self.russify()

            elif("italian" in self.user_input):
                self.italicize()
            
            elif("double" in self.user_input):
                self.double()

            elif("halve" in self.user_input or "half" in self.user_input):
                self.halve()

            elif(self.user_input in ["great", "awesome", "thanks", "thank you", "thanks!", "hi", "hello", "yo", "oh"]):
                print("Yep!")

            else:
                print("I didn't understand that. I can get you ingredients and directions, and I can point you to resources that answer your 'how' and 'what' questions. Type 'exit' to leave the chat.")
chatbot = Chatbot()
chatbot.run()
            
        

            



            
            
            
    
