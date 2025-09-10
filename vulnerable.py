import os

def download_file(filename):
    # This function is vulnerable to path traversal
    # if 'filename' contains directory traversal characters like '..'
    base_dir = "/app/downloads/"
    filepath = os.path.join(base_dir, filename)
    
    # In a real application, this would involve reading/serving the file
    # For demonstration, we'll just print the constructed path
    print(f"Attempting to access: {filepath}")

# User-controlled input (simulated)
user_input_filename = "../../../etc/passwd" 
download_file(user_input_filename)

user_input_safe_filename = "report.pdf"
download_file(user_input_safe_filename)
