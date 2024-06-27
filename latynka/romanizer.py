import os
import json


class Romanizer:
    def __init__(self, text: str = ""):
        """
        < text: str
            Ukrainian text in cyrillic

        > text: str
            internal text, set to text parameter
        > output: str
            output text, stores converted text
        > concordance: dict
            loaded letters concordance
        """

        self.text: str = text
        self.output: str = ""
        self.concordance: dict = {}

        self.load_concordance()

    def romanize(self) -> str:
        """
        Takes in a Ukrainian text in cyrillic and converts it to latin (romanizes, makes into latynka)

        < text: str
            Ukrainian text in cyrillic

        > str
            Ukrainian text in latin
        """

        for index, char in enumerate(self.text):
            if char.lower() in self.concordance:
                converted_letter: str = self.concordance[char.lower()]
                if char.islower():
                    self.output += converted_letter.lower()
                else:
                    # if it is NOT the last letter
                    if index < len(self.text) - 1:
                        # look at the next letter
                        next_letter: str = self.text[index + 1]
                        # if the letter is lowercase, then capitalize only the first letter of our converted_letter; otherwise capitalize the whole converted_letter
                        self.output += (
                            converted_letter.title()
                            if next_letter.islower()
                            else converted_letter.upper()
                        )
                    # if it is the last letter
                    else:
                        # same as above
                        previous_letter: str = self.text[index - 1]
                        # only now we're looking at the last letter, since there are no next letters
                        self.output += (
                            converted_letter.title()
                            if previous_letter.islower()
                            else converted_letter.upper()
                        )
            else:
                self.output += char

        return self.output

    def load_concordance(self) -> None:
        """
        Load letters concordance from json file and set it as Romanizer's concordance
        """

        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        concordance_file_path: str = os.path.join(
            current_dir, "data", "concordance.json"
        )

        with open(concordance_file_path, "r", encoding="utf-8") as concordance_file:
            self.concordance = json.load(concordance_file)

    def set_text(self, text: str) -> None:
        """
        Set internal text given the input text

        < text: str
            Ukrainian text in cyrillic
        """

        self.text = text
