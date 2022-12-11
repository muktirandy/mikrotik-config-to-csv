import csv
import re

# Read the contents of the 'output.txt' file, split it into lines,
# and remove trailing whitespace from each line.
with open('ip-firewall-structured-config.txt') as fp:
    lines = [line.rstrip() for line in fp]

# Process each line in the input file.
flines = []
for line in lines:
    # Ignore lines that start with a '#' character.
    if line.startswith('#'):
        continue

    # Replace any instances of '= ' with '='.
    line = re.sub(r'=\s+', '=', line)

    # Append the processed line to the 'flines' list.
    flines.append(line)

rules = []
n = 1
quoted_str = ''
for l in flines:
    # Split the line on any whitespace characters.
    l = re.split(r'\s+', l)

    # Process each token in the line.
    tokens = []
    for t in l:
        # If the token contains a double quote character,
        # but does not end with a double quote character,
        # then it is part of a quoted string.
        if '"' in t and not t.endswith('"'):
            # Start a new quoted string.
            quoted_str = t
        elif t.endswith('"'):
            # End the current quoted string.
            quoted_str += t
            tokens.append(quoted_str)
            quoted_str = ''
        elif quoted_str:
            # Continue the current quoted string.
            quoted_str += t + ' '
        elif t.endswith('='):
            # Add the token to the list of tokens.
            tokens.append(t)
        else:
            # Add the token to the list of tokens.
            tokens.append(t)

    # Add the line number, the list of tokens, and the list of
    # extracted tokens to the 'rules' list.
    rules.append([n, l, tokens])

# Extract the different labels from the 'rules' list.
labels = {}
for r in rules:
    for t in r[2]:
        # If the token contains an equal sign, then extract
        # the key and value from the token.
        if '=' in t:
            g = t.split('=')
            labels[g[0]] = 1
# Print all possible labels.
print("Labels -----")
labels = labels.keys()
labels.insert(0, 'rule')
for l in labels:
    print(l)

# Create the 'ip-firewall.csv' file.
with open('ip-firewall.csv', 'wb') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # Write the header row to the file.
    w.writerow(labels)

    # Write each rule to the file.
    for r in rules:
        # Initialize an empty list for the row.
        line = []
        for l in labels:
            line.append('')

        # Set the rule number in the first column.
        line[0] = r[0]

        # Set the key/value pairs in the appropriate columns.
        for t in r[2]:
            if '=' in t:
                g = t.split('=')
                line[labels.index(g[0])] = g[1]

        # Write the row to the file.
        w.writerow(line)
