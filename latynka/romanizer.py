import os
import json


class Romanizer:
    def __init__(self, text: str = ""):
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

        for char in self.text:
            if char.lower() in self.concordance:
                if char.islower():
                    self.output += self.concordance[char.lower()].lower()
                else:
                    self.output += self.concordance[char.lower()].upper()
            else:
                self.output += char

        return self.output

    def load_concordance(self) -> None:
        """
        Load letters concordance from json file and set it as Romanizer's concordance
        """

        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        concordance_file_path: str = os.path.join(current_dir, "concordance.json")

        with open(concordance_file_path, "r", encoding="utf-8") as concordance_file:
            self.concordance = json.load(concordance_file)

    def set_text(self, text: str) -> None:
        """
        Given a Ukrainian text string set it as the Romanizer's text

        < text: str
            text to set as Romanizer's text
        """

        self.text = text
