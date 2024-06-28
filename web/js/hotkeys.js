/* on Z key press click the #back_link a tag */
document.addEventListener("keydown", (event) => {
  const key_options = ["z", "Z", "я", "Я"];
  if (key_options.includes(event.key)) {
    document.querySelector("#back_link").click();
  }
});
