def read_log_file(file_path):
    """Reads a log file line by line."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line  # Using a generator to process logs efficiently
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error reading file: {e}")