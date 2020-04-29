#!/usr/bin/env python3

import argparse
import datetime
import os
import yaml

# Location to store output file in
ENV_FILE = 'generated.env'

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Generate the environment')
    parser.add_argument('type', choices=['default', 'sip'])
    parser.add_argument('--overrides')
    args = parser.parse_args()

    # Load variables
    with open('variables.yml') as var_file:
        variables = yaml.safe_load(var_file)

    # Load overrides
    overrides = dict()
    if args.overrides:
        with open(args.overrides) as override_file:
            overrides = yaml.safe_load(override_file)

    # Write .env file
    with open(ENV_FILE, 'w') as env_file:
        env_file.write('# Autogenerated on {}\n\n'.format(datetime.datetime.now()))
        
        sip, default = 0, 1
        for key in variables.keys():
            if key in overrides.keys():
                # Override has highest precedence
                value = overrides[key]
            elif args.type == 'sip' and variables[key][sip]:
                # Try to use SIP env var but fall back to default if unavailable
                value = os.environ.get(variables[key][sip], variables[key][default])
            else:
                # Use default value
                value = variables[key][default]

            # Convert to string
            if isinstance(value, list):
                value = ",".join([str(item) for item in value])
            else:
                value = str(value) if value else "" 
                
            env_file.write("{}={}\n".format(key, value))
