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
    
    mean = 0
    for value in data:
        mean += value

    return round(mean / len(data), 2)

def maximum(data: list) -> float:
    """
    Find the maximum value in a list of integers.

    Args:
        data (list[int]): A list of integers representing heart rate samples.

    Returns:
        float: The highest integer value in the list as a float. Returns an empty list if input is empty.
    """
    if not data:
        return [] # return empty list if no data is provided
    
    maximum = data[0]
    for num in data:
        if num > maximum:
            maximum = num

    return (maximum)
    
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
    variance = [(num - mean) ** 2 for num in data]

    return round(sum(variance) / len(data), 2)

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
    
