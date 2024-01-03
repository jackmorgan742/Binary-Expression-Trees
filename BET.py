from itertools import permutations, product

class BETNode:
    """
    Node for binary expression tree
    """
    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}


    def __init__(self, value, left=None, right=None):
        '''
        Initializes BETNode class variables for other functions
        '''
        self.value = value
        self.left = left
        self.right = right


    # Hashes BETs (so they can be stored in sets)
    # and compare them (so unittests can be written more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    

    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    
    def add_left(self, node):
        '''
        adds node as the left child
        '''
        self.left = node


    def add_right(self, node):
        '''
        adds node as the right child
        '''
        self.right = node


    def evaluate(self): 
        '''
        recursively evaluates the binary expression tree from bottom to top,
        returns the expression evaluated
        '''

        # empty tree
        if self.value is None:
            return 0
    
        # leaf node
        if (self.left is None) and (self.right is None):
            return BETNode.CARD_VAL_DICT[self.value]

        # evaluate left tree
        left_sum = self.left.evaluate()
    
        # evaluate right tree
        right_sum = self.right.evaluate()
    
        # check which operation to apply
        if self.value == '+':
            return left_sum + right_sum
    
        elif self.value == '-':
            return left_sum - right_sum
    
        elif self.value == '*':
            return left_sum * right_sum
    
        else:
            #to ensure dividing by zero does not happen
            if right_sum == 0:
                return 'error, can not divide by zero'
            else:
                return left_sum // right_sum


    def __repr__(self):
        '''
        returns string representation of the BET
        '''
        if self.left is None and self.right is None:
            return str(self.value)
        else:
            return f'({str(self.left)}{str(self.value)}{str(self.right)})'



def create_trees(cards):
    '''
    returns a set of every valid tree for a given collection of 4 cards
    '''

    # Define the five valid shapes for binary expression trees
    shapes = ['CCCCXXX', 'CCCXCXX', 'CCCXXCX', 'CCXCXCX', 'CCXCCXX']

    # Creates a list of all operators
    operators = ['+', '-', '*', '/']

    # Create a set to store all valid binary expression trees
    trees_combos = set()

    # Generate all permutations of the cards
    card_permutations = list(permutations(cards))

    operator_permutations = list(product(operators, repeat=3))

    # Generate all possible binary expression trees for each card permutation and shape
    for combo_cards in card_permutations:
        for op_combo in operator_permutations:
            for shape in shapes:

                tree = BETNode(op_combo[0])

                if shape == 'CCCCXXX':
                    tree.add_right(BETNode(op_combo[1]))
                    tree.add_left(BETNode(combo_cards[0]))

                    if tree.right is not None:
                        tree.right.add_right(BETNode(op_combo[2]))
                        tree.right.right.add_right(BETNode(combo_cards[0]))
                        tree.right.right.add_left(BETNode(combo_cards[1]))
                        tree.right.add_left(BETNode(combo_cards[2]))
                        tree.add_left(BETNode(combo_cards[3]))

                elif shape == 'CCXCCXX':
                    tree.add_right(BETNode(op_combo[1]))
                    tree.add_left(BETNode(op_combo[2]))
                    if tree.right is not None and tree.left is not None:
                        tree.right.add_right(BETNode(combo_cards[0]))
                        tree.right.add_left(BETNode(combo_cards[1]))
                        tree.left.add_right(BETNode(combo_cards[2]))
                        tree.left.add_left(BETNode(combo_cards[3]))
                        
                elif shape == 'CCXCXCX':
                    tree.add_right(BETNode(combo_cards[0]))
                    tree.add_left(BETNode(op_combo[1]))

                    if tree.left is not None:
                        tree.left.add_right(BETNode(combo_cards[1]))
                        tree.left.add_left(BETNode(op_combo[2]))
                        tree.left.left.add_right(BETNode(combo_cards[2]))
                        tree.left.left.add_left(BETNode(combo_cards[3]))

                elif shape == 'CCCXXCX':
                    tree.add_right(BETNode(combo_cards[0]))
                    tree.add_left(BETNode(op_combo[1]))

                    if tree.left is not None:
                        tree.left.add_right(BETNode(op_combo[2]))
                        tree.left.add_left(BETNode(combo_cards[1]))
                        tree.left.right.add_right(BETNode(combo_cards[2]))
                        tree.left.right.add_left(BETNode(combo_cards[3]))

                elif shape == 'CCCXCXX':
                    tree.add_right(BETNode(op_combo[1]))
                    tree.add_left(BETNode(combo_cards[0]))

                    if tree.right is not None:
                        tree.right.add_right(BETNode(combo_cards[1]))
                        tree.right.add_left(BETNode(op_combo[2]))
                        tree.right.left.add_right(BETNode(combo_cards[2]))
                        tree.right.left.add_left(BETNode(combo_cards[3]))
                
                trees_combos.add(tree)

    return trees_combos


def find_solutions(cards):
    '''
    returns a set of all the ways to solve the game 24 (the end value equals 24) 
    '''

    trees = create_trees(cards)
    result = set()

    for tree in trees:
        if tree.evaluate() == 24:
            result.add(repr(tree))

    return result
