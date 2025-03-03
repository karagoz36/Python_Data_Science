import sys
import time
import os


def ft_tqdm(iterable):
    """
    Custom progress bar similar to tqdm.
    """

    total = len(iterable)
    start_time = time.time()

    for index, item in enumerate(iterable, 1):
        # Progress percentage
        progress = index / total
        bar_len = os.get_terminal_size().columns - 40
        filled_len = int(progress * bar_len)

        # Create progress bar string
        bar = '█' * filled_len + '-' * (bar_len - filled_len)
        elapsed_time = time.time() - start_time

        # Format elapsed time as `mm:ss`
        formatted_time = time.strftime("%M:%S", time.gmtime(elapsed_time))

        # Estimate remaining time (ETA)
        eta = elapsed_time / progress - elapsed_time if progress > 0 else 0
        formatted_eta = time.strftime("%M:%S", time.gmtime(eta))

        # Compute speed (iterations per second)
        speed = index / elapsed_time if elapsed_time > 0 else 0

        # Print progress bar with tqdm-like format
        sys.stdout.write(f"\r{int(progress*100)}%|{bar}| {index}/{total} "
                         f"[{formatted_time}<{formatted_eta}, "
                         f"{speed:.2f}it/s]")
        sys.stdout.flush()

        # Generator: keeps iteration going on
        yield item

    print()
