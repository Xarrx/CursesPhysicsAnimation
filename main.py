import curses
import time
from physics_object import PhysicsObject as po

import os
rows, columns = os.popen('stty size', 'r').read().split()

structure = [
  (0, 0, 'L'), (0, 60, 'R'),
  (60, 0, 'l'), (60, 60, 'r')
]

def init_colors():
  # init color pairs
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
  curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN)
  curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLUE)
  curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

def main(stdscr):
  # Clear screen
  stdscr.clear()
  
  # create a pad
  pad = curses.newpad(100,100)

  # fill the pad with numbers
  for y in range(0,99):
    for x in range(0,99):
      pad.addch(y, x, ord('a') + (x*x+y*y) % 26)

  pad.refresh( 0,0, 5,5, 20,75)
  #stdscr.refresh()
  pad.getkey()

def window_example(stdscr):
  # clear screen
  stdscr.clear()

  # init color pairs
  init_colors()
  
  # create a window
  begin_x = 20
  begin_y = 7
  height = 5
  width = 40
  win = curses.newwin(height, width, begin_y, begin_x)
  win.addstr(0, 0, "Dummy Window", curses.color_pair(1))
  win.refresh()
  
  # set the time to wait in seconds
  t = 0.05

  for i in range(1, 30, 2):
    # draw colors
    draw_square(stdscr, 2,i, 2, 1)
    time.sleep(t)
    draw_square(stdscr, 6,i, 2, 2)
    time.sleep(t)
    draw_square(stdscr, 10,i, 2, 3)
    time.sleep(t)
    draw_square(stdscr, 14,i, 2, 4)
    time.sleep(t)
    draw_square(stdscr, 18,i, 2, 5)
    time.sleep(t)
    draw_square(stdscr, 22,i, 2, 6)

  # wait for a keypress before exiting
  win.getkey()


def draw_square(stdscr, x, y, width, color):
  """Draw a square at location y,x with side width of width and height of 
  width/2.

  Actual width of the created window needs to be width/2+1 to prevent the 
  cursor from leaving the window and causing an error.
  
  Runs in O(n) time."""

  # create the height variable
  height = int((width))

  # create the window
  square = curses.newwin(height+1, width, y, x)

  # create the string which will fill the window
  fill = ""
  for i in range(0, width*height):
    fill += "`"

  # draw the square and refresh
  square.addstr(0, 0, fill, curses.color_pair(color))
  square.refresh()

def game_loop(stdscr):
  curses.curs_set(False)
  dt = 0.001;color = 0;color2 = 1; color3 = 2; color4= 3; dt_mult = 1; square_size = 1
  area_width = 80; area_height = 25;
  colors = range(1,6)
  init_colors()
  win = curses.newwin(1,100, 0,0)
  #win.bkgd('O')
  constraints = (0, area_width, 0, area_height)
  obj = po(1, 1, 125, 20, 0, 0, True)
  obj2 = po(124, 1, -125, 20, 0, 0, True)
  obj3 = po(1, 24, 125, 20, 0, 0, True)
  obj4 = po(124, 24, -125, 20, 0, 0, True)

  # gravity values
  obj.gravity = 100
  obj2.gravity = 100

  obj2.color += 1
  obj3.color += 2
  obj4.color += 3
  while True:
    # update physiscs objects
    obj.update(dt*dt_mult, constraints)
    #obj2.update(dt*dt_mult, constraints)
    #obj3.update(dt*dt_mult, constraints)
    #obj4.update(dt*dt_mult, constraints)

    win.erase()
    win.addstr(0, 0, "xv: {} / yv: {} / ypos: {}".format(round(obj.x_velocity, 2), round(obj.y_velocity, 2), obj.y_pos))
    win.refresh()

    # draw objects as squares
    draw_square(stdscr, int(obj.x_pos),int(obj.y_pos), square_size, obj.color)
    #draw_square(stdscr, int(obj2.x_pos),int(obj2.y_pos), square_size, color2)
    #draw_square(stdscr, int(obj3.x_pos),int(obj3.y_pos), square_size, color3)
    #draw_square(stdscr, int(obj4.x_pos),int(obj4.y_pos), square_size, color4)
    
    time.sleep(dt)
    # create some way to do boundries in curses
    
    #color = (color + 1) % 7
    #color2 = (color2 + 1) % 7
    #color3 = (color3 + 1) % 7
    #color4 = (color4 + 1) % 7



curses.wrapper(game_loop)