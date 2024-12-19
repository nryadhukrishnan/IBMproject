Hashed Password Cracker 

This project is part of an IBM cybersecurity project that focuses on cracking hashed passwords using Python. It offers a command-line interface (CLI) and a graphical user interface (GUI) for ease of use. This tool helps to understand the time taken to crack passwords and provides feedback on password strength to encourage stronger passwords.

Features
1.Supports multiple hashing algorithms like MD5, SHA-1, SHA-256.
2.show the time taken to crack the password, allowing users to understand the password's strength.
3. Provides feedback with remarks on password strength. If the password is weak, suggestions for creating a strong password will be provided.
4.Command-line interface (CLI) and graphical user interface (GUI).
5.Dictionary-based attack using custom wordlists.

Requirements
Make sure you have the following installed:

Python 3.x
Required Python packages (listed in requirements.txt)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/nryadhukrishnan/Hashedpasswordcracker.git
cd Hashedpasswordcracker
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Command-Line Interface (CLI)
To run the password cracker using the command-line interface:

bash
Copy code
python hashcrack.py
Graphical User Interface (GUI)
To run the password cracker using the GUI:

bash
Copy code
python advanced_hash_cracker_gui.py
Wordlist Size and Download
Note: Due to GitHub's size limitations, the full rockyou.txt wordlist (14 million passwords) cannot be included in this repository. You can download the full wordlist here:

Download full rockyou.txt
If you need to reduce the size of the wordlist, consider limiting the passwords to certain lengths or truncating the file.

Example Usage
Select Hash Algorithm: Choose the hashing algorithm from the available options (e.g., MD5, SHA-1, etc.).
Upload Hashed Password: Provide the hashed password that needs to be cracked.
Load Wordlist: Load a custom wordlist or dictionary file (e.g., rockyou.txt).
Crack the Password: The tool will attempt to match the hash with the words in the dictionary to find the original password.
View Results:
Time Taken: The time it took to crack the password will be displayed.
Password Strength: Feedback on whether the password is weak, medium, or strong. Suggestions will be provided for creating stronger passwords if needed.
Ethical Use Disclaimer
This tool is intended for ethical purposes only. It is designed for educational and cybersecurity testing within legal and ethical guidelines. The misuse of this tool for illegal or unethical activities is strictly prohibited.

Disclaimer: Use this tool responsibly and only with explicit permission.

Contributing
If you wish to contribute to the project, feel free to submit a pull request or open an issue. Contributions are always welcome!

License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

IBM Project
This project is a part of an IBM Inovaction centre for education to understand the mechanisms behind password security and to educate individuals and organizations on best practices in cybersecurity. The tool helps simulate real-world scenarios for ethical hacking and password recovery.

Contact
For any queries or support, contact:
18961@yenepoya.edu.in
