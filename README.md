# UOL Login Scraper

A Python web scraper that automates login to UOL accounts. This tool can be run locally or deployed as an AWS Lambda function.

## Features

- Automated web scraping of UOL login page
- Form field detection and submission
- Browser-like headers to avoid detection
- Error handling and logging
- AWS Lambda compatible

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Local Installation

1. **Clone or download the project files**
   ```bash
   # Make sure you have these files:
   # - uol_login_scraper.py
   # - requirements.txt
   # - README.md
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Method 1: Using Properties File (Recommended)

1. **Create configuration file**
   ```bash
   cp config.properties.example config.properties
   ```

2. **Edit config.properties with your credentials**
   ```properties
   # Login credentials
   email=rafaelakio@bol.com.br
   password=your_actual_password
   
   # Optional settings
   timeout=30
   max_retries=3
   debug_mode=false
   ```

3. **Run the script**
   ```bash
   python uol_login_scraper.py
   ```

### Method 2: Interactive Mode (Fallback)
If no config file is found, the script will prompt for credentials:

```bash
python uol_login_scraper.py
```

### Method 3: Programmatic Usage
You can also pass credentials directly in code:

```python
from uol_login_scraper import uol_login_scraper

result = uol_login_scraper("email@domain.com", "password")
print(f"Login result: {result}")
```

## Expected Output

```
Fetching login page...
Form action URL: https://conta.uol.com.br/some-action
Form fields found: ['email', 'password', 'csrf_token']
Submitting login form...
Login appears successful!
Login result: True
```

## Troubleshooting

### Common Issues

1. **Import errors**
   ```
   ModuleNotFoundError: No module named 'requests'
   ```
   **Solution:** Make sure you installed dependencies: `pip install -r requirements.txt`

2. **Network errors**
   ```
   Network error: Connection timeout
   ```
   **Solution:** Check your internet connection and try again

3. **Login failed**
   ```
   Login failed - check credentials
   ```
   **Solution:** Verify your email and password are correct

4. **Form not found**
   ```
   Could not find login form
   ```
   **Solution:** UOL may have changed their page structure. The script may need updates.

### Debug Mode

To see more details about what's happening, you can modify the script to save the HTML response:

```python
# Add this after getting the response
with open('login_page.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```

## Security Notes

- Never commit passwords to version control
- Use environment variables for sensitive data in production
- Be aware of UOL's terms of service and rate limiting
- Consider using official APIs when available

## AWS Lambda Deployment

To deploy as a Lambda function:

1. **Package dependencies**
   ```bash
   pip install -r requirements.txt -t .
   ```

2. **Create deployment package**
   ```bash
   zip -r lambda-deployment.zip .
   ```

3. **Upload to AWS Lambda**
   - Create new Lambda function
   - Upload the zip file
   - Set handler to `uol_login_scraper.lambda_handler`

4. **Test with event**
   ```json
   {
     "email": "rafaelakio@bol.com.br",
     "password": "your-password"
   }
   ```

## Project Structure

```
.
├── uol_login_scraper.py       # Main scraper script
├── requirements.txt           # Python dependencies
├── config.properties.example  # Configuration template
├── config.properties          # Your actual config (create from example)
├── .gitignore                # Git ignore file (protects sensitive data)
└── README.md                 # This documentation
```

## Security Best Practices

- **Never commit `config.properties`** - it's already in `.gitignore`
- Use the example file as a template: `cp config.properties.example config.properties`
- Set appropriate file permissions: `chmod 600 config.properties` (Linux/macOS)
- Consider using environment variables in production environments

## Dependencies

- `requests`: HTTP library for making web requests
- `beautifulsoup4`: HTML parsing library
- `lxml`: XML/HTML parser (faster than default)

## License

This project is for educational and personal use only. Make sure to comply with UOL's terms of service.