def mean(xs):
    """Return the arithmetic mean of a non-empty list."""
    if not xs:
        raise ValueError("empty list")
    return sum(xs) / len(xs)