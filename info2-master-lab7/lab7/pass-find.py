import argparse
from password_check import PasswordInWordsDirFilter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check passwords against a wordlist directory.")
    parser.add_argument(
        "directory",
        type=str,
        help="Required directory containing password database/wordlist files."
    )
    args = parser.parse_args()

    # Example usage of the provided class with the directory argument
    checker = PasswordInWordsDirFilter(args.directory)
    # Add further logic here as needed, for example:
    # checker.check_password("some_password")
