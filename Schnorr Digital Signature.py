import random

# Simplified Schnorr Signature Implementation for Demonstration
def generate_keys(p, q, g):
    """Generate Schnorr keys."""
    private_key = random.randint(1, q - 1)
    public_key = pow(g, private_key, p)
    return {"private": private_key, "public": public_key, "p": p, "q": q, "g": g}

def sign_message(message, keys, k=None):
    """Sign a message using Schnorr signature scheme."""
    p, q, g = keys["p"], keys["q"], keys["g"]
    private_key = keys["private"]
    if k is None:
        k = random.randint(1, q - 1)  # Generate a random nonce
    r = pow(g, k, p)
    e = hash_message(message + str(r)) % q  # Simplified hash function
    s = (k + private_key * e) % q
    return (r, s, e, k)  # Return the nonce k for demonstration purposes

def hash_message(message):
    """Simplified hash function for demonstration purposes."""
    return int.from_bytes(message.encode(), "big")

def recover_private_key(signature1, signature2, q):
    """Recover private key using reused nonce."""
    r1, s1, e1, _ = signature1
    r2, s2, e2, _ = signature2
    if r1 != r2:
        raise ValueError("Nonces are not reused; attack not applicable.")
    # Calculate private key using nonce reuse equations
    numerator = (s1 - s2) % q
    denominator = (e1 - e2) % q
    private_key = (numerator * pow(denominator, -1, q)) % q
    return private_key

# Main Execution
if __name__ == "__main__":
    # Schnorr Parameters
    p = 23  # Small prime modulus for demonstration
    q = 11  # Order of g
    g = 2   # Generator

    # Key Generation
    keys = generate_keys(p, q, g)
    print("Private Key:", keys["private"])
    print("Public Key:", keys["public"])

    # Sign two messages with the same nonce
    message1 = "Message 1"
    message2 = "Message 2"
    reused_k = random.randint(1, q - 1)  # Deliberately reuse the same nonce

    signature1 = sign_message(message1, keys, reused_k)
    signature2 = sign_message(message2, keys, reused_k)

    print("\nSignatures with Nonce Reuse:")
    print("Signature 1 (r, s, e):", signature1[:-1])  # Exclude k from output
    print("Signature 2 (r, s, e):", signature2[:-1])  # Exclude k from output

    # Attempt to recover the private key
    recovered_key = recover_private_key(signature1, signature2, q)
    print("\nRecovered Private Key:", recovered_key)

    # Verify attack success
    if recovered_key == keys["private"]:
        print("Attack Successful: Private Key Recovered!")
    else:
        print("Attack Failed: Keys do not match.")
