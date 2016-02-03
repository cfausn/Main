"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates preorder expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Sean Strout (sps@cs.rit.edu)

Author: Colin Fausnaught
"""

from derp_node import *
    
##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From an infix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    if tokens == None:
        return None
    elif len(tokens) == 0:
        return None
    else:
        if tokens[0].isdigit() == False and tokens[0].isidentifier() == False:
            if tokens[0] == '*':
                if tokens[1].isdigit() == True:
                    return MultiplyNode(parse(tokens[1]),parse(tokens[2:]))
                elif tokens[1].isidentifier() == True:
                    return MultiplyNode(parse(tokens[1]),parse(tokens[2:]))
                else:
                    return MulyiplyNode(parse(tokens[1:]),parse(listHelper(tokens[2:])))
                        
                
            elif tokens[0] == '//':
                if tokens[1].isdigit() == True:
                    return DivideNode(parse(tokens[1]),parse(tokens[2:]))
                elif tokens[1].isidentifier() == True:
                    return DivideNode(parse(tokens[1]),parse(tokens[2:]))
                else:
                    return DivideNode(parse(tokens[1:]),parse(listHelper(tokens[2:])))
                    
            elif tokens[0] == '+':
                if tokens[1].isdigit() == True:
                    return AddNode(parse(tokens[1]),parse(tokens[2:]))
                elif tokens[1].isidentifier() == True:
                    return AddNode(parse(tokens[1]),parse(tokens[2:]))
                else:
                    return AddNode(parse(tokens[1:]),parse(listHelper(tokens[2:])))
                
            elif tokens[0] == '-':
                if tokens[1].isdigit() == True:
                    return SubtractNode(parse(tokens[1]),parse(tokens[2:]))
                elif tokens[1].isidentifier() == True:
                    return SubtractNode(parse(tokens[1]),parse(tokens[2:]))
                else:
                    return SubtractNode(parse(tokens[1:]),parse(listHelper(tokens[2:])))
        
        elif tokens[0].isdigit() == True:
            if isinstance(tokens,str):
                return int(tokens)
            else:
                return int(tokens[0])
        
        elif tokens[0].isidentifier() == True:
            if isinstance(tokens,str):
                return tokens
            else:
                return tokens[0]


##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""
    
    if isinstance(node, MultiplyNode) == True:
        if isOperator(node.left) == True and isOperator(node.right) == True:
            return "(" + infix(node.left) + ") * (" + infix(node.right) + ")"
        elif isOperator(node.left) == True:
            return "(" + infix(node.left) + " * " + str(node.right) + ")"
        elif isOperator(node.right) == True:
            return "(" + str(node.left) + " * " + infix(node.right) + ")"
        else:
            return "(" + str(node.left) + " * " + str(node.right) + ")"
        
    elif isinstance(node, DivideNode) == True:
        if isOperator(node.left) == True and isOperator(node.right) == True:
            return "(" + infix(node.left) + ") // (" + infix(node.right) + ")"
        elif isOperator(node.left) == True:
            return "(" + infix(node.left) + " // " + str(node.right) + ")"
        elif isOperator(node.right) == True:
            return "(" + str(node.left) + " // " + infix(node.right) + ")"
        else:
            return "(" + str(node.left) + " // " + str(node.right) + ")"
        
    elif isinstance(node, AddNode) == True:
        print(node)
        if isOperator(node.left) == True and isOperator(node.right) == True:
            return "(" + infix(node.left) + ") + (" + infix(node.right) + ")"
        elif isOperator(node.left) == True:
            return "(" + infix(node.left) + " + " + str(node.right) + ")"
        elif isOperator(node.right) == True:
            return "(" + str(node.left) + " + " + infix(node.right) + ")"
        else:
            return "(" + str(node.left) + " + " + str(node.right) + ")"
        
    elif isinstance(node, SubtractNode) == True:
        if isOperator(node.left) == True and isOperator(node.right) == True:
            return "(" + infix(node.left) + ") - (" + infix(node.right) + ")"
        elif isOperator(node.left) == True:
            return "(" + infix(node.left) + " - " + str(node.right) + ")"
        elif isOperator(node.right) == True:
            return "(" + str(node.left) + " - " + infix(node.right) + ")"
        else:
            return "(" + str(node.left) + " - " + str(node.right) + ")"
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    if isinstance(node, MultiplyNode) == True:
        if not (node.left == None and node.right == None):
            if isOperator(node.left) == True and isOperator(node.right) == True:
                return evaluate(node.left, symTbl)  *  evaluate(node.right, symTbl)
            elif isOperator(node.left) == True and isinstance(node.right, int) == True:
                return evaluate(node.left, symTbl) * int(node.right)
            elif isOperator(node.left) == True and isinstance(node.right, str) == True:
                return evaluate(node.left, symTbl) * symTbl[node.right]
            elif isOperator(node.right) == True and isinstance(node.left, int) == True:
                return int(node.left) * evaluate(node.right,symTbl)
            elif isOperator(node.right) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] * evaluate(node.right,symTbl)
            elif isinstance(node.left,str) == True and isinstance(node.right, int) == True:
                return symTbl[node.left] * int(node.right)
            elif isinstance(node.left, int) == True and isinstance(node.right, str) == True:
                return int(node.left) * symTbl[node.right]
            elif isinstance(node.left, int) == True and isinstance(node.right, int) == True:
                return int(node.left) * int(node.right)
            elif isinstance(node.left, str) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] * symTbl[node.right]
        
    elif isinstance(node, DivideNode) == True:
        if not (node.left == None and node.right == None):
            
            if isOperator(node.left) == True and isOperator(node.right) == True:
                return evaluate(node.left, symTbl)  //  evaluate(node.right, symTbl)
            elif isOperator(node.left) == True and isinstance(node.right, int) == True:
                return evaluate(node.left, symTbl) // int(node.right)
            elif isOperator(node.left) == True and isinstance(node.right, str) == True:
                return evaluate(node.left, symTbl) // symTbl[node.right]
            elif isOperator(node.right) == True and isinstance(node.left, int) == True:
                return int(node.left) // evaluate(node.right,symTbl)
            elif isOperator(node.right) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] // evaluate(node.right,symTbl)
            elif isinstance(node.left,str) == True and isinstance(node.right, int) == True:
                return symTbl[node.left] // int(node.right)
            elif isinstance(node.left, int) == True and isinstance(node.right, str) == True:
                return int(node.left) // symTbl[node.right]
            elif isinstance(node.left, int) == True and isinstance(node.right, int) == True:
                return int(node.left) // int(node.right)
            elif isinstance(node.left, str) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] // symTbl[node.right]
        
    elif isinstance(node, AddNode) == True:
        if not (node.left == None and node.right == None):
            if isOperator(node.left) == True and isOperator(node.right) == True:
                return evaluate(node.left, symTbl)  +  evaluate(node.right, symTbl)
            elif isOperator(node.left) == True and isinstance(node.right, int) == True:
                return evaluate(node.left, symTbl) + int(node.right)
            elif isOperator(node.left) == True and isinstance(node.right, str) == True:
                return evaluate(node.left, symTbl) + symTbl[node.right]
            elif isOperator(node.right) == True and isinstance(node.left, int) == True:
                return int(node.left) + evaluate(node.right,symTbl)
            elif isOperator(node.right) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] + evaluate(node.right,symTbl)
            elif isinstance(node.left,str) == True and isinstance(node.right, int) == True:
                return symTbl[node.left] + int(node.right)
            elif isinstance(node.left, int) == True and isinstance(node.right, str) == True:
                return int(node.left) + symTbl[node.right]
            elif isinstance(node.left, int) == True and isinstance(node.right, int) == True:
                return int(node.left) + int(node.right)
            elif isinstance(node.left, str) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] + symTbl[node.right]
        
    elif isinstance(node, SubtractNode) == True:
        if not (node.left == None and node.right == None):
            if isOperator(node.left) == True and isOperator(node.right) == True:
                return evaluate(node.left, symTbl)  -  evaluate(node.right, symTbl)
            elif isOperator(node.left) == True and isinstance(node.right, int) == True:
                return evaluate(node.left, symTbl) - int(node.right)
            elif isOperator(node.left) == True and isinstance(node.right, str) == True:
                return evaluate(node.left, symTbl) - symTbl[node.right]
            elif isOperator(node.right) == True and isinstance(node.left, int) == True:
                return int(node.left) - evaluate(node.right,symTbl)
            elif isOperator(node.right) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] - evaluate(node.right,symTbl)
            elif isinstance(node.left,str) == True and isinstance(node.right, int) == True:
                return symTbl[node.left] - int(node.right)
            elif isinstance(node.left, int) == True and isinstance(node.right, str) == True:
                return int(node.left) - symTbl[node.right]
            elif isinstance(node.left, int) == True and isinstance(node.right, int) == True:
                return int(node.left) - int(node.right)
            elif isinstance(node.left, str) == True and isinstance(node.right, str) == True:
                return symTbl[node.left] - symTbl[node.right]


  
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    inFile = input("Herp, enter symbol table file: ")
    symTbl = dict()
    tempLst = []

    print("Symbol Table:")
    for line in open(inFile):
        tempLst = line.split(' ')
        symTbl[tempLst[0]] = int(tempLst[1])
        print('name: ' + tempLst[0] + ' => Value: ' + tempLst[1])
        
    print()
    print("Herp, enter prefix expressions, e.g.: + 10 20 (RETURN to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tempLst = prefixExp.split(' ')
        
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        tr = parse(tempLst)
        
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        newString = infix(tr)
        
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression: " + newString)
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        derp = evaluate(tr,symTbl)
        
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation: " + str(derp))
         
    print("Goodbye Herp :(")
                
def listHelper(lst):
    """
    creates and returns a list to be parsed. The returned list will exlude all
    parts of the list that will already be stored by parse.

    :param lst: a list to be converted

    :rtype: list
    :return: the list excluding all values that need to be excluded.
    """
    prevList = []
    index = 0
    for node in lst:
        if len(prevList) == 0:
            prevList += node
            index+=1
        else:
            if (prevList[-1].isdigit or prevList[-1].isidentifier) and \
               (node.isdigit or node.isidentifier):
                return lst[index+1:]
            
            index +=1

def isOperator(node):
    """
    checks to see if the passed node is an operator instance, then returns True or False

    :rtype: Bool
    :return: True/False 
    """
    
    if isinstance(node, MultiplyNode) == True or isinstance(node, DivideNode) == True\
       or isinstance(node, AddNode) == True or isinstance(node, SubtractNode) == True:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
