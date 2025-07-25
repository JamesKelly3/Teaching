from typing import Dict, List, Tuple

def count_in_list(list_of_things: List[str], x) -> int:
    # return the total number of times x occurs in the list_of_things
    count = 0
    for l in list_of_things:
        if l == x:
            count += 1
    return count

def get_and_remove_from_dict(dict_of_things: Dict[str, str], k) -> Tuple[Dict[str, str], str]:
    # remove key k from the dictionary, and return what was in location k
    val = dict_of_things[k]
    del dict_of_things[k]
    return dict_of_things, val

def remove_smallest_value(list_of_things: List[int]) -> List[int]:
    # find the smallest value in the list, and remove it from the list, then return the new list without changing the order
    smallest = sorted(list_of_things)[0]
    return [l for l in list_of_things if l != smallest]

class Dictionary:
    def __init__(self, pages: List[Dict[str, str]], glossary: Dict[str, int]):
        # A list of pages, where the position in the list is the page number, and the page is a dictionary of words to definitions
        self.pages = pages
        # A dictionary mapping words to the page they are in the dictionary
        self.glossary = glossary

    def lookup_definition(self, word: str) -> str:
        page_no = self.glossary[word]
        page = self.pages[page_no]
        return page[word]