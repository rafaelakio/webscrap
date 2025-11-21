#!/usr/bin/env python3
"""
Simple test to verify Python is working and config loading works
"""

import os
from configparser import ConfigParser

def test_config_loading():
    """Test if we can load the configuration file"""
    try:
        config = ConfigParser()
        
        if not os.path.exists('config.properties'):
            print("❌ config.properties file not found")
            return False
        
        config.read('config.properties')
        
        email = config.get('DEFAULT', 'email', fallback='')
        password = config.get('DEFAULT', 'password', fallback='')
        
        print("✅ Configuration file loaded successfully!")
        print(f"📧 Email: {email}")
        print(f"🔒 Password: {'*' * len(password) if password else 'NOT SET'}")
        
        if password == 'your_password_here':
            print("⚠️  Please update your password in config.properties")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing UOL Login Scraper Configuration...")
    print("=" * 50)
    
    success = test_config_loading()
    
    if success:
        print("\n✅ All tests passed! Ready to install dependencies and run the scraper.")
        print("\nNext steps:")
        print("1. Install Python if not already installed")
        print("2. Run: python -m pip install -r requirements.txt")
        print("3. Run: python uol_login_scraper.py")
    else:
        print("\n❌ Please fix the configuration issues above.")