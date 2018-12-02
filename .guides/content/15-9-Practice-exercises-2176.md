---------

1. Write a definition for a class named <span>Circle</span> with attributes <span>center</span> and <span>radius</span>, where <span>center</span> is a Point object and radius is a number.

   Instantiate a Circle object that represents a circle with its center at $(150, 100)$ and radius 75.

   Write a function named `point_in_circle` that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.

   Write a function named `rect_in_circle` that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.

   Write a function named `rect_circle_overlap` that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.

{Try It}(python3 code/classes.py)

Solution: <http://thinkpython2.com/code/Circle.py>.

2. Write a function called `draw_rect` that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.

   Write a function called `draw_circle` that takes a Turtle and a Circle and draws the Circle.

Solution: <http://thinkpython2.com/code/draw.py>.
