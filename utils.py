from rich.console import Console

console = Console()

def print_anime_list(anime_list):
    for anime in anime_list:
        title = anime.get("title")
        synopsis = anime.get("synopsis", "No description")
        url = anime.get("url")
        console.print(f"[bold cyan]{title}[/]")
        console.print(f"{synopsis}")
        console.print(f"[green]{url}[/]\n")
