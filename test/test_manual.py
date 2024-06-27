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
