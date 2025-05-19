# alu_regex-data-extraction-Tkcodes-bit

A simple Python script for extracting various patterns from text using regular expressions.
## Features

Extracts the following:
- **Email addresses**
- **URLs** (including `http`, `https`, and `www`)
- **Phone numbers** (e.g., `123-456-7890`, `+1 234-567-8900`)
- **Credit card numbers** (standard 16-digit format)
- **Time** in `HH:MM` (24-hour) format
- **HTML tags** (e.g., `<div>`, `</div>`)
- **Hashtags** (e.g., `#Python3`)
- **Currency amounts** (e.g., `$100.00`, `$1,000.50`)

Includes handling for **edge cases** such as:
- Currency with commas (e.g., `$1,000.50`)
- International phone numbers (e.g., `+1 234-567-8900`)
- Ignoring malformed emails (e.g., `test@@mail..com`)

---

## How to Run

### Requirements

- Python 3.x

### Run the Script

```bash
python3 datamine.p
