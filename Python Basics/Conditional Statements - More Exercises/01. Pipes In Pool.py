pool_volume = int(input())
debit_pipe_1 = int(input())
debit_pipe_2 = int(input())
hours = float(input())

liters_pipe_1 = debit_pipe_1 * hours
liters_pipe_2 = debit_pipe_2 * hours
total_liters = liters_pipe_1 + liters_pipe_2
diff = abs(pool_volume - total_liters)

if total_liters > pool_volume:
    print(f"For {hours} hours the pool overflows with {diff:.2f} liters.")
else:
    print(
        f"The pool is {total_liters / pool_volume * 100:.2f}% full. Pipe 1: {liters_pipe_1 / total_liters * 100:.2f}%."
        f" Pipe 2: {liters_pipe_2 / total_liters * 100:.2f}%.")
