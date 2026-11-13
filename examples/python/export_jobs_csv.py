"""Export an existing Dataset; this example never starts an Actor run."""
import argparse
import csv
from common import iter_rows

FIELDS = ['id', 'country', 'title', 'company', 'location', 'salary', 'salaryMin', 'salaryMax', 'publishedAt', 'url']

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dataset_id')
    parser.add_argument('--output', default='data/exported-jobs.csv')
    args = parser.parse_args()
    count = 0
    with open(args.output, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for row in iter_rows(args.dataset_id):
            writer.writerow({key:row.get(key) for key in FIELDS})
            count += 1
    print('Exported '+str(count)+' rows to '+args.output)

if __name__ == '__main__':
    main()
