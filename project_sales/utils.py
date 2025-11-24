import numpy as np
import pandas as pd

def generate_random_sales(min_val: int, max_val: int, size: int, seed: int = None) -> np.ndarray:
    """
    Generate a NumPy array of random integer sales between min_val and max_val (inclusive).
    
    Parameters
    ----------
    min_val : int
        Minimum possible sales value.
    max_val : int
        Maximum possible sales value.
    size : int
        Number of values to generate (e.g. 12 months).
    seed : int, optional
        Random seed for reproducibility. If None, no seed is set.
    
    Returns
    -------
    np.ndarray
        Array of random integer sales.
    """
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_val, max_val + 1, size=size)

def create_monthly_sales_dataframe(start_year: int = 2025) -> pd.DataFrame:
    """
    Create a DataFrame of monthly sales for one year (12 months)
    for four products: A, B, C, D.
    
    The ranges are:
      - Product A: 50 - 100
      - Product B: 30 - 80
      - Product C: 20 - 60
      - Product D: 10 - 50
    
    Returns
    -------
    pd.DataFrame
        DataFrame with columns: Date, Product_A, Product_B, Product_C, Product_D.
    """
    # Monthly dates for one year
    dates = pd.date_range(start=f"{start_year}-01-01", periods=12, freq="MS")  # MS = Month Start

    # Generate random sales for each product
    sales_A = generate_random_sales(50, 100, size=12, seed=42)
    sales_B = generate_random_sales(30, 80,  size=12, seed=43)
    sales_C = generate_random_sales(20, 60,  size=12, seed=44)
    sales_D = generate_random_sales(10, 50,  size=12, seed=45)

    df = pd.DataFrame({
        "Date": dates,
        "Product_A": sales_A,
        "Product_B": sales_B,
        "Product_C": sales_C,
        "Product_D": sales_D,
    })
    return df
