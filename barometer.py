def meas_per_second(gen: int) -> int:
    if gen in (0, 1):
        return 1
    return meas_per_second(gen - 1) + meas_per_second(gen - 2)


print(meas_per_second(int(input())))
