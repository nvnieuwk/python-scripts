import argparse
import csv
import os
import re

def get_summaries(files: list) -> list:
    summaries = []
    for file in files:
        if file.endswith("summary.txt") and "mosdepth" not in file:
            summaries.append(file)
    return summaries

if __name__ == "__main__":
    # Setting up argparser
    parser = argparse.ArgumentParser(description="Concatenate all RTG VCFeval summary files")
    parser.add_argument('input', metavar='FOLDER', type=str, help="The folder containing all input files")
    parser.add_argument('output', metavar='FILE', type=str, help="The output CSV file")

    args = parser.parse_args()

    input = args.input
    output_file = args.output

    header = ["samplename", "threshold", "true_positives_baseline", "true_positives_called", "false_positives", "false_negatives", "precision", "sensitivity", "f-measure"]
    output = open(output_file, "w")
    writer = csv.writer(output)
    writer.writerow(header)

    for subdir, dirs, files in os.walk(input):
        summaries = get_summaries(files)
        if len(summaries) == 0: continue

        for summary in summaries:
            sample_name = re.search('^([^\.]+)\..*$', summary).group(1)
            with open(f'{subdir}/{summary}',"r") as file:
                data_rows = file.read().split("\n")[2:4]
                for row in data_rows:
                    parsed_row = re.split('\s+',row)
                    parsed_row[0] = sample_name
                    writer.writerow(parsed_row)

    output.close()