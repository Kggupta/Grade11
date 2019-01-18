#Make up your own questions on topics not covered in the above questions.

import turtle

color = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(200):
   turtle.pencolor(color[x % 3])
   turtle.width(x / 90 + 2)
   turtle.forward(x)
   turtle.left(25)
