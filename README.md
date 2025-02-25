# Gitact

Gitact is a CLI tool to fetch and display the latest GitHub envets for a user. It leverages the GitHub API to retrieve various types of user activities, such as commits, comments, and repository creations.

It is inspired from **[GitHub user activity](https://roadmap.sh/projects/github-user-activity)** project on **[Roadmap.sh](https://roadmap.sh/)**

## Prerequisites

- Python 3.10

## Installation

```sh
pip install git+https://github.com/itsukuna/gitact.git
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

## License

This project is licensed under the MIT License.
