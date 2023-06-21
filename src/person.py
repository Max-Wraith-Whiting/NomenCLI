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