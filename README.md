# raZr

## how it works

raZr is a simple command-line tool that provides various functionalities related to file analysis. here's a breakdown of what it does:

1. `hexdump`: this option allows the user to view the hexadecimal dump of a file. it uses the `hexdump` command to display the file content in hexadecimal format.

2. `strings`: this option allows the user to view all the printable characters in a file. it uses the `strings` command to extract and display the printable characters.

3. `SHA256 hash`: this option calculates the SHA256 hash of a file. it uses the `shasum` command to compute the hash.

4. `MD5 hash`: this option calculates the MD5 hash of a file. it uses the `md5` command to compute the hash.

5. `Random MD5/SHA256 value`: this option generates a random MD5 or SHA256 hash. it reads random data from `/dev/urandom`, extracts printable characters, takes the first line, and computes the hash.

6. `extract strings`: this option extracts strings from a file and saves them to a new file. it uses a custom function `getstrings()` to read the file, perform a bitwise XOR operation on each byte with `0x39`, and write the result to a new file. it then reads the new file and returns its content.

**note**: the bitwise XOR operation in the `getstrings()` function is used as a simple form of obfuscation or encryption.

here's how it works: for each byte in the input file, the function performs a bitwise XOR operation with the value `0x39` (which is 57 in decimal). the result is written to the output file.

the XOR operation has a property where A XOR B XOR B = A. this means that if you XOR a value with a key (in this case, `0x39`), and then XOR the result with the same key again, you get back the original value.

in the context of this script, the XOR operation is used to obfuscate the strings in the file. if you were to look at the output file without knowing the key, the strings would appear as gibberish. but if you know the key, you can easily recover the original strings by performing the XOR operation again.

however, it's important to note that this is a very weak form of encryption. anyone who knows that the XOR operation is being used, and knows the key, can easily recover the original strings. furthermore, if the key is hardcoded into the script as it is here, anyone who has access to the script can find the key.

7. `fast analysis`: this option performs a quick analysis of a file. it uses the `getstrings()` function to extract strings from the file, then checks each line for certain keywords related to random tools, LOLBAS (Living Off The Land Binaries and Scripts) tools, and Windows applications. if it finds any of these keywords, it prints a message indicating the line number and the detected tool.

## use-cases
raZr can be used for various purposes related to file analysis and cybersecurity:

1. file inspection: the hexdump and strings view options allow you to inspect the contents of a file at a low level. this can be useful for understanding the structure of unknown file formats or investigating suspicious files.

2. hash calculation: the SHA256 and MD5 hash calculation options can be used to verify the integrity of files. if you download a file and its hash matches the expected value, you can be confident that the file has not been tampered with.

3. random hash generation: the random MD5/SHA256 value option can be used to generate random hashes, which can be useful in various cryptographic applications.

4. string extraction: the `extract strings` option can be used to extract human-readable text from binary files. this can be useful in reverse engineering or malware analysis.

5. file analysis: the `fast analysis` option can be used to quickly check a file for the use of certain tools or commands. this can be useful in cybersecurity for detecting potentially malicious activity.

in summary, this script is a handy tool for anyone who needs to perform low-level file analysis, particularly in the fields of cybersecurity and reverse engineering.

