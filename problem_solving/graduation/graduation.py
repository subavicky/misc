def find_graduation_prob(n):
    a, b, c = 1, 1, 2  # Starting sequence for the number of days
    d, e, f = 1, 0, 1  # Starting sequence for the number of days that ends with 'A'bsent
    for i in range(n - 1):  # Loop n-1 times so that the last number represents the nth tribonacci number
        a, b, c = b, c, a + b + c
        d, e, f = e, f, d + e + f
    output = "{0}, {1}/{0}".format(c, f)
    print(output)


if __name__ == "__main__":
    n = int(input())
    find_graduation_prob(n)