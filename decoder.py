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
        encoded_firstPart_link = file.read().strip()
    with open('secondPart.txt','r') as file:
        encoded_secondPart_link=file.read().strip()
    encoded_link=encoded_firstPart_link+encoded_secondPart_link
    base64_decode(encoded_link)
except FileNotFoundError:
    print("Hmm, It seems that the file we are searching for is not here, did you actually merged both branches ?")
except Exception as e:
    print(f"An error occurred: {e}")