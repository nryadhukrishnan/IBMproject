import hashlib
import pyfiglet
import os
import sys  # Ensure the sys module is imported

# Display banner
ascii_banner = pyfiglet.figlet_format("HASH CRACKER")
print(ascii_banner)

# Display custom message and disclaimer
print("\033[1;33mHi, this is Amegh here. Congratulations and thank you for using this tool!")
print("\033[1;31mWARNING: Ensure you have the 'rockyou.txt' wordlist file in the same directory or specify the correct path.")
print("\033[1;36mDISCLAIMER: This tool is for educational purposes only. Use it responsibly.\033[0m")

# Available algorithms
print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

# Collect input from the user
hash_type = str(input("What's the hash type? ")).upper()
wordlist_location = str(input("Enter wordlist location (press Enter to use 'rockyou.txt' in the current directory): "))

# Default path to rockyou.txt (adjust if necessary)
if not wordlist_location:
    wordlist_location = './wordlists/rockyou.txt'

# Ensure the wordlist file exists
if not os.path.isfile(wordlist_location):
    print(f"\033[1;31mWordlist file not found at {wordlist_location}. Please check the path and try again.\033[0m")
    print("\033[1;33mMake sure 'rockyou.txt' is in the correct directory or provide the correct path.\033[0m")
    print("\nPress Enter to exit.")
    input()  # Pause to let the user see the error message
    sys.exit(1)  # Use a non-zero exit code to indicate an error

hash_value = str(input("Enter hash: "))

try:
    # Open wordlist and split lines
    with open(wordlist_location, 'r', encoding="latin-1") as word_list_file:
        word_list = word_list_file.read().splitlines()

    # Check each word in the wordlist
    for word in word_list:
        if hash_type == "MD5":
            hash_object = hashlib.md5(word.encode('utf-8'))
        elif hash_type == "SHA1":
            hash_object = hashlib.sha1(word.encode('utf-8'))
        elif hash_type == "SHA224":
            hash_object = hashlib.sha224(word.encode('utf-8'))
        elif hash_type == "SHA512":
            hash_object = hashlib.sha512(word.encode('utf-8'))
        elif hash_type == "SHA384":
            hash_object = hashlib.sha384(word.encode('utf-8'))
        else:
            print("\033[1;31mInvalid hash type. Please choose from the given options.\033[0m")
            sys.exit(1)

        # Get the hashed value
        hashed_word = hash_object.hexdigest()

        # Check if the hash matches
        if hash_value == hashed_word:
            print(f"\033[1;32mHASH FOUND: {word}\n\033[0m")
            break
    else:
        print("\033[1;31mHASH NOT FOUND\033[0m")

except FileNotFoundError:
    print("\033[1;31mWordlist file not found. Please check the path and try again.\033[0m")
    print("\033[1;33mMake sure 'rockyou.txt' is in the correct directory or provide the correct path.\033[0m")
    print("\nPress Enter to exit.")
    input()  # Pause to let the user see the error message
    sys.exit(1)
import hashlib
import pyfiglet
import os
import sys  # Ensure the sys module is imported

# Display banner
ascii_banner = pyfiglet.figlet_format("HASH CRACKER")
print(ascii_banner)

# Display custom message and disclaimer
print("\033[1;33mHi, this is Amegh here. Congratulations and thank you for using this tool!")
print("\033[1;31mWARNING: Ensure you have the 'rockyou.txt' wordlist file in the same directory or specify the correct path.")
print("\033[1;36mDISCLAIMER: This tool is for educational purposes only. Use it responsibly.\033[0m")

# Available algorithms
print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA384")

# Collect input from the user
hash_type = str(input("What's the hash type? ")).upper()
wordlist_location = str(input("Enter wordlist location (press Enter to use 'rockyou.txt' in the current directory): "))

# Default path to rockyou.txt (adjust if necessary)
if not wordlist_location:
    wordlist_location = './wordlists/rockyou.txt'

# Ensure the wordlist file exists
if not os.path.isfile(wordlist_location):
    print(f"\033[1;31mWordlist file not found at {wordlist_location}. Please check the path and try again.\033[0m")
    print("\033[1;33mMake sure 'rockyou.txt' is in the correct directory or provide the correct path.\033[0m")
    print("\nPress Enter to exit.")
    input()  # Pause to let the user see the error message
    sys.exit(1)  # Use a non-zero exit code to indicate an error

hash_value = str(input("Enter hash: "))

try:
    # Open wordlist and split lines
    with open(wordlist_location, 'r', encoding="latin-1") as word_list_file:
        word_list = word_list_file.read().splitlines()

    # Check each word in the wordlist
    for word in word_list:
        if hash_type == "MD5":
            hash_object = hashlib.md5(word.encode('utf-8'))
        elif hash_type == "SHA1":
            hash_object = hashlib.sha1(word.encode('utf-8'))
        elif hash_type == "SHA224":
            hash_object = hashlib.sha224(word.encode('utf-8'))
        elif hash_type == "SHA512":
            hash_object = hashlib.sha512(word.encode('utf-8'))
        elif hash_type == "SHA384":
            hash_object = hashlib.sha384(word.encode('utf-8'))
        else:
            print("\033[1;31mInvalid hash type. Please choose from the given options.\033[0m")
            sys.exit(1)

        # Get the hashed value
        hashed_word = hash_object.hexdigest()

        # Check if the hash matches
        if hash_value == hashed_word:
            print(f"\033[1;32mHASH FOUND: {word}\n\033[0m")
            break
    else:
        print("\033[1;31mHASH NOT FOUND\033[0m")

except FileNotFoundError:
    print("\033[1;31mWordlist file not found. Please check the path and try again.\033[0m")
    print("\033[1;33mMake sure 'rockyou.txt' is in the correct directory or provide the correct path.\033[0m")
    print("\nPress Enter to exit.")
    input()  # Pause to let the user see the error message
    sys.exit(1)
