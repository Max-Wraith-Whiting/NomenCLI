# Typer app for the thing sub-command.
import typer

app = typer.Typer()

@app.command()
def stub():
    print("thing stub was called!")

if __name__ == "__main__":
    app()