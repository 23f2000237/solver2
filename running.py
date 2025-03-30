import subprocess
def run_script():
    """Install requirements and run script.py, capturing the output."""
    try:
        # Install the requirements
        subprocess.run(["pip", "install", "-r", "/tmp/req2.txt", "--no-cache-dir", "--target", "/tmp"], check=True)

        # Execute the script and capture the output
        result = subprocess.run(
            ["python3","/tmp/script.py"], 
            text=True,
            capture_output=True)

        # Capture stdout or stderr output
        output = result.stdout
        return output

    except Exception as e:
        return f"Error running the script: {str(e)}"
