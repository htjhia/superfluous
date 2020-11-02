def create_perm(actual_list, add_list):
    """
    https://stackoverflow.com/questions/64614220/python-permutation-using-recursion
    Recursive function for the creation of the permutation
    """
    if len(add_list)==1:
        # If you reach the last item, print the found permutation
        # (add the 0 at the beginning)
        print([0] + actual_list + add_list)
    else:
        for i in add_list:
            # Go one step deeper by removing one item and add it to the found permutation
            new_add_list = add_list.copy()
            new_add_list.remove(i)
            # Make the recursion
            create_perm(actual_list + [i], new_add_list)

li = [i for i in range(1, 10)]

for i in create_perm([], li):
    print(i)