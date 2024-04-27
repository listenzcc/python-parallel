# %%
import time

# %%

base_iterations = int(1e6)


def compute_pi(buffer, idx_session, idx_pi, idx_start, idx_stop, stop_session=-1, base_iterations=base_iterations, quite=False, **args):
    # Initialize denominator
    k = 1

    # Initialize sum
    s = 0

    # Initialize session
    session = 0

    # Record start time
    buffer[idx_start] = time.time()
    buffer[idx_stop] = time.time()

    while buffer[-1] == 0:
        for i in range(base_iterations):

            # even index elements are positive
            if i % 2 == 0:
                s += 4/k
            else:
                # odd index elements are negative
                s -= 4/k

            # denominator is odd
            k += 2

        if not quite:
            print(session * base_iterations, s)

        # Simulate data interaction between process or thread
        a = [e for e in buffer]
        buffer[-2] += 1

        buffer[idx_session] = session
        buffer[idx_pi] = s
        buffer[idx_stop] = time.time()

        if session == stop_session:
            break

        session += 1

    print('The compute_pi stops')

    return s


# %%
if __name__ == '__main__':
    output_array = [0, 0, 0, 0]
    idx_session = 0
    idx_pi = 1
    idx_start = 2
    idx_stop = 3
    compute_pi(output_array, idx_session, idx_pi, idx_start, idx_stop, 10)
    print(output_array)

# %%
