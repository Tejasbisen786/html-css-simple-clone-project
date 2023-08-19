const inputTxt = document.getElementById("Text");
const wordOutput = document.getElementById("countArea");
const btn = document.getElementById("btn");

function extractText() {
  var len = inputTxt.value;
  var fVal = len.trim().length;
  if (fVal > 10) {
    wordOutput.style.color = "red";
    wordOutput.textContent = ` Sorry!! Word Limit Reached`;
} else {
      wordOutput.textContent = ` Word Count is : ${fVal}`;
  }
}
inputTxt.addEventListener("input", extractText);
