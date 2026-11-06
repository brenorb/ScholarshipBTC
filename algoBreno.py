def find_range(utxos, x):
    """Find the least-change range in a timestamp-ordered sequence of UTXOs."""
    smallest = float("inf")
    result = []

    for end in reversed(range(len(utxos))):
        total = 0
        start = end
        while total < x and start >= 0:
            total += utxos[start].amount
            if total >= x and total - x < smallest:
                smallest = total - x
                result = sorted((utxos[start].timestamp, utxos[end].timestamp))
                if smallest == 0:
                    return result
            start -= 1
    return result
