#Typer app for the place sub-command.
import typer

APP_NAME = "NomenCLI"

app = typer.Typer()

@app.command()
def stub():
    print("place stub was called!")

if __name__ == "__main__":
    app()