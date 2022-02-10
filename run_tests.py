import time
from solver import get_pattern_from_guess

if __name__ == '__main__':
    start = time.time()
    with open("tests/pattern_test_cases.csv", "r") as csvfile:
        for i, line in enumerate(csvfile):
            guess, hidden_word, expected_pattern = line.strip().split(",")
            pattern = get_pattern_from_guess(guess, hidden_word)

            if pattern != expected_pattern:
                raise AssertionError(
                    f"Test case #{i+1} failed: guessing '{guess}' "
                    f"against '{hidden_word}' yielded '{pattern}' "
                    f"instead of expected '{expected_pattern}'"
                )
    end = time.time()
    print(f"All test cases passed. Time elapsed: {round(end-start, 3)} seconds")