import math

def calculate_statistics(data):
    """
    Calculate mean, median, and standard deviation of numerical data.

    Args:
        data (list): List of numerical data.

    Returns:
        tuple: (mean, median, standard deviation)
    """
    if not data:
        raise ValueError("Input list is empty")

    mean = sum(data) / len(data)

    sorted_data = sorted(data)
    middle_index = len(sorted_data) // 2

    if len(sorted_data) % 2 == 0:
        median = (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
    else:
        median = sorted_data[middle_index]

    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_deviation = math.sqrt(variance)

    return mean, median, std_deviation
