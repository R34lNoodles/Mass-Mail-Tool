# Automated Email Sender

This script allows you to send an email with an attachment to multiple recipients using a Gmail account. The recipients and the message content are read from text files.

## Requirements

- Python 3.x
- `smtplib` and `email` libraries (These are part of the standard library)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/automated-email-sender.git
    cd automated-email-sender
    ```

2. **Prepare your files:**

    - `recipients.txt`: A file containing email addresses, one per line.
    - `msg.txt`: A file containing the message you want to send.
    - `attachment.jpg`: The file you want to attach to the email.

## Usage

1. **Run the script:**

    ```bash
    python send_email.py
    ```

2. **Enter your Gmail address and password when prompted.**

    > Note: If you have 2-factor authentication enabled, you may need to use an [App Password](https://support.google.com/accounts/answer/185833?hl=en).

## Note

- Ensure that `recipients.txt`, `msg.txt`, and `attachment.jpg` are in the same directory as the script.
- Modify `filename` if you want to attach a different file.
