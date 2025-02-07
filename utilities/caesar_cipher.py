#------------------------------------------------------------------------------
# caesar_cipher.py
#
# This module provides utility functions for generating random strings, 
# encrypting/decrypting text using Caesar's cipher, and performing frequency 
# analysis for decryption.
#
# Functions included:
# - generate_random_string(length, letters): Generates a random string of 
#   lowercase letters or bits.
# - cesars_cipher_encryption(text, shift_amount): Encrypts or decrypts text 
#   using Caesar's cipher.
# - frequency_attack(ciphertext, top_letter): Performs frequency analysis to 
#   decrypt a given ciphertext.
#
# These utilities are useful for cryptographic experiments, classical 
# cryptanalysis, and generating test data.
#
# © Leonardo Lavagna 2025
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------


import string
import random

def generate_random_string(length, letters=None):
    """
    Generates a random string of lowercase letters.

    Args:
        length (int): The desired length of the random string.
        letters (list[str]): A desired list of letters. Default is None.

    Returns:
        str: A random string of lowercase letters (or bits) with the specified length.
    Raises:
        NotImplementedError if letters is not None or letters is not ['0','1'].
    """
    if letters is None:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
    elif letters == ['0', '1']:
        return ''.join(random.choice(letters) for _ in range(length))
    else:
        raise NotImplementedError

def caesars_cipher_encryption(text, shift_amount):
    """
    Encrypts or decrypts a text using a Caesar's cipher based on the shift_right function.

    Args:
        text: The text to be encrypted or decrypted.
        shift_amount: The number of positions to shift each character.

    Returns:
        The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char_ord = (ord(char) - start + shift_amount) % 26 + start
            result += chr(shifted_char_ord)
        else:
            result += char
    return result

def frequency_attack(ciphertext, top_letter="e"):
    """
    Performs frequency analysis on a given ciphertext and attempts to decrypt it using letter frequency.

    Args:
        ciphertext (str): The encrypted text to analyze and decrypt.
        top_letter (str, optional): The letter assumed to be the most frequent in the plaintext.
                                    Defaults to 'e', which is the most common letter in English.

    Returns:
        str: The decrypted plaintext obtained by shifting the characters of the ciphertext.
    """
    letter_frequencies = {}
    for letter in ciphertext:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_frequencies:
                letter_frequencies[letter] += 1
            else:
                letter_frequencies[letter] = 1
    most_frequent_letter = max(letter_frequencies, key=letter_frequencies.get)
    shift_amount = ord(most_frequent_letter) - ord(top_letter)
    plaintext = ""
    for letter in ciphertext:
        if letter.isalpha():
            start = ord('a') if letter.islower() else ord('A')
            shifted_letter_ord = (ord(letter) - start - shift_amount) % 26 + start
            plaintext += chr(shifted_letter_ord)
        else:
            plaintext += letter
    return plaintext
