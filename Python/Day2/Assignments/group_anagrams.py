from collections import defaultdict
def group_anagrams():
    words = ["abc", "bca", "cab", "foo", "ofo", "bar"]
    # words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Initialize an empty hashmap using list 
    anagram_map = defaultdict(list)

    # result will be stored in an empty array
    res = []

    for w in words:
        '''
        sorted() returns a list, which is mutable and therefore
        cannot be used as a dictionary key. Convert it to a tuple
        because tuples are immutable and hashable. Sorting strings in alphabetically 
        increasing order and converting them into immutable tuple
        '''
        sorted_w = tuple(sorted(w))

        # Use the sorted character tuple as the anagram singature.
        # Words with the same signature belong to the same group.
        anagram_map[sorted_w].append(w)

    # For adding all the values in the map and appending them in the result
    # Iterating over the values in map
    for value in anagram_map.values():
        res.append(value)

    print(res)
    
group_anagrams()