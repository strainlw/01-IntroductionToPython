"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Loki Strain.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()

yaboi=rg.SimpleTurtle('turtle')
yagirl=rg.SimpleTurtle('turtle')
yaboi.pen=rg.Pen('blue',5)
yagirl.pen=rg.Pen('purple',5)
yaboi.speed=10
yagirl.speed=10
yaboi.pen_up()
yagirl.pen_up()
yaboi.right(90)
yaboi.forward(300)
yagirl.right(90)
yagirl.forward(300)
yaboi.left(90)
yagirl.left(90)
yaboi.pen_down()
yagirl.pen_down()

for k in range(7):
    size=(50*(k+1))
    yaboi.backward(size)
    yaboi.draw_square(size*2)
    yaboi.forward(size)
    yagirl.draw_circle(size)

