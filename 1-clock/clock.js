let radius = 200;
let n = 3;

let v1;
let v2;
let unit;

let currsec;
let currmin;
let currhour;

let sec;
let min;
let hou;

function setup() {
  
  createCanvas(800, 600);
  v1 = createVector(0, 0);
  v2 = createVector(0, 0);
  currsec = second();
  currmin = minute();
  currhour = hour();

}

function draw() {

  background(200);
  translate(width / 2, height / 2);

  unit = millis(); 
  let s = currsec + unit / 1000;
  let m = currmin + s/60;
  let h = currhour + m/60;

  console.log(nf(floor(h), 2) + ":" + nf(floor(m), 2) + ":" + nf(floor(s), 2));
  
  maps = map(s, 0, 60, 0, TWO_PI);
  mapm = map(m, 0, 60, 0, TWO_PI);
  maph = map(h, 0, 12, 0, TWO_PI);
  
  circle(0, 0, 500);

  // minute lines
  for (let i = 0; i < 60; i++) {
    let angle = map(i, 0, 60, 0, TWO_PI);
    let x = (radius * 1.2) * cos(angle);
    let y = (radius * 1.2) * sin(angle);
    let x2 = ((radius * 1.2) - 5) * cos(angle);
    let y2 = ((radius * 1.2) - 5) * sin(angle);
    stroke(0);
    line(x, y, x2, y2);
  }

  // hour lines
  for (let i = 0; i < 12; i++) {
    let angle = map(i, 0, 12, 0, TWO_PI);
    let x = (radius * 1.2) * cos(angle);
    let y = (radius * 1.2) * sin(angle);
    let x2 = ((radius * 1.2) - 10) * cos(angle);
    let y2 = ((radius * 1.2) - 10) * sin(angle);
    stroke(0);
    line(x, y, x2, y2);
  }
  
  // hours
  push();
  rotate(maph - PI / 2);
  line(v2.x, v2.y, 150, 0);
  pop();

  // min
  push();
  rotate(mapm - PI / 2);
  line(v2.x, v2.y, 200, 0);
  pop();

  // sec
  push();
  rotate(maps - PI / 2);
  stroke(255, 0, 0);
  line(v2.x, v2.y, 200, 0);
  pop();

}