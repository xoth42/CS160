import MergeSort, unittest
class tests(unittest.TestCase):
    def testMerge(self):
        # equivalence tests & more
        inputsOutputs = (([0],[0],          [0,0]),
                        ([0],[],            [0]),
                        ([],[],             []),
                        ([1,3,5],[2],       [1,2,3,5]),
                        ([1,2,3],[4,5,6],   [1,2,3,4,5,6]),
                        ([4,4],[4,4],       [4,4,4,4]),
                        ([-1],[0],          [-1,0]),
                        ([-1,0,4],[-0.5,5], [-1,-0.5,0,4,5]))
        for i in range(len(inputsOutputs)):
            self.assertEqual(inputsOutputs[i][2],MergeSort.merge(inputsOutputs[i][0],inputsOutputs[i][1]))
if __name__=="__main__":
    unittest.main()