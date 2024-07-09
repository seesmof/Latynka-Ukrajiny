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
const input = document.querySelector("#input");
const output = document.querySelector("#output");

const title = (text) => `${text.charAt(0).toUpperCase()}${text.slice(1)}`;

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
              ? title(convertedLetter)
              : convertedLetter.toUpperCase();
        } else {
          const previousLetter = text.charAt(index - 1);
          output +=
            previousLetter === previousLetter.toLowerCase()
              ? title(convertedLetter)
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
  output.select();
  document.execCommand("copy");
};

input.addEventListener("input", () => (output.value = convert(input.value)));

/* on Space key press focus the #input textarea */
document.addEventListener("keydown", (event) => {
  if (event.key === " " && document.activeElement.id !== "input") {
    input.focus();
    event.preventDefault();
  }
});

/* on Escape key press unfocus the #input textarea */
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    input.blur();
  }
});

/* on C key press copy the #output text */
document.addEventListener("keydown", (event) => {
  const key_options = ["c", "C", "с", "С"];
  if (
    key_options.includes(event.key) &&
    document.activeElement.id !== "input"
  ) {
    copyOutputText();
  }
});

/* on X key press clear the #input textarea from text */
document.addEventListener("keydown", (event) => {
  const key_options = ["x", "X", "ч", "Ч"];
  if (
    key_options.includes(event.key) &&
    document.activeElement.id !== "input"
  ) {
    input.value = "";
    output.value = "";
  }
});

/* on Z key press click the #hotkeys_link a tag */
document.addEventListener("keydown", (event) => {
  const key_options = ["z", "Z", "я", "Я"];
  if (
    key_options.includes(event.key) &&
    document.activeElement.id !== "input"
  ) {
    document.querySelector("#hotkeys_link").click();
  }
});

document
  .querySelector("#copy_button")
  .addEventListener("click", () => copyOutputText());
document
  .querySelector("#output")
  .addEventListener("focus", () => copyOutputText());
