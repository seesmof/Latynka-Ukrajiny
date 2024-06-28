const concordance = {
  а: "a",
  б: "b",
  в: "v",
  г: "g",
  ґ: "ĝ",
  д: "d",
  е: "e",
  є: "je",
  ж: "ž",
  з: "z",
  и: "y",
  і: "i",
  ї: "ji",
  й: "j",
  к: "k",
  л: "l",
  м: "m",
  н: "n",
  о: "o",
  п: "p",
  р: "r",
  с: "s",
  т: "t",
  у: "u",
  ф: "f",
  х: "h",
  ц: "c",
  ч: "č",
  ш: "š",
  щ: "šč",
  ь: "'",
  ю: "ju",
  я: "ja",
  "'": "'",
};

const convert = (text) => {
  let output = "";
  for (let index = 0; index < text.length; index++) {
    const char = text.charAt(index);
    if (char.toLowerCase() in concordance) {
      let convertedLetter = concordance[char.toLowerCase()];
      if (char === char.toLowerCase()) {
        output += convertedLetter.toLowerCase();
      } else {
        if (index < text.length - 1) {
          const nextLetter = text.charAt(index + 1);
          output +=
            nextLetter === nextLetter.toLowerCase()
              ? `${convertedLetter
                  .charAt(0)
                  .toUpperCase()}${convertedLetter.slice(1)}`
              : convertedLetter.toUpperCase();
        } else {
          const previousLetter = text.charAt(index - 1);
          output +=
            previousLetter === previousLetter.toLowerCase()
              ? `${convertedLetter
                  .charAt(0)
                  .toUpperCase()}${convertedLetter.slice(1)}`
              : convertedLetter.toUpperCase();
        }
      }
    } else {
      output += char;
    }
  }
  return output;
};

const copyOutputText = () => {
  document.querySelector("#output").select();
  document.execCommand("copy");
};

document.querySelector("#input").addEventListener("input", () => {
  let input = document.querySelector("#input").value;
  let output = document.querySelector("#output");
  output.value = convert(input);
});

document
  .querySelector("#copy_button")
  .addEventListener("click", () => copyOutputText());
document
  .querySelector("#output")
  .addEventListener("focus", () => copyOutputText());
