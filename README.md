# IP Firewall Config Parser

This script processes a structured config file for an IP firewall and outputs a CSV file with the extracted key/value pairs.

## Requirements

- Python 2.7 or higher
- The `csv`,`re` and `sys` modules

## Usage

To run the script, use the following command:

```
python ip-firewall-config-parser.py <input_file> <output_file>
```

This will process the file `ip-firewall-structured-config.txt` and create the file `ip-firewall.csv` with the extracted key/value pairs.

## Configuration

The script can be configured by modifying the following variables in the code:

- `INPUT_FILE`: The name of the input file containing the structured config data.
- `OUTPUT_FILE`: The name of the output CSV file.

## Limitations

- The script assumes that the input file is structured in a specific way and may not work with arbitrary config files. You may need to use mikrotik-raw-config.py first before using 
ip-firewall-config-parser.py
- The script does not handle quoted strings that span multiple lines.
- The script does not handle lines that start with '#' as comments, it only ignores lines that start with '#' and are empty.
