import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()
