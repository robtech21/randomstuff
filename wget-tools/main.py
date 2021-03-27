#!/usr/bin/env python3

'''
Minimal wget CLI utility or module
Made by Robert Furr
2021
'''

from os import system

pnt     = print
inpt    = input
dosudo  = False


def setsudo(state=False):
  '''Sets the sudo state'''
  if state == True:
    dosudo = True
    pnt('Sudo has been set to True')
  else:
    dosudo = False
    pnt('Sudo has been set to False')

def wget(args):
  '''Runs wget'''
  if dosudo == True:
    system('sudo wget '+args)
  else:
    system('wget '+args)
    
if __name__ == '__main__':
  pnt('Wget Utility')
  while True:
    cmd = inpt('base > ')
    
    if cmd == 'wget':
      cmd1 = inpt('wget args > ')
      wget(cmd1)
      
    if cmd == 'exit':
      exit(0)
      
    if cmd == 'clear':
      system('clear')
      
    if cmd == 'setsudo':
      cmd1 = inpt('sudo state > ')
      if cmd1 == 'True':
        cmd1 = True
      else:
        cmd1 = False
      setsudo(cmd1)
      
    if cmd == 'help':
      pnt('''Help:
      
      help:    displays this help
      wget:    runs wget
      clear:   clears the screen
      setsudo: sets the sudo state
      exit:    exits the program''')
