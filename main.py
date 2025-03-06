import log_reader
import log_parser
import log_analyzer

# Path to your log file
log_file_path = "logs/access.log"

# Run the log analysis
ip_counter, url_counter, status_counter = log_analyzer.analyze_logs(
    log_file_path, log_reader.read_log_file, log_parser.parse_log_line
)

# Save results to a file
log_analyzer.save_results(ip_counter, url_counter, status_counter)