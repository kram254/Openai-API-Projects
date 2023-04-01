import os
from datetime import datetime, timedelta
from shutil import move

# Path to the Downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
# Path to the to_delete folder
to_delete_path = os.path.join(os.path.expanduser('~'), 'to_delete')

# Get the current date
now = datetime.now()

# Go through all files in Downloads folder
for filename in os.listdir(downloads_path):
    
    # Get the file's path
    file_path = os.path.join(downloads_path, filename)
    
    # Get the file's last modified date
    last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
    
    # Check if the file is older than 30 days
    if now - last_modified_date > timedelta(days=30):
        
        # Move the file to the to_delete folder
        move(file_path, to_delete_path)