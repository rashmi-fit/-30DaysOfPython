# -  Build a context manager for safe file handling
def safe_file_handling(file_path, mode='r'):
    try:
        file = open(file_path, mode)
        yield file
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close()
