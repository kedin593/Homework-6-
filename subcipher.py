"""
--------------------------
Homework 06: Substitution Cipher
--------------------------
STUDENT: Kelsey Edinborough
SEMESTER: Fall 2024
"""
import sys
from string import digits, ascii_letters
from random import sample

ALL_LETTERS_DIGITS = digits + ascii_letters
# use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))

ACTION_ENCRYPT = 'encrypt'
ACTION_DECRYPT = 'decrypt'


def match_normal_with_key(key):
    """
    Matches the provided string, the key, with ALL_LETTERS_DIGITS, which includes digits then ascii letters. 
    The ALL_LETTERS_DIGITS is fist in the mapping

    Examples: 
    >>> match_normal_with_key("P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6")
    {'0': 'P', '1': '4', '2': 'A', '3': '3', '4': '8', '5': 'l', '6': 'm', '7': 'W', '8': 'T', '9': 'w', 'a': 'Q', 'b': 'k', 'c': 'f', 'd': 'Y', 'e': 'i', 'f': '0', 'g': 'Z', 'h': 'E', 'i': 'J', 'j': 'u', 'k': 'F', 'l': 'O', 'm': 'y', 'n': 'L', 'o': 'R', 'p': 'o', 'q': 'r', 'r': 'z', 's': 'X', 't': 'a', 'u': 'd', 'v': '1', 'w': 'B', 'x': 'c', 'y': 'b', 'z': 'G', 'A': 'n', 'B': 'H', 'C': 'V', 'D': '2', 'E': 'x', 'F': 't', 'G': 'g', 'H': 'D', 'I': '5', 'J': '7', 'K': '9', 'L': 'I', 'M': 'h', 'N': 'v', 'O': 'e', 'P': 'q', 'Q': 'C', 'R': 's', 'S': 'N', 'T': 'M', 'U': 'K', 'V': 'p', 'W': 'U', 'X': 'j', 'Y': 'S', 'Z': '6'}
    >>> match_normal_with_key("gSEAOeh6M2UfYQLF4KbukcZ0n3yImDlsaCJq7o519Wwp8TrGNHvxjRtVBzdXPi")
    {'0': 'g', '1': 'S', '2': 'E', '3': 'A', '4': 'O', '5': 'e', '6': 'h', '7': '6', '8': 'M', '9': '2', 'a': 'U', 'b': 'f', 'c': 'Y', 'd': 'Q', 'e': 'L', 'f': 'F', 'g': '4', 'h': 'K', 'i': 'b', 'j': 'u', 'k': 'k', 'l': 'c', 'm': 'Z', 'n': '0', 'o': 'n', 'p': '3', 'q': 'y', 'r': 'I', 's': 'm', 't': 'D', 'u': 'l', 'v': 's', 'w': 'a', 'x': 'C', 'y': 'J', 'z': 'q', 'A': '7', 'B': 'o', 'C': '5', 'D': '1', 'E': '9', 'F': 'W', 'G': 'w', 'H': 'p', 'I': '8', 'J': 'T', 'K': 'r', 'L': 'G', 'M': 'N', 'N': 'H', 'O': 'v', 'P': 'x', 'Q': 'j', 'R': 'R', 'S': 't', 'T': 'V', 'U': 'B', 'V': 'z', 'W': 'd', 'X': 'X', 'Y': 'P', 'Z': 'i'}
    >>> match_normal_with_key("9VoltmqpHC3S2s0LdUOIfFbiAj7xXZgTe8JaNG1DQvcPyruWK4zh6YRkwn5EMB")
    {'0': '9', '1': 'V', '2': 'o', '3': 'l', '4': 't', '5': 'm', '6': 'q', '7': 'p', '8': 'H', '9': 'C', 'a': '3', 'b': 'S', 'c': '2', 'd': 's', 'e': '0', 'f': 'L', 'g': 'd', 'h': 'U', 'i': 'O', 'j': 'I', 'k': 'f', 'l': 'F', 'm': 'b', 'n': 'i', 'o': 'A', 'p': 'j', 'q': '7', 'r': 'x', 's': 'X', 't': 'Z', 'u': 'g', 'v': 'T', 'w': 'e', 'x': '8', 'y': 'J', 'z': 'a', 'A': 'N', 'B': 'G', 'C': '1', 'D': 'D', 'E': 'Q', 'F': 'v', 'G': 'c', 'H': 'P', 'I': 'y', 'J': 'r', 'K': 'u', 'L': 'W', 'M': 'K', 'N': '4', 'O': 'z', 'P': 'h', 'Q': '6', 'R': 'Y', 'S': 'R', 'T': 'k', 'U': 'w', 'V': 'n', 'W': '5', 'X': 'E', 'Y': 'M', 'Z': 'B'}

   Args: 
        key(str): a string containing digits and letters the same length as ALL_LETTERS_DIGITS

    Returns: 
        dict: dictionary that contains all characters from the key linked to a character from ALL_LETTERS_DIGITS

    """
    matching = {}
    for i in range(len(ALL_LETTERS_DIGITS)):
        matching[ALL_LETTERS_DIGITS[i]] = key[i]
    return matching


def match_key_with_normal(key):
    """
    Matches the provided string, the key, with ALL_LETTERS_DIGITS, which includes digits then ascii letters. 
    The ALL_LETTERS_DIGITS is second in the mapping

    Examples: 
    >>> match_key_with_normal("P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6")
    {'P': '0', '4': '1', 'A': '2', '3': '3', '8': '4', 'l': '5', 'm': '6', 'W': '7', 'T': '8', 'w': '9', 'Q': 'a', 'k': 'b', 'f': 'c', 'Y': 'd', 'i': 'e', '0': 'f', 'Z': 'g', 'E': 'h', 'J': 'i', 'u': 'j', 'F': 'k', 'O': 'l', 'y': 'm', 'L': 'n', 'R': 'o', 'o': 'p', 'r': 'q', 'z': 'r', 'X': 's', 'a': 't', 'd': 'u', '1': 'v', 'B': 'w', 'c': 'x', 'b': 'y', 'G': 'z', 'n': 'A', 'H': 'B', 'V': 'C', '2': 'D', 'x': 'E', 't': 'F', 'g': 'G', 'D': 'H', '5': 'I', '7': 'J', '9': 'K', 'I': 'L', 'h': 'M', 'v': 'N', 'e': 'O', 'q': 'P', 'C': 'Q', 's': 'R', 'N': 'S', 'M': 'T', 'K': 'U', 'p': 'V', 'U': 'W', 'j': 'X', 'S': 'Y', '6': 'Z'}
    >>> match_key_with_normal("gSEAOeh6M2UfYQLF4KbukcZ0n3yImDlsaCJq7o519Wwp8TrGNHvxjRtVBzdXPi")
    {'g': '0', 'S': '1', 'E': '2', 'A': '3', 'O': '4', 'e': '5', 'h': '6', '6': '7', 'M': '8', '2': '9', 'U': 'a', 'f': 'b', 'Y': 'c', 'Q': 'd', 'L': 'e', 'F': 'f', '4': 'g', 'K': 'h', 'b': 'i', 'u': 'j', 'k': 'k', 'c': 'l', 'Z': 'm', '0': 'n', 'n': 'o', '3': 'p', 'y': 'q', 'I': 'r', 'm': 's', 'D': 't', 'l': 'u', 's': 'v', 'a': 'w', 'C': 'x', 'J': 'y', 'q': 'z', '7': 'A', 'o': 'B', '5': 'C', '1': 'D', '9': 'E', 'W': 'F', 'w': 'G', 'p': 'H', '8': 'I', 'T': 'J', 'r': 'K', 'G': 'L', 'N': 'M', 'H': 'N', 'v': 'O', 'x': 'P', 'j': 'Q', 'R': 'R', 't': 'S', 'V': 'T', 'B': 'U', 'z': 'V', 'd': 'W', 'X': 'X', 'P': 'Y', 'i': 'Z'}
    >>> match_key_with_normal("9VoltmqpHC3S2s0LdUOIfFbiAj7xXZgTe8JaNG1DQvcPyruWK4zh6YRkwn5EMB")
    {'9': '0', 'V': '1', 'o': '2', 'l': '3', 't': '4', 'm': '5', 'q': '6', 'p': '7', 'H': '8', 'C': '9', '3': 'a', 'S': 'b', '2': 'c', 's': 'd', '0': 'e', 'L': 'f', 'd': 'g', 'U': 'h', 'O': 'i', 'I': 'j', 'f': 'k', 'F': 'l', 'b': 'm', 'i': 'n', 'A': 'o', 'j': 'p', '7': 'q', 'x': 'r', 'X': 's', 'Z': 't', 'g': 'u', 'T': 'v', 'e': 'w', '8': 'x', 'J': 'y', 'a': 'z', 'N': 'A', 'G': 'B', '1': 'C', 'D': 'D', 'Q': 'E', 'v': 'F', 'c': 'G', 'P': 'H', 'y': 'I', 'r': 'J', 'u': 'K', 'W': 'L', 'K': 'M', '4': 'N', 'z': 'O', 'h': 'P', '6': 'Q', 'Y': 'R', 'R': 'S', 'k': 'T', 'w': 'U', 'n': 'V', '5': 'W', 'E': 'X', 'M': 'Y', 'B': 'Z'}

    Args: 
        key(str): a string containing digits and letters the same length as ALL_LETTERS_DIGITS

    Returns: 
        dict: dictionary that contains all characters from the key linked to a character from ALL_LETTERS_DIGITS

    """
    matching = {}
    for i in range(len(key)):
        matching[key[i]] = ALL_LETTERS_DIGITS[i]
    return matching


def encrypt_string(message: str, key=RANDOM_KEY):
    """
    Using the key provided, a new string is created, which is the encrypted string. 
    It first maps the key to ALL_LETTERS_DIGITS using the match_normal_with_key function. 
    Then it replaces the characters in the message with the corresponding character in the key 

    Examples: 
    >>> encrypt_string("Hello, Kelsey")
    'oX55E, WX5iXF'
    >>> encrypt_string("Hello, Kelsey", "P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6") 
    'DiOOR, 9iOXib'
    >>> encrypt_string("Hello, Kelsey. hello", "P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6")
    'DiOOR, 9iOXib. EiOOR'

    Args:
        message(str): the message using letters and digits that is to be encrypted 
        key(str): a string of characters that is used to encrypt the message provided. The default is RANDOM_KEY if no key is provided 

    Return: 
        str: the message encrypted, a string of characters that were replaced by the corresponding character in the key, if there is one. 
    """
    if key == "":
        key = RANDOM_KEY
    new_str = match_normal_with_key(key)
    encrypt_final_message = ""
    for char in message:
        if char in new_str:
            encrypt_final_message += new_str[char]
        else:
            encrypt_final_message += char

    return encrypt_final_message


def decrypt_string(message: str, key=''):
    """
    Takes in an encrypted message and decrypts the message given the key provided. A key must be provided to keep going

    Examples: 
    >>> decrypt_string("DiOOR, 9iOXib. EiOOR","P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6" )
    'Hello, Kelsey. hello'
    >>> decrypt_string("DiOOR, 9iOXib","P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6" )
    'Hello, Kelsey'
    >>> decrypt_string("DiOOR, 9iOXib")
    error


    Args: 
        message(str): encrypted message that is to be decrypted 
        key(str): a string of characters that is was used to encrypt the message that currently requires decrypting. 

    Returns: 
        str: decrypted message using the characters associated with the encryption key 


    """
    if not key or key == "":
        print("error")
        return

    new_str = match_key_with_normal(key)
    decrypt_final_message = ""
    for char in message:
        if char in new_str:
            decrypt_final_message += new_str[char]
        else:
            decrypt_final_message += char
    return decrypt_final_message


def print_encrypted_msg(message, key=RANDOM_KEY):
    """
    Prints out the encrypted message and the key, given a message and a key.
    If no key is provided it defaults to RANDOM_KEY

    Examples: 
    >>> print_encrypted_msg("Hello, Kelsey", "P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6")
    Encrypted= DiOOR, 9iOXib
    Key= P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6
    >>> print_encrypted_msg("Hello, Kelsey")
    Encrypted= oX55E, WX5iXF
    Key= e40wJdhtcl2YTCXObLxN75f9EUHMi8D1VuFrzkZBqapoA3WyQKIjgnm6RsvGPS
    >>> print_encrypted_msg("Hello, Kelsey. hello", "P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6")
    Encrypted= DiOOR, 9iOXib. EiOOR
    Key= P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6

    Args: 
        message(str): a message than is to be encrypted
        key(str): a str of characters the same length as ALL_LETTERS_DIGITS. 

    Returns:
        None: does not a return anything 

    """
    if key == '':
        key = RANDOM_KEY
    done_encrypt = encrypt_string(message, key)

    print("Encrypted=", done_encrypt)
    print("Key=", key)


def print_decrypted_msg(message, key):
    """
    Provided an encrypted message and a key, this function will print out a decrypted message 

    Examples: 
    >>> print_decrypted_msg("DiOOR, 9iOXib","P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6") 
    Decrypted message is:  Hello, Kelsey
    >>> print_decrypted_msg("DiOOR, 9iOXib. EiOOR","P4A38lmWTwQkfYi0ZEJuFOyLRorzXad1BcbGnHV2xtgD579IhveqCsNMKpUjS6" )
    Decrypted message is:  Hello, Kelsey. hello

    Args: 
        message(str): an encrypted message that is to be decrypted 
        key(str):a required string the length of ALL_LETTERS_DIGITS that is used to decrypt the message 

    Returns: 
        none: this function prints out the decrypted message 


    """

    done_decrypt = decrypt_string(message, key)
    print("Decrypted message is: ", done_decrypt)


def main(action: str, msg: str, key=RANDOM_KEY) -> None:
    f"""Main driver of the program based on
    the passed in arguments. Will encrypt or decrypt
    based on the action, message, and key provided.



    Args:
        action (str): Options are {ACTION_ENCRYPT} and {ACTION_DECRYPT}
        msg (str): the message to encrypt or decrypt
        key (str): the key to use for encryption or decryption, if the empty
        string is passed in, a random key will be generated using
        RANDOM_KEY.
    """
    if action == "encrypt":
        print_encrypted_msg(msg, key)

    elif action == "decrypt":
        if key is None or key == "":
            print("Error: A key must be provided for decryption.")
            return
        print_decrypted_msg(msg, key)

    else:
        print("error")


# If you wish to run the program from the command line
# You could do the following
# python3 subcipher.py "Aloha, World"
# that will encrypt this is my message and return both message and key
# you can decrypt by adding -d or --decrypt as the first argument, and then a key after the message
# python3 subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
# reminder, windows replaces python3 with python

# The following allows us to run various features from the command line
# do not modify!
if __name__ == "__main__":
    # sets default values for args
    _action = ACTION_ENCRYPT
    _msg = ''
    _key = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            _action = ACTION_DECRYPT
            remainder = sys.argv[2:]
        else:
            remainder = sys.argv[1:]
        if len(remainder) > 0:
            _msg = remainder[0]
            if len(remainder) > 1:
                _key = remainder[1]

    # calls your main function
    main(_action, _msg, _key)
