"""Tiny Python project used to demonstrate a Jenkins pipeline."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def is_even(n: int) -> bool:
    """Return True when n is even."""
    return n % 2 == 0


def summarize(values):
    """Return count, sum and average of a list of numbers."""
    values = list(values)
    count = len(values)
    total = sum(values)
    average = total / count if count else 0.0
    return {"count": count, "sum": total, "average": average}


def main():
    print("add(2, 3) =", add(2, 3))
    print("is_even(4) =", is_even(4))
    print("summarize([1, 2, 3, 4]) =", summarize([1, 2, 3, 4]))


if __name__ == "__main__":
    main()