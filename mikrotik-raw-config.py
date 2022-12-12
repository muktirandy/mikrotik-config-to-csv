import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Define a command line argument for the input file
parser.add_argument('input_file', help='the input file containing the raw configuration')

# Define a command line argument for the output file
parser.add_argument('output_file', help='the output file to write the structured configuration to')

# Parse the command line arguments
args = parser.parse_args()

# Open the input file for reading
with open(args.input_file, 'r') as input_file:
    # Open the output file for writing
    with open(args.output_file, 'w') as output_file:
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
