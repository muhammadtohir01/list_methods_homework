def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    d=list01.count(0)
    return d
print(main([1, 0, 1, 1, 0, 1, 1]))