# Bolt for Python Custom Step Template

This is a Bolt for Python template app used to build custom steps for use in
[Workflow Builder](https://api.slack.com/start#workflow-builder).

## Setup

Before getting started, first make sure you have a development workspace where
you have permission to install apps. **Please note that the features in this
project require that the workspace be part of
[a Slack paid plan](https://slack.com/pricing).**

### Developer Program

Join the [Slack Developer Program](https://api.slack.com/developer-program) for
exclusive access to sandbox environments for building and testing your apps,
tooling, and resources created to help developers build and grow.

## Installation

### Create a Slack App

1. Open [https://api.slack.com/apps/new](https://api.slack.com/apps/new) and
   choose "From an app manifest"
2. Choose the workspace you want to install the application to
3. Copy the contents of [manifest.json](./manifest.json) into the text box that
   says `*Paste your manifest code here*` (within the JSON tab) and click _Next_
4. Review the configuration and click _Create_
5. Click _Install_ button and _Allow_ on the screen that follows. You'll then be
   redirected to the App Settings dashboard.

### Environment Variables

Before you can run the app, you'll need to store some environment variables.

1. Open your apps setting page from this list, click **OAuth & Permissions** in
   the left hand menu, then copy the Bot User OAuth Token. You will store this
   in your environment as `SLACK_BOT_TOKEN`.
2. Click **Basic Information** from the left hand menu and follow the steps in
   the App-Level Tokens section to create an app-level token with the
   `connections:write` scope. Copy this token. You will store this in your
   environment as `SLACK_APP_TOKEN`.

```zsh
# Replace with your app token and bot token
export SLACK_BOT_TOKEN=<your-bot-token>
export SLACK_APP_TOKEN=<your-app-token>
```

### Local Project

```zsh
# Clone this project onto your machine
git clone https://github.com/slack-samples/bolt-python-custom-step-template.git

# Change into this project directory
cd bolt-python-custom-step-template

# Setup your python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip3 install -r requirements.txt

# Start your local server
python3 app.py
```

### Linting

Run flake8 and black for linting and code formatting:

```zsh
# Run ruff from root directory for linting
ruff check

# Run ruff from root directory for code formatting
ruff format
ruff check --fix
```

## Using Steps in Workflow Builder

With your server running, the `Sample step` is now ready for use in
[Workflow Builder](https://api.slack.com/start#workflow-builder)! Add it as a
custom step in a new or existing workflow, then run the workflow while your app
is running.

For more information on creating workflows and adding custom steps, read more
[here](https://slack.com/help/articles/17542172840595-Create-a-new-workflow-in-Slack).

## Project Structure

### `app.py`

`app.py` is the entry point for the application and is the file you'll run to
start the server. This project aims to keep this file as thin as possible,
primarily using it as a way to route inbound requests.

### `manifest.json`

`manifest.json` is a configuration for Slack apps. With a manifest, you can
create an app with a pre-defined configuration, or adjust the configuration of
an existing app.

### `/listeners`

Every incoming request is routed to a "listener". Inside this directory, we
group each listener based on the Slack Platform feature used, so
`/listeners/actions.py` handles incoming
[Actions](https://api.slack.com/reference/interaction-payloads/block-actions)
requests, `/listeners/functions.py` handles
[Custom Steps](https://api.slack.com/automation/functions/custom-bolt) and so
on.
