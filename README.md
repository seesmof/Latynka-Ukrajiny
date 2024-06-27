**Let no unwholesome word come out of your mouth, but if there is any good word for edification according to the need of the moment, say that, so that it will give grace to those who hear.**
~ [Ephesians 4:29](https://www.biblegateway.com/passage/?search=Ephesians+4%3A29&version=NASB,KJV)

**You know this, my beloved brothers and sisters. Now everyone must be quick to hear, slow to speak, and slow to anger;**
~ [James 1:19](https://www.biblegateway.com/passage/?search=James+1%3A19&version=NASB,KJV)

**Your speech must always be with grace, as though seasoned with salt, so that you will know how you should respond to each person.**
~ [Colossians 4:6](https://www.biblegateway.com/passage/?search=Colossians+4%3A6&version=NASB,KJV)

contains a python library that takes in a Ukrainian text in cyrillic alphabet and converts it into latin (romanizes, makes into latynka)

all by the Amazing Grace of Jesus Christ our Holy Lord GOD Almighty for His Glory ✝️💗🙏🏼

### how to use
#### `convert` function
##### in short
just use `convert(your_text)`, this will return your text in latin

##### in detail
the main function of the library is pretty much `convert`. it takes in a Ukrainian text in cyrillic alphabet and converts it into latin (romanizes, makes into latynka)

###### `convert` function
you use the `convert` method by simply passing to it a string, which will be converted into latin and returned back to you ✝️🙏🏼

```python
convert("слава Ісусу Христу Святому БОГУ Всемогутньому навіки вічні, АМІНЬ! привіт їжак п'ять ґудзик гліб хліб")
```
```
slava Isusu Hrystu Svjatomu BOGU Vsemogutn'omu naviky vični, AMIN'! pryvit jižak p'jat' ĝudzyk glib hlib
```

you can also use uppercase letters and even all-caps, i pray and hope it will work alrighty ✝️🙏🏼

```python
convert("СЛАВА НАВІКИ БОГУ СВЯТОМУ ІСУСУ ХРИСТУ НАШОМУ ГОСПОДУ І СПАСИТЕЛЮ, Амінь і АМІНЬ! ЇЖАК та Їжак або їжак")
```
```
SLAVA NAVIKY BOGU SVJATOMU ISUSU HRYSTU NAŠOMU GOSPODU I SPASYTELJU, Amin' i AMIN'! JIŽAK ta Jižak abo jižak
```

###### `Romanizer` class
you can also use the underlying class called `Romanizer` that the `convert` function uses. it contains a method called `romanize` that performs the latynkification process and returns the result back to you ✝️🙏🏼

```python
r = Romanizer("ЄДИНИЙ БОГ ІСУС ХРИСТОС Святий ГОСПОДЬ і Спаситель")
r.romanize()
```
```
JEDYNYJ BOG ISUS HRYSTOS Svjatyj GOSPOD' i Spasytel'
```

the `Romanizer` class's constructor takes in the same Ukrainian cyrillic text string and the `romanize` method converts it into latin

### usage examples
```python
from latynka import convert, Romanizer

text: str = (
    "Слава Ісусу Христу Святому Господу БОГУ Одвічному Всемогутньому Всевишньому навіки Вічні АМІНЬ!"
)
print(convert(text))

text: str = (
    "ґудзик ґанок гліб глобус м'яч п'ять сім'я їхати під'їзд приїхали наїздилися Йошуа Єшуа Мошей Рут Моав Адонай"
)
print(Romanizer(text).romanize())

input_text: str = "СЛАВА НАВІКИ БОГУ ЄДИНОМУ ІСУСУ ХРИСТУ СВЯТОМУ ГОСПОДУ"
converter = Romanizer()
converter.set_text(input_text)
output_text: str = converter.romanize()
print(output_text)
```
```
Slava Isusu Hrystu Svjatomu Gospodu BOGU Odvičnomu Vsemogutn'omu Vsevyšn'omu naviky Vični AMIN'!

ĝudzyk ĝanok glib globus m'jač p'jat' sim'ja jihaty pid'jizd pryjihaly najizdylysja Jošua Ješua Mošej Rut Moav Adonaj

SLAVA NAVIKY BOGU JEDYNOMU ISUSU HRYSTU SVJATOMU GOSPODU
```