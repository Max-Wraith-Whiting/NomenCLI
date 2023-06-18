# Typer app for the person sub-command.
import typer

app = typer.Typer()

@app.command()
def stub():
    print("person stub was called!")

if __name__ == "__main__":
    app()