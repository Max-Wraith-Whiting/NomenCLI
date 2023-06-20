# Typer app for the person sub-command.
import typer
from pathlib import Path
from random import choice
from helpers import load_csv_file
from typing import Optional
from typing_extensions import Annotated


app = typer.Typer()

@app.command()
def stub():
    print("person stub was called!")

@app.command()
def roman(amount_of_names: Annotated[Optional[int], typer.Argument()] = 10,
          save: Annotated[bool, typer.Option("--save", "-s")] = False): 
    if amount_of_names <= 0:
        return
    
    if save:
        print("You be saving this one...")
        
    #Load the csv data.
    data = load_csv_file(Path("Roman"))
    
    praenomen = data["praenomen"]
    nomen = data["nomen"]
    cognomen = data["cognomen"]
    
    full_names = []
    for i in range(amount_of_names):
        name = choice(praenomen) + " " + choice(nomen) + " " + choice(cognomen)
        full_names.append(name)
    
    print(full_names)

if __name__ == "__main__":
    app()