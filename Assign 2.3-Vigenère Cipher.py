# Programmed by: Rebekah Joy E. Sevial
# Problem 3: Vigenère Cipher

# Implementing keypadding method
def pad_key(message, key):
# Variable to store padded key
    padded_key = ""
# Check the chr if alpha
    i = 0
    for chr in message:
        if chr.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        # Else, ignore and append as empty
        else:
            padded_key += ' '
    # Return padded_key          
    return padded_key        

# Implement encrypt character method
# Check if the message is alpha and is an uppercase letter
        # Define as "a"
            # Define as "A"

# Find the position of the message's char in alphabet
# Find the  position of the key's char in alphabet
# Find the new postion of the message 
        # Return char
    # If not, return message_char

# Implement encrypt method
# Ask the user to input a message and key to encrypt
# Import module
# Format massage and key
# Print the output with color

