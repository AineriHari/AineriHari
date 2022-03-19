"""
List:
    1. List is a collection of different data types.
    2. it accepts duplicate values
    3. it is a mutable
    4. Lists are ordered so we can fetch values by index.
    5. Lists uses the same address for same data which menas another variable list2 is tagging to list1.
        Ex: list.copy()"""


def List(Lst):
    #append: add the value at the end of the list, Slices Lst[len(Lst):] = [2]. it retuns None
    print("Append:{}".format(Lst.append(2)))

    #remove: remove the values from the list, Slices del Lst[Lst.index(1)]. it returns None
    print("Remove:{}".format(Lst.remove(1)))

    #copy: copy all the elements from lst to lst1, Slices lst1 = Lst[:] or lst1 = Lst.
    lst1 = Lst.copy() #it returns None
    print("Copy:{}".format(lst1)) 

    #count: returns the number values occurances. it retuns int
    print("Count:{}".format(Lst.count(1)))

    #extend: it appendes multiple values to list, Slices Lst[len(Lst):] = [2, 3] or Lst[len(Lst):len(Lst)] = [2, 3] or Lst += [2, 3]. it returns None
    print("Extend:{}".format(Lst.extend([2, 3])))

    #index: returns the index of the passed value. it returns value
    print("index:{}".format(Lst.index(3)))

    #pop: it returns the values which is present at index 1, pop() it returns the end of the value Slices, Lst[len(Lst)-1] or default is -1. it returns value
    #Stack: last in first out (LIFO)
    print("pop:{}".format(Lst.pop(1)))
    
    #insert: insert the value at index, Slices Lst[0:0] = [1], insert(index, value). it return None
    print("Insert:{}".format(Lst.insert(0, 1)))

    #reverse: returns the values in reverse, Slices Lst[::-1]. it return None
    print("Reverse:{}".format(Lst.reverse()))

    #sort: it sort the list of values. it return None
    print("Sort:{}".format(Lst.sort()))

    #clear: remove all the values from the list, Slices del Lst[:]. it return None
    print("Clear:{}".format(Lst.clear()))
