var canvas;
var slider;
let toggleButton;
var xmas_mode = false;

class KochLine {
    constructor(start, end) {
        this.start = start.copy();
        this.end = end.copy();
    }
    
    show() {
        line(this.start.x, this.start.y, this.end.x, this.end.y);
    }
}

class Koch {
  constructor(start, end) {
    this.start = start.copy();
    this.end = end.copy();
    this.lines = [];
  }

  generate(amount) {
    this.lines = [];
    this._koch(this.start, this.end, amount);
  }

    _koch(start, end, n) {

        if (n === 0) {
            this.lines.push(new KochLine(start, end));
        } else {

            let v = p5.Vector.sub(end, start);
            v.div(3);

            let a = 0;
            let b = 0;
            let c = 0;
            let d = 0;

            if (!xmas_mode) {

                a = p5.Vector.add(start, v);
                        
                v.rotate(-radians(60));
                b = p5.Vector.add(a, v);
                    
                v.rotate(radians(120));
                c = p5.Vector.add(b, v);

                v.rotate(-radians(60));
                d = p5.Vector.add(c, v);

            } else {

                a = p5.Vector.add(start, v);
                b = p5.Vector.sub(end, v);

                v.rotate(-radians(45));
                c = p5.Vector.add(a, v);

                v = p5.Vector.sub(b, a);
                v.div(3);

                d = p5.Vector.add(a, v);

            }
    
            // Recursively apply the algorithm to the four segments
            this._koch(start, a, n - 1);
            this._koch(a, b, n - 1);
            this._koch(b, c, n - 1);
            this._koch(c, d, n - 1);
            this._koch(d, end, n - 1);
        }
    }

    show() {
        for (let l of this.lines) {
            l.show();
        }
    }
}

function setup() {

  createCanvas(600, 600);
  background(0);
  slider = createSlider(1, 10, 0, 1);
  slider.position((width/4 - slider.width) / 2, 10);
  toggleButton = createButton('XMAS MODE');
  toggleButton.position(slider.x + slider.width + 10, 10);
  toggleButton.mousePressed(toggle);

}

function toggle() {
    xmas_mode = !xmas_mode;
}

function draw() {
    stroke(255);
    if (!xmas_mode) {
        // Default mode
        background(0);
        
    } else {
        // XMAS mode
        background(50, 55, 165);
    }

    translate(0, height / 2);

    let koch = new Koch(createVector(0, 0), createVector(width, 0));
    koch.generate(slider.value());

    koch.show();

    if (xmas_mode) {

        push();
        fill(90, 215, 65);
        beginShape();
        if (slider.value() > 0) {
            for (let l of koch.lines) {
                vertex(l.start.x, l.start.y);
            }
        } 
        endShape(CLOSE);

        fill(255);
        beginShape();
        vertex(0, 0);
        vertex(width, 0);
        vertex(width, height);
        vertex(0, height);
        endShape(CLOSE);
        pop();

    }
}