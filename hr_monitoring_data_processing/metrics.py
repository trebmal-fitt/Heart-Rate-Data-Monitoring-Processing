def average(data: list[int]) -> float:
    """
    Calculate average value (mean) of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list, rounded to 2 decimal places
    """
    if not data:
        return [] # return empty list if no data is provided
    
    total = 0
    for value in data:
        total += value

    return round(total / len(data), 2)

def maximum(data: list) -> float:
    """
    Find the maximum value in a list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.

    Returns:
        float: The highest integer value in the list. Returns an empty list if input is empty.
    """
    if not data:
        return [] # return empty list if no data is provided
    
    max_value = data[0]
    for num in data:
        if num > max_value:
            max_value = num

    return float(max_value)
    
def variance(data: list) -> float:
    """
    Calculate the population variance of a list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.

    Returns:
        float: The variance value rounded to 2 decimal places, or an empty list if input is empty.
    """
    if not data:
        return [] # return empty list if no data is provided
    
    mean = average(data)
    squared_diffs = [(num - mean) ** 2 for num in data]

    return round(sum(squared_diffs) / len(data), 2)

def standard_deviation(data: list) -> float:
    """
    Calculate the population standard deviation of a list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.

    Returns:
        float: The standard deviation rounded to 2 decimal places, or an empty list if input is empty.
    """
    if not data:
        return [] # return empty list if no data is provided
    
    return round(variance(data) ** 0.5, 2)
    
