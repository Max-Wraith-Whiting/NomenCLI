#Typer app for the place sub-command.
import typer

APP_NAME = "NomenCLI"

app = typer.Typer()

@app.command()
def landform(amount_of_names: Annotated[Optional[int], typer.Argument(callback=amount_of_names_callback)] = 10,
          save: Annotated[bool, typer.Option("--save", "-s", help="Save the generated names to the configured save location.")] = False,
          filename: Annotated[str, typer.Option(help="The specified filename if the --save/-s option is chosen.")] = "Names"):
    pass
    

if __name__ == "__main__":
    app()