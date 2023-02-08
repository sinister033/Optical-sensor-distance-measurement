int i=0;
float fac, dist;
void setup() {
  size(600, 600); 
  dist = 7.65; // 2*Pi*r of the mousewheel 
  // may differ for different mouses 
  fac = dist/24;
}

void draw() {
  background(204);
  fill(0);
  textSize(120);
  textAlign(CENTER);
  text(i*fac*-1, width/2, height/2);
  interaction();
}

void keyPressed() {
  if (key==' ')i=0;
}

void mouseWheel(MouseEvent event) {
  float e = event.getCount();
  if (e>0)i++;
  if (e<0)i--;
  if (e==0)print("stop");
}

void interaction(){
    textSize(20);
  text("Press  space key to callibrate...",width/2,height-20);
}
