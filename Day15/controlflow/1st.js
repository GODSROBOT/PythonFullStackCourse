// even odd numbers

let numbers = [2,1,4,3];

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    console.log(numbers[i] + " is Even");
  } else {
    console.log(numbers[i] + " is Odd");
  }
}

