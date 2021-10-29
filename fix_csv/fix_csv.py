import argparse
import csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--in-delimiter',
                        help="Specifies the delimiter used in the csv file (will be replaced by commas)")
    parser.add_argument('-iq', '--in-quote',
                        help="Specifies the type of quotes used in the csv file (will be escape appropriately)")

    parser.add_argument("original_csv")
    parser.add_argument("output_csv")

    args = parser.parse_args()

    with open(args.original_csv) as input_csv:
        with open(args.output_csv, "w", newline='') as output_csv:
            # Auto detect csv formatting if no delimiter and quote type is given
            if args.in_delimiter is None and args.in_quote is None:
                dialect = csv.Sniffer().sniff(input_csv.read(1024))
                input_csv.seek(0)
                csv_reader = csv.reader(input_csv, dialect)
            else:
                # Use default value for the empty arguments (the basic default of argparse was not enough for this)
                args.in_delimiter = "|" if args.in_delimiter is None else args.in_delimiter
                args.in_quote = '"' if args.in_quote is None else args.in_quote
                csv_reader = csv.reader(input_csv, delimiter=args.in_delimiter, quotechar=args.in_quote)
            # Write to a new file using predefined delimiter and quoting behavior
            csv_writer = csv.writer(output_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                csv_writer.writerow(row)
