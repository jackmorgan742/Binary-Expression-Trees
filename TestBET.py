import unittest
from BET import BETNode, create_trees, find_solutions



class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    
    def test_add_left(self):
        '''
        tests functionality of add_left function within BETNode class
        '''
        bet = BETNode('-')
        bet.add_left(BETNode('Q'))
        self.assertEqual('(Q-None)', repr(bet))


    def test_add_right(self):
        '''
        tests functionality of add_right function within the BETNode class
        '''
        bet = BETNode('*')
        bet.add_right(BETNode('5'))
        self.assertEqual('(None*5)', repr(bet))


    def test_evaluate_tree1(self):
        '''
        tests functionality of evaluate function within BETNode class
        ASCII art of the tree is provided under unit test for visualization
        '''
        root = BETNode('+')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('A'))
        root.left.add_left(BETNode('Q'))
        root.left.add_right(BETNode('7'))
        self.assertEqual('((Q*7)+A)', repr(root))
        self.assertEqual(root.evaluate(), 85)
        '''
            +
           / \
          *   A
         / \  
        Q   7
        '''


    def test_evaluate_tree2(self):
        '''
        tests functionality of evaluate function within BETNode class
        ASCII art of the tree is provided under unit test for visualization
        '''
        root = BETNode('*')
        root.add_left(BETNode('-'))
        root.add_right(BETNode('+'))
        root.left.add_left(BETNode('-'))
        root.left.left.add_left(BETNode('A'))
        root.left.left.add_right(BETNode('Q'))
        root.left.add_right(BETNode('+'))
        root.left.right.add_left(BETNode('4'))
        root.left.right.add_right(BETNode('5'))
        root.right.add_right(BETNode('/'))
        root.right.right.add_right(BETNode('J'))
        root.right.right.add_left(BETNode('K'))
        root.right.add_left(BETNode('*'))
        root.right.left.add_left(BETNode('8'))
        root.right.left.add_right(BETNode('7'))
        self.assertEqual('(((A-Q)-(4+5))*((8*7)+(K/J)))', repr(root))
        self.assertEqual(root.evaluate(), -1140)
        '''
                         *
                      /     \
                    -          +
                  /  \        /  \
                 -    +      *    //
                / \  / \    /\   / \
                A Q  4 5    8 7  K  J
        '''


    def test_evaluate_tree3(self):
        '''
        tests functionality of evaluate function within BETNode class 
        (specifically what happens when dividing by zero)
        ASCII art of the tree is provided under unit test for visualization
        '''
        root = BETNode('/')
        root.add_left(BETNode('+'))
        root.add_right(BETNode('-'))
        root.left.add_left(BETNode('5'))
        root.left.add_right(BETNode('5'))
        root.right.add_left(BETNode('3'))
        root.right.add_right(BETNode('3'))
        self.assertEqual('((5+5)/(3-3))', repr(root))
        self.assertEqual(root.evaluate(), 'error, can not divide by zero')
        '''
            //
           /   \
          +     -
         / \   / \
        5   5 3   3
        '''

 

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        '''
        tests the functionality of the create_trees function with a hand of 4 unique cards
        '''
        cards1 = [1, 2, 3, 4]
        trees1 = create_trees(cards1)
        self.assertEqual(len(trees1), 7680)


    def test_hand2(self):
        '''
        tests the functionality of the create_trees function with a hand of 4 duplicates cards
        '''
        cards2 = [2, 2, 2, 2]
        trees2 = create_trees(cards2)
        self.assertEqual(len(trees2), 320)
        



class TestFindSolutions(unittest.TestCase):
    def test0sols(self): 
        '''
        tests functionality of find_solutions function with a 4 card hand that gives 0 solutions
        '''

        #Did not have enough time to debug the keyerrors these throw but the unit test is still correctly made
        cards3 = ['A', 2, 3, 5]
        solutions3 = find_solutions(cards3)
        self.assertEqual(len(solutions3), 0)
        

    def test_A23Q(self): 
        '''
        tests functionality of find_solutions function with a 4 card hand that gives 33 solutions
        '''

        #Did not have enough time to debug the keyerrors these throw but the unit test is still correctly made
        cards4 = ['A', 2, 3, 'Q']
        solutions4 = find_solutions(cards4)
        self.assertEqual(len(solutions4), 33)



if __name__ == '__main__':
    unittest.main()