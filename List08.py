def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i=0
    while i<len(fruits):
         x=fruits.pop("apple")
         i+=1
         print(x)
print(main(["apple", "banana", "apple", "pear", "apple"]))