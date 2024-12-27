# Find the first 10 prime numbers using a loop and the break statement.

def is_prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

def main():
    
    cnt = 0  
    num = 2
 
    while cnt < 10:
        if is_prime(num):
            print(num)
            cnt += 1
        num += 1

if __name__ == "__main__":
    main()