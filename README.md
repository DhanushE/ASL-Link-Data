## ASL Link Data
> Written in Python Version 3, using requests and beautiful soup.

> Powered by handspeak.com


This is a small python snippet (part of ASL Link Application) that generates a JSON file that contains "words" associated with links. For example the word "box" is associated with [this](https://www.handspeak.com/word/search/index.php?id=2683) link.

If you are only intrested in the final result of this program, examine [this](https://github.com/DhanushE/ASL-Link-Data/blob/main/words_after_program.json) file which contains all of the data on the handspeak website.

## Build Setup

```zsh
# Download the project as a zip attachment
# Open a new terminal at the location that you downloaded

# Install all of the python dependencies on your interpreter
pip3 install -r requirements.txt

# Run the project, and monitor the words.json file
python3 main.py
```
