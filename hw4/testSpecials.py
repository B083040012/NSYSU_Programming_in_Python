#B083040012
import traceback
from PyPA4 import *
def testSpecials():
    printf('''Backslashes are handled automatically, because printf receives each of the 
    following as just one character: tab:\t, backslash:\\, newline:\n''')
    printf('This is how you get a "%%" symbol.\n')
    printf('The following line will do nothing:\n')
    printf()
    printf('Any of the following lines will crash:\n')
    try:
        printf('%')
    except SyntaxError:
        traceback.print_exc()
        
    try:
        printf('%Q')
    except SyntaxError:
        traceback.print_exc()
    try:
        printf('%',1)
    except SyntaxError:
        traceback.print_exc()
    try:
        printf('%Q',1)
    except ValueError:
        traceback.print_exc()
    try:
        printf('%s','1','2')
    except SyntaxError:
        traceback.print_exc()
    try:
        printf('1','2')
    except SyntaxError:
        traceback.print_exc()

if (__name__=="__main__"):
    testSpecials()
