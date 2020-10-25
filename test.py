import unittest
#Import our function from task1 and task2
from task1 import mostFreq
from task2 import reverseIterative, reverseRecurse

class TestSum(unittest.TestCase):
    print("Unit testing...\n")

    #Set up a number of test cases and assert the correct result and compare it to the result we get
    def test_mostFrequent(self):
        print("\nUnit testing mostFreq function...\n")

        self.assertEqual(mostFreq([1,2,3]), [1,2,3])
        self.assertEqual(mostFreq([8,1,5,6,7,0,1,1]), [1])
        self.assertEqual(mostFreq([-1,-2,-3,-1,-2]), [-1,-2])
        self.assertEqual(mostFreq([-1,-2,3,3]), [3])
        self.assertEqual(mostFreq([8]), [8])
        self.assertEqual(mostFreq(None), None)
        self.assertEqual(mostFreq([]), None)

    def test_reverseIterative(self):
        print("\nUnit testing recurseIterative function...\n")

        self.assertEqual(reverseIterative("hotdog"), "godtoh")
        self.assertEqual(reverseIterative("HOTDOG"), "GODTOH")
        self.assertEqual(reverseIterative("navan"), "navan")
        self.assertEqual(reverseIterative("hanna"), "annah")
        self.assertEqual(reverseIterative("Hanna"), "annaH")
        self.assertEqual(reverseIterative("conor   "), "   ronoc")
        self.assertEqual(reverseRecurse("Mastercard is a great company"), "ynapmoc taerg a si dracretsaM")
        self.assertEqual(reverseIterative(""), "")
        self.assertEqual(reverseIterative(None), None)

    def test_reverseRecurse(self):
        print("\nUnit testing recurseRecurse function...\n")

        result = reverseRecurse("hotdog")
        self.assertEqual(result, "godtoh")
        print("hotdog ->",result)

        result = reverseRecurse("HOTDOG")
        self.assertEqual(result, "GODTOH")
        print("HOTDOG ->",result)

        result = reverseRecurse("navan")
        self.assertEqual(result, "navan")
        print("navan ->",result)

        result = reverseRecurse("hanna")
        self.assertEqual(result, "annah")
        print("hanna ->",result)

        result = reverseRecurse("Hanna")
        self.assertEqual(result, "annaH")
        print("Hanna ->",result)


        result = reverseRecurse("conor   ")
        self.assertEqual(result, "   ronoc")
        print("conor    ->",result)

        result = reverseRecurse("Mastercard is a great company")
        self.assertEqual(result, "ynapmoc taerg a si dracretsaM")
        print("Mastercard is a great company ->", result)

        result = reverseRecurse("")
        self.assertEqual(result, "")
        print(" \"  \" -> \"",result,"\"")

        result = reverseRecurse(None)
        self.assertEqual(result, None)
        print("None ->",result)

if __name__ == '__main__':
    unittest.main()