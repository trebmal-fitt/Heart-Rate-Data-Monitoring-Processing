"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, max, and standard deviation
    """ 
    data = []

    # open file using file I/O and read it into the `data` list
    try:    
        with open(filename, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

        return 0.0, 0.0, 0.0

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    clean_data = filter_nondigits(data)

    if not clean_data:
        print(f"Error: No valid data found in '{filename}'.")

        return 0.0, 0.0, 0.0

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    plt.figure(figsize=(10, 5))
    plt.plot(clean_data, marker='o', linestyle='-')
    plt.title("Heart Rate Over Time")
    plt.xlabel("Time (samples)")
    plt.ylabel("Heart Rate (BPM)")
    plt.grid(True)
    plt.savefig(f"images/{filename.split('/')[-1].replace('.txt', '.png')}")
    plt.close()

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(clean_data)
    max_hr = maximum(clean_data)
    std_dev_hr = (standard_deviation(clean_data))

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr

    # print data from each phase for avg_hr, max_hr, and std_dev_hr
if __name__ == "__main__":
    print(run("data/phase0.txt"))
    print(run("data/phase1.txt"))
    print(run("data/phase2.txt"))
    print(run("data/phase3.txt"))
