Python Discord Bot

Discord python bot is a Discord bot programmed in Python using the Discord.py library. The bot supports a variety of commands ranging from admin commands to commands just for fun.
The bot was created to make the server more interactive and attract new users to the server.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
* Google Cloud account

### Installing
1. Create a new VM instance (or use an existing one) running Linux.
2. Install Python (3.5+), Pip and Git
3. Clone the repository and navigate to the directory
```
git clone https://github.com/adamlawson99/DiscordBot.git
cd <Folder Name>
```
4. Create new virtual environement with Pip and activate it
```
python3.8 -m venv my_app_venv
source my_app_venv/bin/activate
```
5. Install all project dependencies
```
pip install -r requirements.txt
```
6. Create a new .env file and add the values for DISCORD_TOKEN, DISCORD_GUILD, PREFIX
```
touch .env
nano .env *(or vim .env if using vim)*
```
7. Install all python modules
```
pip install -e .
```
8. Run the program
```
python Bot/__main__.py
```
## Built With

* [Discord.py](https://github.com/Rapptz/discord.py) - API for Discord
* [Google Cloud](https://cloud.google.com/) - Hosting
* [Python](https://www.python.org/) - Main programming language

## Authors

* **Adam Lawson** - *Lead* - [Portfolio](https://adamlawson.dev/)

## Acknowledgments

* Discord.py library developers
