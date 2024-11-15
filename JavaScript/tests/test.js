let integer = parseInt(prompt("Enter a number: "));

while (integer !== 1) {
  if (integer % 2 === 0) {
    integer /= 2;
    console.log(Math.floor(integer));
  } else if (integer % 2 !== 0) {
    integer = 3 * integer + 1;
    console.log(Math.floor(integer));
  } else {
    console.log("Unknown Number");
  }
}