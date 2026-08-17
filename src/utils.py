"""
Utils.py

File used for utility functions in the project.

"""


def summary_df(df):
    """
    Prints a summary of the DataFrame including its shape, data types, and missing values.

    Parameters:
    df (pd.DataFrame): The DataFrame to summarize.
    """

    for col in df.columns:
        print(f"Column: {col}")
        print(f"  Data Type: {df[col].dtype}")
        print(f"  Missing Values: {df[col].isnull().sum()}")

