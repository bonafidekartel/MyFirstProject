import sys
import requests

print("Hello! My Python development setup is working.")
print(f"Python version: {sys.version.split()[0]}")
print(f"Python location: {sys.executable}")
print(f"Requests version: {requests.__version__}")

