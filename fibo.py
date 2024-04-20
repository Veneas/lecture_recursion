def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)
def main():
    n = int(input("Enter the number of Fibonacci sequence elements you want to calculate: "))
    fibonacci_sequence = [recursive_nth_fibo(i) for i in range(n)]
    print("Fibonacci sequence with", n, "elements:", fibonacci_sequence)


if __name__ == "__main__":
    main()
