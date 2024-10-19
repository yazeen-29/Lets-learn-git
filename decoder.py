import base64

def base64_decode(encoded_str):
    missing_padding = len(encoded_str) % 4
    if missing_padding:
        encoded_str += '=' * (4 - missing_padding)
    
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_link = decoded_bytes.decode('utf-8')
        print(f"Decoded link: {decoded_link}")
    except Exception as e:
        print(f"Error decoding: The base-64 code is incomplete")

try:
    with open('firstPart.txt', 'r') as file:
        encoded_link = file.read().strip()
    base64_decode(encoded_link)
except FileNotFoundError:
    print("Error: firstPart.txt not found.")
except Exception as e:
    print(f"An error occurred: {e}")