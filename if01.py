def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a>b and a>c):
        return a 
    if (a<b and b>c):
        return b
    if (a<c and b<c):
        return c
print(main(12,13,15))