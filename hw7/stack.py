class Stack:
    """
    A stack data structure.
    """
    
    def __init__(self):
        """ 
        Create a new stack.
        """
        self.__lst = []
        
    def push(self, value):
        """
        Push a value onto the stack.

        Inputs:
            value (any): the value to push
        """
        self.__lst.append(value)
        
    def pop(self):
        """
        Pop a value off the stack.

        Return: the value popped off the stack
        """

        assert len(self.__lst) > 0
        
        value = self.__lst.pop()
        return value
    
    def peek(self):
        """
        Return the value at the top of the stack without removing it.

        Return: the value at the top of the stack
        """
        assert len(self.__lst) > 0

        return self.__lst[-1]
    
    def is_empty(self):
        """
        Return True if the stack is empty, False otherwise.
        """
        return len(self.__lst) == 0

    def to_string(self):
        '''
        Returns a string representation of the stack.
        '''
        s  = " TOP OF THE STACK\n"
        s += "-------------------\n"
    
        for v in reversed(self.__lst):
            s += str(v).center(20) + "\n"

        s += "-------------------\n"
        s += "BOTTOM OF THE STACK\n"
        return s


    def __repr__(self):
        return "repr:\n" + self.to_string()
    
    def __str__(self):
        return "str:\n" + self.to_string()

    def __eq__(self, other):
        assert isinstance(other, Stack)

        print("in stack equality method...")
        return self.__lst == other.__lst
