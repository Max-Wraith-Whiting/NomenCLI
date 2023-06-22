# Typer app for the person sub-command.
import typer
from pathlib import Path
from random import choice
from helpers import load_csv_file, amount_of_names_callback
from typing import Optional
from typing_extensions import Annotated


app = typer.Typer()

@app.command()
def stub():
    print("person stub was called!")
    
@app.command()
def biblical(amount_of_names: Annotated[Optional[int], typer.Argument(callback=amount_of_names_callback)] = 10,
          save: Annotated[bool, typer.Option("--save", "-s")] = False):
    
    biblical_names = load_csv_file(Path("Biblical"))["biblical"]
    
    full_names = []
    for i in range(amount_of_names):
        name = choice(biblical_names)
        print(name)
        full_names.append(name)
        
    if save:
        print("Saved this...")
        
@app.command()
def dwarf(amount_of_names: Annotated[Optional[int], typer.Argument(callback=amount_of_names_callback)] = 10,
          sex: Annotated[bool, typer.Option("--male/--female", "-m/-f", help="Exclusively generate names of a certain sex.")] = None,
          save: Annotated[bool, typer.Option("--save", "-s", help="Save the generated names to the configured save location.")] = False):
    
    data = load_csv_file(Path("Dwarf"))
    
    syllable_1, syllable_2, title_1, title_2 = data["syllable_1"], data["syllable_2"], data["title_1"], data["title_2"]
    
    if type(sex) is None:
        suffix = data["suffix_male"] + data["suffix_female"]
    elif sex:
        suffix = data["suffix_male"]
    else:
        suffix = data["suffix_female"]
    
    full_names = []
    for i in range(amount_of_names):
            name = choice(syllable_1) + choice(syllable_2) + choice(suffix) + " " + choice(title_1) + choice(title_2)
            print(name)
            full_names.append(name)
            
    if save:
        print("Saved...")

@app.command()
def roman(amount_of_names: Annotated[Optional[int], typer.Argument(callback=amount_of_names_callback)] = 10,
          save: Annotated[bool, typer.Option("--save", "-s")] = False):
    
    #Load the csv data.
    data = load_csv_file(Path("Roman"))
    
    praenomen, nomen, cognomen = data["praenomen"], data["nomen"], data["cognomen"]
    
    full_names = []
    for i in range(amount_of_names):
        name = choice(praenomen) + " " + choice(nomen) + " " + choice(cognomen)
        print(name)
        full_names.append(name)
        
    if save:
        print("You be saving this one...")

if __name__ == "__main__":
    app()