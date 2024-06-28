from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hallelujah thank YOU Jesus Christ our Holy Lord GOD Almighty ✝️💖 enter a text to get the response"


@app.get("/{text}")
async def convert(text: str):
    """
    Takes in a Ukrainian text in cyrillic and converts it to latin (romanizes, makes into latynka)

    < text: str
        Ukrainian text in cyrillic
    > str
        Ukrainian text in latin
    """

    # TODO install latynka library and use it here. for now, just title case
    def convert(text: str) -> str:
        return text.title()

    print(text)
    return convert(text)
