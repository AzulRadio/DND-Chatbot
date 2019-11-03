# DND Chatbot

This is a DND game bot under development, contributed by **Kevinskwk** and **AzulRadio**

### Files:
 - `monsterspawn.py`: A d&d monster spawner.
 - `Athena.py`: A telegram bot that helps host DND game (under development)
 - `Monsters.json`: A dictionary of data of different monsters
 - `TOKEN.json`: json file that stores your telegram bot token (you need to **create one yourself!**)

### How to use:
 - Install the libraries required in `requirements.txt`
 - If you want to use python virtual environment. In terminal, get into your virtual environment, and then install the libraries required in `requirements.txt`
     - For example, if you are using pip, do the following:
        ```
        $ python3 -m venv env
        $ source env/bin/activate
        $ pip install -r requirements.txt 
        ```
     - If you are using anaconda, do the following:
        ```
        $ conda create --name env --file requirements.txt 
        ```
     - For more usage of virtual environment, check [this](https://github.com/Kevinskwk/Coding-Note/blob/master/Python/Packages_and_Environments.md)
 - Next, Create a json file, name it `TOKEN.json`. Then put your telegram bot token into it. Remember to put **double quotation marks** around the token!
 - Then, make sure that your computer has sqlite3 installed. To do this, run the following command in the terminal:
    ```
    $ sudo apt-get install sqlite3
    ```
 - After you finish, run `Athena.py`, and your bot is running!

### To do:
 - Add hero-monster calculator (allow DM to input customized names)
 - dead, alive and respawn
 - attack, exempt and AC
 - Make Monster a subclass of creature, which has subclass of Player, Monsters and other subclasses(like NPC)
