#!/usr/bin/env python3
import sys
import platform

def main():
    print(f"Hello from Python {sys.version}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python executable: {sys.executable}")

if __name__ == "__main__":
    main()
