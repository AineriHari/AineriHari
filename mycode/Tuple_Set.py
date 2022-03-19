"""
Tuple:
    1. Tuple is a colection of different data types.
    2. it accepts duplicates.
    3. it is immutables.
    4. Tuples are ordered so we can fetch values by index.
    5. Tuples uses the same address for same data which means another variable tuple2 name is tagging to tuple1.
        Ex: tuple.copy()

 Set:
    1. Set is a collection of different data types.
    2. it won't accepts duplicates.
    3. it is mutable.
    4. Sets are unordered so we can fetch values by index.
    5. sets uses the same address for same data which means another variable set2 name is tagging to set1.
        Ex: set.copy()
"""

def Tuple(arg):
    #returns the number of occurences of item in arg.
    #arg.count("iterable item")
    tuple.count.__doc__

    #accepts item and returns the index of the item in arg.
    #arg.index("iterable item")
    tuple.index.__doc__

def Set(arg):
    #add: Annd an element to a set.
    #this as no effect if the element is already present.
    #returns None.
    #set.add("iterable item")
    set.add.__doc__

    #clear: remove all the elements from this set.
    #returns None.
    #set.clear()
    set.clear.__doc__

    #copy:copy all the items to another set.
    #return None.
    #set.copy()
    set.copy.__doc__

    #difference: Return the difference of two or more sets as a new set.
    #(i.e. all elements that are in this set but not the others.)
    #it intersections the two sets.
    #set.differnce(compare set) --> retun new set for set.
    set.difference.__doc__

    #differnce_update: Remove all elements of another set from this set.
    #returns None.
    #set.differnce_update(compare set) --> update the difference to the current set.
    set.difference_update.__doc__

    #discard: Remove an element from a set if it is a member.
    #If the element is not a member, do nothing.
    #return None.
    #set.discard(discard item)
    set.discard.__doc__

    #intersection: Return the intersection of two sets as a new set.
    #(i.e. all elements that are in both sets.)
    #set.intersection(compare set)
    set.intersection.__doc__

    #intersection_update: Update a set with the intersection of itself and another.
    #set.intersection_update(compare set)
    set.intersection_update.__doc__

    #isdisjoint: Return True if two sets have a null intersection.
    #return true or false.
    #set.isdisjoint(compare set)
    set.isdisjoint.__doc__

    #issubset: Report whether another set contains this set.
    #return true or false.
    #set.issubset(compare set)
    set.issubset.__doc__

    #issuperset: Report whether this set contains another set.
    #return true or false
    #set.issuperset(compare set)
    set.issuperset.__doc__

    #pop: Remove and return an arbitrary set element.
    #Raises KeyError if the set is empty.
    #set.pop()
    set.pop.__doc__

    #remove: Remove an element from a set; it must be a member.
    # If the element is not a member, raise a KeyError.
    #return None.
    #set.remove(set member)
    set.remove.__doc__

    #symmetric_difference: Return the symmetric difference of two sets as a new set.
    # (i.e. all elements that are in exactly one of the sets.)
    #set.symmetric_difference(compare set)
    set.symmetric_difference.__doc__

    #symmetric_difference_update: Update a set with the symmetric difference of itself and another.
    #return None
    #set.symmetric_differnce_update(compare set) --> update to set.
    set.symmetric_difference_update.__doc__

    #union: Return the union of sets as a new set.
    # (i.e. all elements that are in either set.)
    #set.union(compare set)
    set.union.__doc__

    #update: Update a set with the union of itself and others.
    #set.update(compare set) --> update the new set from union to set.
    set.update.__doc__
