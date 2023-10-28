from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Input, Label, Pretty, OptionList

from hw6 import generate_language_model

import json
import requests
import os
import sys


IMAGE = '''
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⠟⠛⠉⠉⠉⠉⠛⠻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣤⣤⣄⠀⠀⣠⣤⣤⣿⣿⣿⣷⡀⠀⠀⠀
⠀⢀⣼⣿⣿⣿⠋⢠⣤⠙⠁⠈⠋⣤⡄⠙⣿⣿⣿⣿⣄⠀⠀
⢠⣿⣿⣿⣿⡿⠀⠈⠉⠀⠀⠀⠀⠉⠁⠀⢿⣿⣿⣿⣿⣷⠀
⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡆
⠹⣿⣿⣿⣿⣿⠀⠀⠴⠞⠁⠈⠳⠦⠀⠀⣿⣿⣿⣿⣿⡿⠁
⠀⠉⢻⡿⢿⣿⣧⠀⠀⠀⢶⡶⠀⠀⠀⣼⣿⣿⣿⡟⠋⠁⠀
⠀⠀⣼⡇⠀⠀⠙⣷⣄⠀⠈⠁⠀⣠⣾⠋⠀⠀⢸⣧⠀⠀⠀
⠀⠀⣿⡇⠀⠀⠀⠈⠛⠷⣶⣶⠾⠛⠁⠀⠀⠀⢸⣿⠀⠀⠀
⠀⠀⢻⡇⠀⠀⠀⣀⣀⣤⣤⣤⣤⣀⣀⠀⠀⠀⢸⡟⠀⠀⠀
⠀⠀⠘⣿⣴⠾⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠷⣦⣿⠃⠀⠀⠀
⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀
'''


class InputApp(App):
    
    CSS = """
    Input.-valid {
        border: tall $success 60%;
    }
    Input.-valid:focus {
        border: tall $success;
    }
    Input {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    Pretty {
        margin: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label(IMAGE)
        yield Label("Enter thy phrase (Presseth' Ctlr/Cmd+C to quit):)")
        yield Input(
            placeholder="Thy phrase goeth h're",
        )
        yield OptionList('')

    @on(Input.Changed)
    def text_changed(self, event: Input.Changed) -> None:
        global language_model

        #Debug Print
        #self.query_one(Pretty).update(f"You wrote: {event.value}")

        # Get the value of the input
        text = event.value

        # Check if alteast 2 words are entered
        if len(text.split())>=1:
            # Get the autocomplete
            autocomplete_options = autocomplete(text, language_model)
            if autocomplete_options is None:
                return "No Suggestions"
            # Create a string with each autocomplete response on a new line
            suggestions = [word for word, _ in autocomplete_options]

            options = self.query_one(OptionList)

            # Remove any existing options
            options.clear_options()

            # Update the Pretty widget with the autocomplete options
            for suggestion in suggestions:
                options.add_option(suggestion)


def autocomplete(phrase, language_model):
    """
    Given a phrase and a language model, return the most likely next word
    in the phrase.

    Inputs:
        phrase (str): A phrase containing atleast 1 word and upto 5 words
        language_model (Dict[str, List(Tuple(str, float))]): A dictionary 
            mapping each n-gram string to a list of tuples, 
            each tuple containing the next word and it's probability

    Returns (List[Tuple(str,float)]): The most probable list of words and their
    probabilities, sorted by probability, descending.
    """

    # DO NOT MODIFY THIS FUNCTION

    split_phrase = tuple(phrase.split())
    num_words = len(split_phrase)

    if not (1 <= num_words < 5):
        return None

    else:        
        if split_phrase not in language_model.keys():
            return None
        
        next_word_probs = language_model[split_phrase]
        next_word_probs.sort(key=lambda x: x[1], reverse=True)
        return next_word_probs[:5]


def download_shakespeare_lines():
    """
    Downloads all of shakespeare's lines from the internet and saves them to
    shakespeare_lines.json
    """

    # Get all of shakespeare's lines
    r = requests.get("https://people.cs.uchicago.edu/~suhail/cs141/shakespeare_lines.json")

    # Save them to a file
    with open("shakespeare_lines.json", "w") as f:
        f.write(r.text)

sys.path.insert(0, os.getcwd())

if not os.path.exists("shakespeare_lines.json"):
    print("Downloading Shakespeare's lines (Will take a few seconds)...")
    # Download all shakespeare lines
    download_shakespeare_lines()


# Load all shakespeare lines
with open("shakespeare_lines.json") as f:
    lines = json.load(f)

print("Loading Language Model (Will take a few seconds)...")
# Generate Language Model
language_model = generate_language_model(lines)

print("Done!")

# Display the GUI
app = InputApp()
app.run()
