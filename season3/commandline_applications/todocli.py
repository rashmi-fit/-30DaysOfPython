import typer
from rich.console import Console
from rich.table import Table


console = Console()

app = typer.Typer()

@app.command(short_help = 'add an item')
def add(task:str,category:str):
      typer.echo(f"adding {task},{category}")
      show()

@app.command()
def delete(task:str,category:str):
      typer.echo(f"deleting {task},{category}")
      show()

@app.command()
def update(position:int, task:str = None,category:str = None):
      typer.echo(f"updating {task},{category}")
      show()

@app.command()
def complete(position: int):
      typer.echo(f"complete {position}")
      show()
      
@app.command()
def show():
      tasks = [("Todo1", "Study"), ("Todo2", "Sports")]
      console.print("[bold magenta]Todos[/bold magenta]!", "")

      for idx, task in enumerate(tasks, start = 1):
            c = get_category_color(task[1])
            is_done_str = "tick" if True ==2 else "cross"
            table.add_row(str(idx),task[0], f'[{c}]{task[1]}[/{c}]', is_done_str)
      console.print(table)

if __name__ == "__main__" :
      app()
