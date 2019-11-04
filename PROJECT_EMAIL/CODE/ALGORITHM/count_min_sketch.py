import numpy as np
import mmh3

class CountMinSketch(object):
    ''' Class for a CountMinSketch data structure
    '''
    def __init__(self, width, width, seeds):
        ''' 
        This method initializes the data structure
        @param width int: Width of the table 	(Number of Hash Functions)
        @param length int: length of the table  (Range of the hash function)
        @param seeds list: Random seed list     [np.random.randint(param_w, size = param_d)]
        '''
        self.width = width
        self.length = length
        self.table = np.zeros([width, length])  # Create empty table
        self.seed = [3, 1]

    def sketch_table(self):
    	'''
    	This method returns the Sketch_Table
    	'''
    	return self.table

    def increment(self, key):
        '''
        This method increments the frequency of the key in Sketch_Table
        @param key str: A string to add to the CMS
        '''
        for i in range(0, self.width):
            index = mmh3.hash(key, self.seed[i]) % self.length
            print(index)
            self.table[i, index] = self.table[i, index]+1

    def get_hashindices(self, key) :
    	''' 
    	This method returns the indices of a key in Sktech_Table
        '''
	index_list = []
    	for i in range(0, self.width):
    		index = mmh3.hash(key, self.seed[i]) % self.length
    		index_list.append(index)

    	return index_list

    def estimate(self, key):
        ''' 
        This method estimates if the key is in Sketch_Table
        @param key str: A string to check
        '''
        min_est = self.width
        for i in range(0, self.width):
            index = mmh3.hash(key, self.seed[i]) % self.length
            if self.table[i, index] < min_est:
                min_est = self.table[i, index]
        return min_est

    # def merge(self, new_cms):
    #     ''' Method to combine two count min sketches
    #     @param new_cms CountMinSketch: Another CMS object
    #     '''
    #     return self.table + new_cms


cms = CountMinSketch(2, 16369, [3,1])
cms.increment("sai")
cms.increment("sai")
cms.increment("sree")
cms.increment("sreee")
list_ = cms.get_hashvalues("sai")
print(list_)
table = cms.sketch_table()
print(table[0, list_[0]])
print(table[1, list_[1]])
print(cms.estimate("sre"))
