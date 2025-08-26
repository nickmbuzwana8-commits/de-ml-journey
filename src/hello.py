import pandas as pd

def main():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
    print("Data preview:")
    print(df.head())
    print("\nSummary stats:")
    print(df.describe())

if __name__ == "__main__":
    main()