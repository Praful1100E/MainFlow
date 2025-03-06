import os
from collections import Counter

OUTPUT_FILE = "output/log_analysis_results.txt"

def analyze_logs(file_path, log_reader, log_parser):
    """Analyzes logs to find frequent IPs, URLs, and response codes."""
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    for line in log_reader(file_path):
        parsed_data = log_parser(line)
        if parsed_data:
            ip, url, status = parsed_data
            ip_counter[ip] += 1
            url_counter[url] += 1
            status_counter[status] += 1

    return ip_counter, url_counter, status_counter

def save_results(ip_counter, url_counter, status_counter):
    """Saves the analysis results to a file."""
    os.makedirs("output", exist_ok=True)  # Create the output folder if it doesn't exist

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\nTop 5 IP Addresses:\n")
        for ip, count in ip_counter.most_common(5):
            f.write(f"{ip}: {count} requests\n")

        f.write("\nTop 5 Requested URLs:\n")
        for url, count in url_counter.most_common(5):
            f.write(f"{url}: {count} requests\n")

        f.write("\nResponse Code Count:\n")
        for status, count in status_counter.items():
            f.write(f"Status {status}: {count} times\n")

    print(f"\nResults saved to {OUTPUT_FILE}")