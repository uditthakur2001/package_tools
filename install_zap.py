import os
import platform
import urllib.request
import zipfile

def install_zap():
    if platform.system() == "Windows":
        url = "https://github.com/zaproxy/zaproxy/releases/download/v2.15.0/ZAP_2_15_0_windows.exe"
        download_path = "zap.zip"
        extract_path = os.path.join(os.getenv('USERPROFILE'), 'bin', 'zap')

        # Create user bin directory if it does not exist
        os.makedirs(extract_path, exist_ok=True)

        print("Downloading OWASP ZAP...")
        urllib.request.urlretrieve(url, download_path)

        print("Extracting OWASP ZAP...")
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        print("OWASP ZAP installed in user bin directory.")
        add_to_path(extract_path)
    else:
        print("OWASP ZAP installation is supported only on Windows.")
        print("Please install OWASP ZAP manually from https://github.com/zaproxy/zaproxy")

def add_to_path(directory):
    path = os.environ.get('PATH', '')
    if directory not in path:
        new_path = f"{path};{directory}"
        os.environ['PATH'] = new_path
        print(f"Added {directory} to PATH.")
        # Notify user to restart their terminal or system
        print("Please restart your terminal or system to apply the PATH changes.")

if __name__ == "__main__":
    install_zap()
