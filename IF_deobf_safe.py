import base64
import zlib

obfuscated_str = ""

with open('payload.txt','r') as f:
    obfuscated_str = f.read()
    print(obfuscated_str)

def deobfuscate(data):
    # Step 1: Reverse the string
    data = data[::-1]
    # Step 2: Decode from Base64
    decoded = base64.b64decode(data)
    # Step 3: Inflate using zlib
    return zlib.decompress(decoded).decode()

loops = 0

# Main loop that runs about 50 times before producing the final payload
while obfuscated_str.startswith("exec((_)(b'"):
    #hard stop at 100 rounds in case the script runs forever xD
    loops+=1
    if loops >= 500:
        return
    # the deobfuscation routine will produce a string that looks like
    # exec((_)(b'.....'
    # the target of the deobfuscation is the binary string within

    try:
        extracted_str = obfuscated_str[11:-1] #ignores exec((_)(b' and the last '
        # Deobfuscate the string
        obfuscated_str = deobfuscate(extracted_str)
        print("Deobfuscated output:\n", obfuscated_str)
    except Exception as e:
        print(f"Error during deobfuscation: {e}")
        break

print(obfuscated_str)