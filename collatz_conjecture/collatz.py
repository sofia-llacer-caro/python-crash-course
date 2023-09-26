def collatz(n):
    """
    Returns the Collatz sequence starting from the given n
    """
    if n < 1:
        raise ValueError("Cannot perform Collatz sequence of non-positive numbers!!")
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in seq:
            # If the next number is already in the sequence, then we are in a cycle and won't reach 1!!
            raise RuntimeError("Oh gee, we broke Collatz conjecture 😱")
        seq.append(n)
    return seq
