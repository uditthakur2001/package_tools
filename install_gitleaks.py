import os
import platform
import urllib.request
import zipfile

def install_gitleaks():
    if platform.system() == "Windows":
        url = "https://github.com/gitleaks/gitleaks/releases/download/v8.18.4/gitleaks_8.18.4_windows_armv6.zip"
        download_path = "gitleaks.zip"
        extract_path = os.path.join(os.getenv('USERPROFILE'), 'bin', 'gitleaks')

        # Create user bin directory if it does not exist
        os.makedirs(extract_path, exist_ok=True)

        print("Downloading Gitleaks...")
        urllib.request.urlretrieve(url, download_path)

        print("Extracting Gitleaks...")
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        print("Gitleaks installed in user bin directory.")
        # Optionally add the directory to PATH
        add_to_path(extract_path)
    else:
        print("Gitleaks installation is supported only on Windows.")
        print("Please install Gitleaks manually from https://github.com/gitleaks/gitleaks")

def add_to_path(directory):
    path = os.environ.get('PATH', '')
    if directory not in path:
        new_path = f"{path};{directory}"
        os.environ['PATH'] = new_path
        print(f"Added {directory} to PATH.")
        # Update the user's PATH environment variable permanently
        with open(os.path.expanduser("~/.bashrc"), "a") as file:
            file.write(f'export PATH="{directory}:$PATH"\n')
        # Notify user to restart their terminal or system
        print("Please restart your terminal or system to apply the PATH changes.")

if __name__ == "__main__":
    install_gitleaks()
