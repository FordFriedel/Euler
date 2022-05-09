#solved
#4/22/22

def factorial(x: int):
    "find the factorial of an integer"
    if x < 1:
        return 0
    product = x
    while x > 1:
        x -= 1
        product *= x
    return product



def lattice_square(x: int):
    "find the number of possible permutations through a lattice square for a given width"
    if x < 1:
        return 0
    permutations = factorial(2* x) / (factorial(2 * x - x) * factorial(x))
    return int(permutations)

if __name__ == "__main__":
    print(lattice_square(1))
    print(lattice_square(2))
    print(lattice_square(3))
    print(lattice_square(4))
    print(lattice_square(20))

