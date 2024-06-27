from latynka import convert, Romanizer


def run_tests() -> None:
    tests_data: list[tuple[str, str]] = [
        (
            "хліб, гліб, ґанок, під'їзд, в'юнки, п'ять, Слава Ісусу Христу Святому Господу БОГУ Всемогутньому Всевишньому навіки Вічні АМІНЬ",
            "hlib, glib, ĝanok, pid'jizd, v'junky, p'jat', Slava Isusu Hrystu Svjatomu Gospodu BOGU Vsemogutn'omu Vsevyšn'omu naviky Vični AMIN'",
        ),
        (
            "Ще до існування світу було Слово, і Слово було з Богом, і Слово було Бог. Той, Хто був Словом, був з Богом споконвіку. Все було створене через Нього, і ніщо не було створене без Нього. В Ньому було життя, і воно було Світлом для людей. (Йоан 1:1-4)",
            "Šče do isnuvannja svitu bulo Slovo, i Slovo bulo z Bogom, i Slovo bulo Bog. Toj, Hto buv Slovom, buv z Bogom spokonviku. Vse bulo stvorene čerez N'ogo, i niščo ne bulo stvorene bez N'ogo. V N'omu bulo žyttja, i vono bulo Svitlom dlja ljudej. (Joan 1:1-4)",
        ),
        ("ЄДИНИЙ", "JEDYNYJ"),
        ("ЄДИНИЇ", "JEDYNYJI"),
    ]

    for test_input, test_check in tests_data:
        assert (
            convert(test_input) == test_check == Romanizer(test_input).romanize()
        ), f"{test_input=}\n{convert(test_input)=}\n{test_check=}"

    print(
        "All tests passed! Hallelujah thank YOU Jesus Christ our Holy Lord GOD Almighty"
    )


if __name__ == "__main__":
    run_tests()
