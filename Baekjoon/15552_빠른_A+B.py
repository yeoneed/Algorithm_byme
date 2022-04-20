import sys
read_ints = lambda: list(map(int, sys.stdin.readline().split()))
read_int = lambda: read_ints()[0]

def main():
    T = read_int()
    for i in range(T):
        a,b = map(int, sys.stdin.readline().strip().split())
        print(f"{a+b}")
        
if __name__ == "__main__":
  main()  