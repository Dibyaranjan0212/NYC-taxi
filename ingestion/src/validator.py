from pathlib import Path

def file_exists(file_path:str) -> bool:
    """Check if a file exists at the given path."""
    return Path(file_path).is_file()

def file_not_empty(file_path:str) -> bool:
    """Check if a file is not empty."""
    return Path(file_path).stat().st_size > 0


