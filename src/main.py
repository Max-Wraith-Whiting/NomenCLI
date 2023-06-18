import itertools
import typer
import random
import configparser

app = typer.Typer()

@app.command()
def name():
    word = input("Enter a word that relates to that which intend to name. \n> ")
    permutations = itertools.permutations([*word])
    permutations = ["".join(word) for word in permutations]
    print("Enter the number of one the following words you like.")
    
    # Select 20 words or less word
    words_to_select = 20 if len(permutations) > 20 else len(permutations)
    selection = []
    while words_to_select != 0:
        random_word = random.choice(permutations)
        selection.append(random_word)
        permutations.remove(random_word)
        words_to_select -= 1
    
    count = 1
    for word in selection:
        print(f"\t {count}. {word}")
        count += 1
        
    print("Enter 0 for to generate more names:")
    
    chosen_word = None
    while chosen_word not in range(1,count):
        try:
            chosen_word = int(input("> "))
        except:
            print("Please enter a valid number.")
            
    print("\n Now that you have your word, try and say it. \n If you have trouble try adding some vowels around the troublesome parts.")
    word = selection[chosen_word - 1]
    print(f" {word} is an interesting choice to say the least.")

@app.command()
def person():
    pass

@app.command()
def place():
    pass

@app.command()
def thing():
    pass

if __name__ == "__main__":
    app()