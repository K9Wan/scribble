let arr = [333, 332, 323, 233, 322, 232, 223, 321, 132, 213, 123, 231, 312];
let testcases = arr.map(nums => Array.from(String(nums)).map(Number));
for(let tc of testcases){
    console.log(tc);
}

results = Array.from('3333222222222').map(Number);
