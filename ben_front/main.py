from kernel.kernel import Kernel


def main() -> None:
    kernel = Kernel()
    while True:
        kernel.run()
    print("[ CRIT] What the fuck are you doing here?")
    exit(-1)


if __name__ == "__main__":
    main()