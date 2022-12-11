# Open the input file for reading
with open('ip-firewall-raw.txt', 'r') as input_file:
    # Open the output file for writing
    with open('ip-firewall-structured-config.txt', 'w') as output_file:
        # Create an empty string to store the combined configuration
        combined_config = ''
        # Read each line from the input file
        for line in input_file:
            # Remove the `\` and newline characters from the line
            line = line.strip().replace('\\', '').replace('\n', '')
            # Append the modified line to the combined configuration string
            combined_config += line + ''
        # Split the combined configuration string on the `add action=` string
        config_lines = combined_config.split('add action=')
        # Write each resulting substring to a new line in the output file
        for line in config_lines:
            output_file.write('add action=' + line + '\n')
