import os
path = r"C:\Quick Share\website\speech_project\speech_app\static"
print(os.access(path, os.W_OK))  # Should print True
