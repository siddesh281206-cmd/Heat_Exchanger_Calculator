def heat_transfer(U, A, deltaT):
    """
    Calculate heat transfer rate
    Q = U * A * deltaT
    """
    Q = U * A * deltaT
    return Q


def main():
    print("Heat Exchanger Calculator")

    U = float(input("Enter heat transfer coefficient (W/m2*K): "))
    A = float(input("Enter heat transfer area (m2): "))
    deltaT = float(input("Enter temperature difference (K): "))

    Q = heat_transfer(U, A, deltaT)

    print("Heat Transfer Rate (Q) =", Q, "Watts")


if __name__ == "__main__":
    main()