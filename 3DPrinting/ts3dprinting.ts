// This keeps track of what test case we're currently in so it can be inserted as {case} later on
let count: number = 1;

// These values are stored as strings for testing but should be inputs in the final version
const pr_string_1: string = "300000 200000 300000 500000";
const pr_string_2: string = "300000 200000 500000 300000";
const pr_string_3: string = "300000 500000 300000 200000";

// Values are split and stored in a list
const printer_1: string[] = pr_string_1.split(" ");
const printer_2: string[] = pr_string_2.split(" ");
const printer_3: string[] = pr_string_3.split(" ");

// Convert the list of strings to a list of numbers these values represent the cyan ink in each printer
// Find the printer with the least cyan ink and store that value in cy
let cy: number = Math.min(
  parseInt(printer_1[0]),
  parseInt(printer_2[0]),
  parseInt(printer_3[0])
);

// Same for all other colors (magenta, yellow and black) to complete CMYK
let ma: number = Math.min(
  parseInt(printer_1[1]),
  parseInt(printer_2[1]),
  parseInt(printer_3[1])
);

let ye: number = Math.min(
  parseInt(printer_1[2]),
  parseInt(printer_2[2]),
  parseInt(printer_3[2])
);

let bl: number = Math.min(
  parseInt(printer_1[3]),
  parseInt(printer_2[3]),
  parseInt(printer_3[3])
);

// Put them in an iterable, so they can be added with reduce()
const color_out: number[] = [cy, ma, ye, bl];
const total_ink: number = color_out.reduce((sum, ink) => sum + ink);

// If we have less than 10^6 there is not enough ink
if (total_ink < 1000000) {
  console.log(`Case #${count}: IMPOSSIBLE`);
}

// If we have just enough ink to print
else if (total_ink === 1000000) {
  console.log(`Case #${count}: ${cy} ${ma} ${ye} ${bl}`);
}

// There is more than enough so we need to use less ink
else {
  let dif: number = total_ink - 1000000;

  for (let i: number = 0; i < color_out.length; i++) {
    if (dif >= color_out[i]) {
      dif -= color_out[i];
      color_out[i] = 0;
    } else {
      color_out[i] -= dif;
      break;
    }
  }

  console.log(
    `Case #${count}: ${color_out[0]} ${color_out[1]} ${color_out[2]} ${color_out[3]}`
  );
}
