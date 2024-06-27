from latynka.romanizer import Romanizer


def convert(text: str) -> str:
    """
    Takes in a Ukrainian text in cyrillic and converts it to latin (romanizes, makes into latynka)

    < text: str
        Ukrainian text in cyrillic

    > str
        Ukrainian text in latin
    """

    return Romanizer(text).romanize()
