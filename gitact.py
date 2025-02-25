import requests
import sys
from rich import print as rich_print


def gitact(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        events = response.json()
        rich_print(f"[blue]Latest events for {username}[/blue]")
        for event in events:
            event_type = event.get("type")
            event_date = event.get("created_at").split("T")[0]
            match event_type:
                # covering only most common events types
                case "PushEvent":
                    rich_print(
                        f":smiley: Pushed to [bold green]{event['repo']['name']}[/bold green] on {event_date}"
                    )
                case "CreateEvent":
                    rich_print(
                        f":smiley: Created {event['payload']['ref_type']} {event['payload']['ref']} at [bold green]{event['repo']['name']}[/bold green] on {event_date}"
                    )
                case "IssuesEvent":
                    rich_print(
                        f":smiley: Created issue [bold green]{event['payload']['issue']['number']}[/bold green] on {event_date}"
                    )
                case "PullRequestEvent":
                    rich_print(
                        f":smiley: Opened PR [bold green]{event['payload']['pull_request']['number']}[/bold green] on {event_date}"
                    )
                case "WatchEvent":
                    rich_print(
                        f":smiley: Starred [bold green]{event['repo']['name']}[/bold green] on {event_date}"
                    )

    else:
        rich_print(
            f"[red]Failed to fetch data for {username}. Status code:{response.status_code}[/red]"
        )


def main():
    if len(sys.argv) > 1:
        gitact(sys.argv[1])
    else:
        rich_print(
            "[red]Please provide a github username as commandline argument.[/red]"
        )


if __name__ == "__main__":
    main()
