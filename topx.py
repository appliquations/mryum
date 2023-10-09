import argparse
import time


def topX(file_path, x):
    largest_numbers = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                num = int(line.strip())
                # if we haven't reached the number of largest numbers we want to output
                # add it to the list
                if len(largest_numbers) < x:
                    largest_numbers.append(num)
                # if the current number is larger than the smallest in the list
                # add it to the list
                # we're not going to remove duplicates as this didn't seem to be a requirement
                elif num > min(largest_numbers):
                    largest_numbers.remove(min(largest_numbers))
                    largest_numbers.append(num)
    except OSError:
        print("Error opening file")
        exit(1)

    # sort in descending before returning
    largest_numbers.sort(reverse=True)
    return largest_numbers


if __name__ == "__main__":
    start_time = time.time()

    # parse script args
    parser = argparse.ArgumentParser(
        description="Find the largest 'x' amount of numbers in a text file containing only numbers."
    )
    parser.add_argument("file_path", help="Path to the input file")
    parser.add_argument("x", type=int, help="Number of largest numbers to output")
    parser.add_argument(
        "--debug", type=bool, help="Enable debug outputs", default=False, required=False
    )

    args = parser.parse_args()

    largest_numbers = topX(args.file_path, args.x)
    print(f"The largest {args.x} numbers in {args.file_path} are: {largest_numbers}")

    # print timing if debug = true
    if args.debug:
        print(f"Execution time: {time.time() - start_time:.2f} seconds")
