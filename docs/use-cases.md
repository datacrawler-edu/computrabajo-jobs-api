# Integration workflows

## Role spreadsheet

Run `examples/python/collect_jobs.py` with the bounded sample, then export the resulting Dataset ID with `examples/python/export_jobs_csv.py`. Exporting an existing Dataset starts no new collection.

## Country comparison

`examples/python/batch_job_searches.py` submits separate Colombia and Mexico searches with the same keyword. Each run is separately billed and has its own charge cap. Change one country at a time; do not pass an unsupported list to the Actor.

## Repeated snapshots

Save IDs and timestamps from different runs for your own comparisons. A repeated run can charge for its own results again. This repository does not promise cross-run change detection or deduplication. Review SUMMARY on every run and retain partial-result context.
