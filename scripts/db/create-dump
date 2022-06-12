#!/bin/python

import argparse
from datetime import datetime
import subprocess

OUTPUT_DIR = "dumps"

parser = argparse.ArgumentParser()
parser.add_argument('--container', '-c',
                    help="The name of the docker container.")
parser.add_argument('--user', '-u', help="The database user name")
parser.add_argument('--database', '-d', help="The name of the database.")
args = parser.parse_args()

if not args.container or not args.user or not args.database:
    print("Please provide values for container, user and database. Type --help for more information.")
    exit(1)

file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".sql"
subprocess.call(
    f"docker exec {args.container} pg_dump -U {args.user} --format=c {args.database} > {OUTPUT_DIR}/{file_name}", shell=True)
