#!/us/bin/node
const x = process.argv[2];
let y = '';

for (let i = 0; i < x; i++) {
  y += '#';
}
for (let i = 0; i < x; i++) {
  console.log(y);
}
