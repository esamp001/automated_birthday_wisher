
# Birthday Greetings Automation

This project automates the process of sending personalized birthday greetings via email. It uses a CSV file to track birthdays and selects a random greeting template to send personalized emails to recipients whose birthdays match the current date.

## Features

- Reads birthday data from a CSV file (`birthdays.csv`).
- Randomly selects a greeting template from three provided text files.
- Personalizes the greeting with the recipient's name.
- Automatically sends the email via an SMTP server on matching dates.

---

## Requirements

This project requires the following libraries and dependencies:

- Python 3.6 or higher
- pandas
- pytz
- smtplib
- email

---

## Installation and Setup

### Step 1: Clone the Repository

Clone the repository or download the source code.

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Install Dependencies

Install the required Python libraries using pip:

```bash
pip install pandas pytz
```

### Step 3: Prepare Necessary Files

Ensure the following files are present in the project directory:

1. **`birthdays.csv`**: A CSV file containing the following columns:
   - `name` (Name of the recipient)
   - `month` (Month of the birthday as an integer, e.g., 1 for January)
   - `day` (Day of the birthday as an integer)

   Example:
   ```csv
   name,month,day
   John,11,26
   Jane,12,5
   ```

2. **Greeting templates**: Three text files (`greetings1.txt`, `greetings2.txt`, `greetings3.txt`) containing customizable greeting templates. Use `[Name]` as a placeholder for personalization.

   Example of a greeting template in `greetings1.txt`:
   ```
   Dear [Name],
   Wishing you a fantastic birthday filled with joy and happiness!
   ```

### Step 4: Configure Email Credentials

Edit the script to include your email credentials. Replace:

- `my_email`: Your email address.
- `my_password`: Your [Google App Password](https://support.google.com/accounts/answer/185833?hl=en).

Ensure **App Passwords** are set up in your Google account if you are using Gmail.

---

## Usage

Run the script using the following command:

```bash
python birthday_greetings.py
```

The script will:

1. Check the current date.
2. Search the `birthdays.csv` file for matching birthdays.
3. Randomly select a greeting template, personalize it with the recipient's name, and send the email.

---

## Notes and Security

- **Environment Variables**: For security, it is recommended to use environment variables or a `.env` file to store email credentials instead of hardcoding them into the script.
- **SMTP Settings**: Ensure your email account is configured to allow SMTP connections.
- **App Password**: Use an app-specific password rather than your main email password for enhanced security.
- **Timezone Configuration**: The script uses `Asia/Manila` timezone. Adjust this as needed for your location.

---

## Troubleshooting

### Common Issues

1. **Authentication Error**:
   - Ensure your email credentials are correct.
   - Check if your Google account allows "Less Secure Apps" or uses App Passwords.

2. **SMTP Connection Error**:
   - Verify the SMTP server (`smtp.gmail.com`) and port (587).
   - Ensure your network allows outgoing SMTP connections.

3. **File Errors**:
   - Ensure `birthdays.csv` and the greeting templates exist and are correctly formatted.

---

## Acknowledgments

This project uses Python's built-in email and datetime modules, as well as the third-party libraries `pandas` and `pytz`.

---
