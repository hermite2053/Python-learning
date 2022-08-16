"""
Let us run
python sequences.py 10

'55' will be displayed.
"""
def triangular_number(n):
    return int(n * (n + 1) / 2)

def square_pyramidal_number(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)

if __name__ == "__main__":
    import sys
    print(triangular_number(int(sys.argv[1])))
