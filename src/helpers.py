"""This file holds utility and helper functions used across many modules."""

from pathlib import Path
import csv
import typer

APP_NAME = "NomenCLI"

def load_csv_file(relative_file_path:Path):   
    data_dir = Path.cwd().parent / "data" / relative_file_path
    data = {}
    for data_file in data_dir.iterdir():
        with data_file.open(mode='r', encoding="utf-8") as file:
            reader = csv.reader(file)
            file_data = next(reader)
                
        data[f"{data_file.name}"[:-4]] = file_data
    
    return data

def save_to_path(data: list, file_name: str):
    save_dir_path = get_save_dir()
    if save_dir_path.is_dir():
        with open(save_dir_path / f"{file_name}.txt", "a") as file:
            for name in data:
                file.write(f"{name}\n")
    else:
        print("The given path is not to a directory!")
        
def amount_of_names_callback(amount_of_names: int):
    if amount_of_names <= 0:
        raise typer.BadParameter("You cannot have 0 or less names.")
    else:
        return amount_of_names
    
def get_save_dir():
    config_file = Path(typer.get_app_dir(APP_NAME)) / "config.txt"
    return Path(config_file.read_text())