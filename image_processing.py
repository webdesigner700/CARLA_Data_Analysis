import os
import subprocess
# Path to the directory containing the LabelImg executable script
directory_to_add = "/Users/vinay/Library/Python/3.7/bin"

# Get the current PATH environment variable
current_path = os.environ.get('PATH', '')

# Append the directory to the PATH if it's not already there
if directory_to_add not in current_path:
    os.environ['PATH'] = f"{directory_to_add}:{current_path}"
    print("Directory added to PATH successfully.")
else:
    print("Directory already exists in PATH.")
    
    
subprocess.run("labelImg")