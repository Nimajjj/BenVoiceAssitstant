from kernel.kernel import Kernel


def main() -> None:
    kernel = Kernel()
    while True:
        kernel.run()


if __name__ == "__main__":
    main()