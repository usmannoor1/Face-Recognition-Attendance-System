from tkinter import *
from math import *

from math import *


#                                           Stack Implementaion Start                                    #

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def check(self):
        if self.head == None:
            return False
        else:
            return True

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

        # Remove element that is the current head (start of the stack)

    def pop(self):

        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            # the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

        # Returns the head node data

    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

        # Prints out the stack

    def printStack(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while iternode is not None:
                print(iternode.data, " ", end=" ")
                iternode = iternode.next
            return


#                                           Stack Implementaion End                                     #

User_input = ""


def press(num):
    global User_input

    User_input = User_input + str(num)

    Result.set(User_input)


def split(User_input):
    return [char for char in User_input]


#                               Validity Check Function And Result Calculation                         #

def equalpress():
    global User_input
    if(len(User_input) != 0):
        try:
            temp_valid = ""
            Mystack = Stack()  # stack object
            New_Stack = Stack()
            automated_stack = Stack()
            Mystack.push('$')  # stack symbol
            automated_stack.push('$')  # stack symbol

            for i in User_input:  # split string into char
                New_Stack.push(i)

            while New_Stack.check():  # copy one stack to another beacuse of order
                temp = New_Stack.pop()
                Mystack.push(temp)

            state = 0

            while 1:
                if state == 0 and Mystack.peek() == '(':
                    automated_stack.push('(')
                    Mystack.pop()
                    state = 0
                    if Mystack.peek() == ')' or Mystack.peek() == '+' or Mystack.peek() == '-' or Mystack.peek() == '*' or Mystack.peek() == '/':
                        temp_valid = "invalid"
                        break
                    state = 0
                elif state == 0 and Mystack.peek() == '1' or Mystack.peek() == '2' or Mystack.peek() == '3' or Mystack.peek() == '4' or Mystack.peek() == '5' or Mystack.peek() == '6' or Mystack.peek() == '7' or Mystack.peek() == '8' or Mystack.peek() == '9' or Mystack.peek() == '0':
                    state = 2
                    Mystack.pop()
                    if automated_stack.peek() == '$' and Mystack.peek() == '$':
                        temp_valid = "Valid"
                        break
                elif state == 2 and Mystack.peek() == '+' or Mystack.peek() == '-' or Mystack.peek() == '*' or Mystack.peek() == '/':
                    state = 0
                    Mystack.pop()
                    if Mystack.peek() == '$' or Mystack.peek() == '+' or Mystack.peek() == '-' or Mystack.peek() == '*' or Mystack.peek() == '/':
                        temp_valid = "Invalid"
                        break
                elif state == 2 and Mystack.peek() == ')':
                    Mystack.pop()
                    automated_stack.pop()
                    if automated_stack.peek() == '$' and Mystack.peek() == '$':
                        temp_valid = "Valid"
                        break
                elif state == 0 and Mystack.peek() == ')' or automated_stack.peek() == '$' or Mystack.peek() == '+' or Mystack.peek() == '-' or Mystack.peek() == '*' or Mystack.peek() == '/':
                    vall = Mystack.pop()
                    if Mystack.peek() == "$":
                        temp_valid = "Invalid"
                        break
                else:
                    temp_valid = "Invalid"
                    break

            if temp_valid == "Valid":
                Value = str(eval(User_input))
                Result.set(Value)
                validity.set('Valid')
                User_input = ""

            else:
                Result.set(" Cannot Process the Expression ")
                validity.set('Invalid')
                User_input = ""
        except:
            User_input = ""





def clear():
    global User_input
    User_input = ""
    Result.set('Enter Arithmetic Expression')
    validity.set('PDA Result')


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="white")

    # set the title of GUI window
    gui.title("PDA Validity Calculator")

    # set the configuration of GUI window
    gui.geometry("300x168")

    # StringVar() is the variable class
    # we create an instance of this class
    Result = StringVar()
    validity = StringVar()

    # create the text entry box for
    # showing the User_input .
    User_input_field = Entry(gui, textvariable=Result)
    Validity_field = Entry(gui, textvariable=validity)
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    Validity_field.grid(columnspan=4, ipadx=90)
    User_input_field.grid(columnspan=4, ipadx=90)

    Result.set('Enter Mathematical Expression')
    validity.set('PDA Result')
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='white', bg='black',
                     command=lambda: press(1), height=1, width=9)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='black',
                     command=lambda: press(2), height=1, width=9)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='black',
                     command=lambda: press(3), height=1, width=9)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='white', bg='black',
                     command=lambda: press(4), height=1, width=9)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='black',
                     command=lambda: press(5), height=1, width=9)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='black',
                     command=lambda: press(6), height=1, width=9)
    button6.grid(row=3, column=2)

    button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                     command=lambda: press(9), height=1, width=9)
    button9.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='black',
                     command=lambda: press(8), height=1, width=9)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='black',
                     command=lambda: press(9), height=1, width=9)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='black',
                     command=lambda: press(0), height=1, width=9)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='white', bg='red',
                  command=lambda: press("+"), height=1, width=9)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='red',
                   command=lambda: press("-"), height=1, width=9)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' x ', fg='white', bg='red',
                      command=lambda: press("*"), height=1, width=9)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='red',
                    command=lambda: press("/"), height=1, width=9)
    divide.grid(row=5, column=3)

    bracketstart = Button(gui, text=' ( ', fg='white', bg='red',
                          command=lambda: press("("), height=1, width=9)
    bracketstart.grid(row=5, column=1)

    bracketend = Button(gui, text=' ) ', fg='white', bg='red',
                        command=lambda: press(")"), height=1, width=9)
    bracketend.grid(row=5, column=2)

    equal = Button(gui, text=' = ', fg='white', bg='red',
                   command=equalpress, height=1, width=9)
    equal.grid(row=6, column=3)

    clear = Button(gui, text='Clear', fg='white', bg='red',
                   command=clear, height=1, width=9)
    clear.grid(row=6, column=0)

    # start the GUI
    gui.mainloop()
