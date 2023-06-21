import itertools
import typer
import random
import configparser
from  pathlib import Path

import person
import place
import thing
from helpers import load_csv_file, save_to_abs_path, amount_of_names_callback
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()
app.add_typer(person.app, name="person")
app.add_typer(place.app, name="place")
app.add_typer(thing.app, name="thing")

APP_NAME = "NomenCLI"

@app.command()
def scramble(word, amount_of_names: Annotated[Optional[int], typer.Argument(callback=amount_of_names_callback)] = 10,
             save: Annotated[bool, typer.Option("--save", "-s")] = False):
    permutations = itertools.permutations([*word])
    permutations = ["".join(word) for word in permutations]
    
    # Select words.
    selection = []
    while amount_of_names != 0:
        random_word = random.choice(permutations)
        selection.append(random_word)
        permutations.remove(random_word)
        amount_of_names -= 1
    
    for word in selection:
        print(word)
        
    if save:
        print("Save this.")

@app.command()
def place():
    pass

@app.command()
def thing():
    pass

if __name__ == "__main__":
    app()