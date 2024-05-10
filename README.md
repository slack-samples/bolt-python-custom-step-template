# Bolt for Python Custom Function Template

This is a Bolt for Python template app used to build custom functions in [Workflow Builder](https://api.slack.com/start#workflow-builder).

## Setup

Before getting started, first make sure you have a development workspace where
you have permission to install apps. **Please note that the features in this
project require that the workspace be part of
[a Slack paid plan](https://slack.com/pricing).**

### Install the Slack CLI

To use this template, you need to install and configure the Slack CLI.
Step-by-step instructions can be found in our
[Quickstart Guide](https://api.slack.com/automation/quickstart).

### Clone the Template

Start by cloning this repository:

```zsh
# Clone this project onto your machine
$ slack create my-app -t slack-samples/bolt-python-custom-function-template

# Change into the project directory
$ cd my-app

# Install dependencies
$ pip install -r requirements.txt
```

## Running Your Project Locally

While building your app, you can see your changes appear in your workspace in
real-time with `slack run`. You'll know an app is the development version if the
name has the string `(local)` appended.

```zsh
# Run app locally
$ slack run

⚡️ Bolt app is running! ⚡️
```

To stop running locally, press `<CTRL> + C` to end the process.

### Linting
Run flake8 and black for linting and code formatting:

```zsh
# Run flake8 from root directory (linting)
$ flake8 *.py

# Run black from root directory (code formatting)
$ black .
```

## Using Functions in Workflow Builder
With your server running, your function is now ready for use in [Workflow Builder](https://api.slack.com/start#workflow-builder)! Add it as a custom step in a new or existing workflow, then run the workflow while your app is running.

For more information on creating workflows and adding custom steps, read more [here](https://slack.com/help/articles/17542172840595-Create-a-new-workflow-in-Slack).

## Project Structure

### `.slack/`

Contains `apps.dev.json` and `config.json`, which include installation details for your project.

### `app.py`

`app.py` is the entry point for the application and is the file you'll run to start the server. This project aims to keep this file as thin as possible, primarily using it as a way to route inbound requests.

### `manifest.json`

`manifest.json` is a configuration for Slack apps. With a manifest, you can create an app with a pre-defined configuration, or adjust the configuration of an existing app.

### `slack.json`

Used by the Slack CLI to interact with the project's SDK dependencies. It contains
script hooks that are executed by the CLI and implemented by `slack_cli_hooks`.
