import requests
from bs4 import BeautifulSoup
import json
import os
from configparser import ConfigParser

def load_config(config_file='config.properties'):
    """
    Load configuration from properties file
    """
    config = ConfigParser()
    
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found")
    
    # Read the properties file
    config.read(config_file)
    
    # Extract values with defaults
    email = config.get('DEFAULT', 'email', fallback='')
    password = config.get('DEFAULT', 'password', fallback='')
    timeout = config.getint('DEFAULT', 'timeout', fallback=30)
    max_retries = config.getint('DEFAULT', 'max_retries', fallback=3)
    debug_mode = config.getboolean('DEFAULT', 'debug_mode', fallback=False)
    
    if not email or not password or password == 'your_password_here':
        raise ValueError("Please set valid email and password in config.properties")
    
    return {
        'email': email,
        'password': password,
        'timeout': timeout,
        'max_retries': max_retries,
        'debug_mode': debug_mode
    }

def uol_login_scraper(email=None, password=None, config_file='config.properties'):
    """
    Scrapes UOL login page and attempts to login with provided credentials
    If email/password not provided, loads from config file
    """
    # Load from config file if credentials not provided
    if not email or not password:
        try:
            config = load_config(config_file)
            email = config['email']
            password = config['password']
            timeout = config['timeout']
            debug_mode = config['debug_mode']
        except (FileNotFoundError, ValueError) as e:
            print(f"Configuration error: {e}")
            return False
    else:
        timeout = 30
        debug_mode = False
    session = requests.Session()
    
    # Set headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        # Step 1: Get the login page
        print("Fetching login page...")
        login_url = "https://conta.uol.com.br/login"
        response = session.get(login_url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        # Step 2: Parse the HTML to find form fields
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the login form
        login_form = soup.find('form')
        if not login_form:
            print("Could not find login form")
            return False
            
        # Extract form action URL
        form_action = login_form.get('action', '')
        if form_action.startswith('/'):
            form_action = 'https://conta.uol.com.br' + form_action
        elif not form_action.startswith('http'):
            form_action = login_url
            
        print(f"Form action URL: {form_action}")
        
        # Step 3: Prepare form data
        form_data = {}
        
        # Find all input fields in the form
        inputs = login_form.find_all('input')
        for input_field in inputs:
            name = input_field.get('name')
            value = input_field.get('value', '')
            input_type = input_field.get('type', 'text')
            
            if name:
                if input_type == 'email' or 'email' in name.lower() or 'user' in name.lower():
                    form_data[name] = email
                elif input_type == 'password' or 'password' in name.lower() or 'senha' in name.lower():
                    form_data[name] = password
                else:
                    form_data[name] = value
        
        print(f"Form fields found: {list(form_data.keys())}")
        
        # Step 4: Submit the login form
        print("Submitting login form...")
        if debug_mode:
            print(f"Form data: {form_data}")
        login_response = session.post(form_action, data=form_data, headers=headers, allow_redirects=True, timeout=timeout)
        login_response.raise_for_status()
        
        # Step 5: Check if login was successful
        # This depends on UOL's response - you may need to adjust this logic
        if "dashboard" in login_response.url.lower() or "home" in login_response.url.lower():
            print("Login appears successful!")
            return True
        elif "erro" in login_response.text.lower() or "error" in login_response.text.lower():
            print("Login failed - check credentials")
            return False
        else:
            print(f"Login status unclear. Final URL: {login_response.url}")
            print(f"Response status: {login_response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Lambda function wrapper
def lambda_handler(event, context):
    """
    AWS Lambda handler function
    """
    try:
        # Try to get credentials from event first, then from config file
        email = event.get('email', '')
        password = event.get('password', '')
        
        # If not in event, try to load from config file
        if not email or not password:
            try:
                config = load_config()
                email = email or config['email']
                password = password or config['password']
            except Exception as config_error:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': f'Configuration error: {str(config_error)}'})
                }
        
        result = uol_login_scraper(email, password)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'success': result,
                'message': 'Login attempt completed'
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

# For local testing
if __name__ == "__main__":
    try:
        # Try to load from config file first
        print("Loading configuration from config.properties...")
        result = uol_login_scraper()
        print(f"Login result: {result}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Config file error: {e}")
        print("Falling back to manual input...")
        
        # Fallback to manual input
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        result = uol_login_scraper(email, password)
        print(f"Login result: {result}")