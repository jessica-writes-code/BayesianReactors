import pandas as pd


def percent_of_year_operational(row: pd.Series) -> float:
    """Calculate the percent of the year that a reactor was in operation.
    
    Notes:
    - We assume a reactor does not start and end operations in the same year.
    - This calculation does not account precisely for leap years.
    """
    year = row['year']

    # Comparison to start date
    start_date = row['start operation']
    if year < start_date.year:
        return 0.0
    if year == start_date.year:
        return (365 - start_date.dayofyear) / 365.0

    # Comparison to end date
    end_date = row['end operation']
    if year > end_date.year:
        return 0.0
    if year == end_date.year:
        return end_date.dayofyear / 365.0

    return 1.0
