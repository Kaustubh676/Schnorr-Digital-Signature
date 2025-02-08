# Schnorr Digital Signature Demonstration

This repository contains a Python implementation and an interactive HTML demo for the **Schnorr Digital Signature Scheme**. The project showcases the generation of cryptographic keys, message signing, and a demonstration of cryptographic vulnerabilities through nonce reuse.

## Project Structure
- **`Schnorr Digital Signature.py`**: A simplified Python implementation of the Schnorr Digital Signature Scheme, demonstrating key generation, message signing, and private key recovery from nonce reuse.
- **`crypto.html`**: An interactive HTML interface for demonstrating the Schnorr Digital Signature process. Users can generate keys, sign messages, and perform a nonce reuse attack to recover private keys.

---

## Features
- **Key Generation:** Generate private and public keys for the Schnorr signature scheme.
- **Message Signing:** Sign two messages using the same nonce to demonstrate a cryptographic vulnerability.
- **Nonce Reuse Attack:** Recover the private key when the same nonce is reused for signing two messages.
- **Interactive Demo:** A user-friendly web interface for visualizing the cryptographic process.

---

## Installation and Usage

### Python Script
1. Ensure you have Python 3.x installed.
2. Run the script using:
   ```bash
   python Schnorr\ Digital\ Signature.py
3. Follow the instructions printed in the terminal.
## Web Demo
1. Open `crypto.html` in any modern web browser.
2. Follow the interactive steps to:
   - Generate keys
   - Sign messages
   - Perform private key recovery

---

## Security Considerations
> ⚠️ **This project is for educational purposes only.**  
It uses simplified cryptographic operations and is not intended for production use. The project demonstrates a critical vulnerability where nonce reuse allows the recovery of private keys.

---

## Demonstrated Concepts
- **Schnorr Digital Signature Scheme**
- **Key generation and message signing**
- **Cryptographic vulnerabilities and attacks**
- **Importance of secure random nonce generation**

---

## License
This project is open-source and available under the [MIT License](LICENSE).
