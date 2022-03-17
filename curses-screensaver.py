#! /usr/bin/env python3
# Brandon Vincent 20220317
# Uses python curses library to create a screensaver capable of reducing burn-in on LCD and possibly CRT terminals

import curses
import signal
import time
import sys

global height
global width
delay = 1 # delay between inverting, longer time may be required on terminals which operate at slower baudrates

if len(sys.argv) > 1:
	try:
		delay = float(sys.argv[1])
	except:
		print("syntax: curses-scrensaver.py <delay>")
def setup(): # create screen
	global stdscr
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)

def quit(a, b): # take down screen and restore terminal
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	exit()

def drawA(): # draw lines
	stdscr.clear()

	width = stdscr.getmaxyx()[1]
	height = stdscr.getmaxyx()[0]

	for line in range(0, height):
		if line % 2 == 0:
			try: # curses breaks if you try to write the last character on the line, catching the exception and ignoring it fixes this.
				stdscr.addstr(line, 0, "█" * width)
			except:
				pass

	stdscr.refresh()

def drawB(): # draw inverse lines
	stdscr.clear()

	width = stdscr.getmaxyx()[1]
	height = stdscr.getmaxyx()[0]

	for line in range(0, height):
		if line % 2 != 0:
			try:
                        	stdscr.addstr(line, 0, "█" * width)
			except:
				pass

	stdscr.refresh()

def main():

	signal.signal(signal.SIGINT, quit)
	setup()
	width = stdscr.getmaxyx()[1]
	height = stdscr.getmaxyx()[0]

	while True:
		drawA()
		time.sleep(delay)
		drawB()
		time.sleep(delay)

if __name__ == "__main__":
    main()


