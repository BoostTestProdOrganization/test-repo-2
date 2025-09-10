"""
Test file to demonstrate Semgrep security rule detection
This contains intentional security anti-patterns for testing purposes
"""

import hashlib
import os
import sqlite3
import subprocess

# This will trigger Semgrep's hardcoded-credential rules
API_KEY = "sk-1234567890abcdef1234567890abcdef"
DATABASE_PASSWORD = "admin123"
SECRET_TOKEN = "super_secret_token_12345"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def connect_to_api():
    """Function that uses hardcoded API key - triggers Semgrep warning"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    return headers

def get_database_connection():
    """Function with hardcoded password - triggers Semgrep warning"""
    connection_string = f"postgresql://user:{DATABASE_PASSWORD}@localhost:5432/mydb"
    return connection_string

def generate_jwt():
    """Function using hardcoded secret - triggers Semgrep warning"""
    import jwt
    payload = {"user_id": 123, "role": "admin"}
    token = jwt.encode(payload, SECRET_TOKEN, algorithm="HS256")
    return token

def weak_hash_example(data):
    """Function using weak hashing algorithm - may trigger Semgrep warning"""
    return hashlib.md5(data.encode()).hexdigest()

def sql_injection_example(user_id):
    """Function with SQL injection vulnerability - triggers Semgrep warning"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Dangerous: Direct string interpolation in SQL query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

def command_injection_example(filename):
    """Function with command injection vulnerability - triggers Semgrep warning"""
    # Dangerous: Direct user input in shell command
    result = subprocess.run(f"cat {filename}", shell=True, capture_output=True)
    return result.stdout

def insecure_random_example():
    """Function using insecure random - may trigger Semgrep warning"""
    import random
    # Insecure for cryptographic purposes
    return random.randint(1000, 9999)

if __name__ == "__main__":
    print("This is a test file for Semgrep security scanning")
    print(f"API Key starts with: {API_KEY[:10]}...")
    print(f"Database connection: {get_database_connection()}")
    print(f"Weak hash: {weak_hash_example('test')}")
    print(f"Random token: {insecure_random_example()}")
