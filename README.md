# HyperView

HyperView is a Python-based program designed to protect sensitive information on Windows systems through advanced data encryption and security measures. It leverages the `cryptography` library to provide robust encryption capabilities for files and directories.

## Features

- **File Encryption**: Encrypt individual files to secure sensitive information.
- **File Decryption**: Decrypt previously encrypted files.
- **Directory Encryption**: Encrypt all files within a specified directory.
- **Directory Decryption**: Decrypt all files within a specified directory.

## Installation

To run HyperView, you need to have Python installed on your system along with the `cryptography` library. You can install the required library using pip:

```bash
pip install cryptography
```

## Usage

1. Clone the repository or download the `hyperview.py` file.
2. Open a terminal or command prompt and navigate to the directory containing `hyperview.py`.
3. Run the program using Python:

```bash
python hyperview.py
```

4. Use the available methods to encrypt or decrypt files and directories. For example:

```python
hv = HyperView()
hv.encrypt_file('sensitive_data.txt')
hv.decrypt_file('sensitive_data.txt')
hv.encrypt_directory('sensitive_folder')
hv.decrypt_directory('sensitive_folder')
```

## Important Note

- Ensure you keep the `hyperview.key` file secure, as it is necessary for decrypting your files. Losing this key means you will not be able to decrypt your encrypted data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.