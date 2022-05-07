def odd_generator():
    starting, add_up = 1, 2
    while True:
        yield starting
        starting = starting + add_up


def pi_series():
    odds = odd_generator()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(100000):
    print(next(approx_pi))
