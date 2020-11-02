from collections import Counter
from itertools import chain

graphs = [[1, 2, 3], [4, 5], [6]] 
test1 = [1, 2, 3, 6] 
test2 = [99]

# count all occurences from numbers in graphs
source = Counter(chain.from_iterable(graphs)) # {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}


# count whatever is needed for your inputs and compare to all_of_them 
what = Counter(test1)                           # {1:1, 2:1, 3:1, 6:1}
print(all ( source.get(i,0) >= what[i] for i in what))

what = Counter(test2)                           # {99:1}
print(all ( source.get(i,0) >= what[i] for i in what))