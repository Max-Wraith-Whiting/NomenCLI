import itertools
import typer
import random
import configparser
from  pathlib import Path

import person
import place
import thing
from helpers import load_csv_file, save_to_abs_path, amount_of_names_callback, get_save_dir
from typing import Optional
from typing_extensions import Annotated

APP_NAME = "NomenCLI"

app = typer.Typer()
app.add_typer(person.app, name="person")
app.add_typer(place.app, name="place")
app.add_typer(thing.app, name="thing")

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

@app.command()
def config(save_directory: Annotated[str, typer.Argument(help="Takes a directory path to configure the save locatoin.")]):
    config_file = Path(typer.get_app_dir(APP_NAME)) / "config.txt"
    config_file.parent.mkdir(exist_ok=True, parents=True)
    
    save_dir_path = Path(save_directory)
    if save_dir_path.is_dir():
        config_file.write_text(save_directory)
        print(f"Save location is now set to \'{save_directory}\'")
    else:
        raise typer.BadParameter("Invalid save_directory path given.")
    
@app.command()
def show_save_location():
    save_directory = get_save_dir()
    print(f"Save location is set to \'{save_directory}\'")

if __name__ == "__main__":
    app()