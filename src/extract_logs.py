import sys
import os
import re

def format_log_entry(line):
    """ Convert log format to expected output format. """
    match = re.match(r"^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\.\d{4} - (\w+) - (.*)", line)
    if match:
        date, time, level, message = match.groups()
        return f"{date} {time} {level} {message}\n"
    return None  


def extract_logs(input_file, target_date, output_dir="output"):
    """
    Extracts logs for the given date from a large log file and formats them correctly.
    
    :param input_file: Path to the log file
    :param target_date: Date in YYYY-MM-DD format
    :param output_dir: Directory to store the output file
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    date_pattern = re.compile(rf"^{target_date}T\d{{2}}:\d{{2}}:\d{{2}}\.\d{{4}} - ")

    try:
        with open(input_file, "rt", encoding="utf-8", errors="ignore") as infile, \
             open(output_file, "w", encoding="utf-8") as outfile:
            
            matched_lines = 0
            for line in infile:
                if date_pattern.match(line):
                    formatted_entry = format_log_entry(line)
                    if formatted_entry:
                        outfile.write(formatted_entry)
                        matched_lines += 1

            if matched_lines == 0:
                print(f"No logs found for {target_date}")
            else:
                print(f"Extracted {matched_lines} logs for {target_date} -> {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_logs.py <log_file_path> <YYYY-MM-DD>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    search_date = sys.argv[2]

    extract_logs(log_file_path, search_date)
