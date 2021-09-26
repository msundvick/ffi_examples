def run():
    a = 0
    for i in range(1_000_000):
        a += i % 2 - 0.5
    print(a)
    return "Python"