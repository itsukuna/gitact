# Gitact

Gitact is a CLI tool to fetch and display the latest GitHub events for a user. It leverages the GitHub API to retrieve various types of user activities, such as commits, comments, and repository creations.

It is inspired by **[GitHub user activity](https://roadmap.sh/projects/github-user-activity)** project on **[Roadmap.sh](https://roadmap.sh/)**.

## Prerequisites

- Python 3.10+
- [pipx](https://pypa.github.io/pipx/)

## Installation

Gitact is best installed using `pipx`, which ensures it runs in an isolated environment:

```sh
pipx install git+https://github.com/itsukuna/gitact.git
```

If you don't have `pipx` installed, you can install it first:

```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

## Usage

To fetch and display the latest GitHub events for a user, run the following command:

```sh
gitact <username>
```

Replace `<username>` with the GitHub username you want to fetch events for.

## Example

```sh
gitact itsukuna
```

## Uninstallation

To remove Gitact, use:

```sh
pipx uninstall gitact
```

## License

This project is licensed under the MIT License.
