import random
class Utilities():
    def first(iterable, default=None):
        """Return the first element of an iterable; or default."""
        return next(iter(iterable), default)

    def count(seq):
        """Count the number of items in sequence that are interpreted as true."""
        return sum(map(bool, seq))

    def argmin_random_tie(seq, key=lambda x: x):
        """Return a minimum element of seq; break ties at random."""
        items = list(seq)
        random.shuffle(items) #Randomly shuffle a copy of seq.
        return min(items, key=key)

    def flatten(seqs):
        return sum(seqs, [])

    def different_values_constraint(A, a, B, b):
        """A constraint saying two neighboring variables must differ in value."""
        return a != b
