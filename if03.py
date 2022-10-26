def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a>=b and a>=c):
        if b>=c:
            return b
    if (b>=a and b>=c):
        if c>=a:
            return c
    if (c>=b and c>=a):
        if a>=b:
            return a 

print(main(15 , 15,12))
