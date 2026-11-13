# Computrabajo jobs API: Python examples and CSV export

Search public job listings in **Colombia, Mexico, Peru, Chile and Argentina** through the hosted Computrabajo Actor. This guide focuses on integrating the API, checking collection outcomes, batching searches and exporting existing datasets.

[Open Computrabajo Jobs Scraper on Apify](https://apify.com/datascraperes/computrabajo-jobs-extractor?fpr=edudata)

This repository contains client examples and sample data. It does not contain a standalone scraper. You need an Apify account and token for API calls; starting the hosted Actor can incur charges. Links to Apify include an affiliate referral parameter; we may receive a commission without an additional charge to you.

## What this repository helps you do

- Search one country and an optional exact city per run.
- Request descriptions and optional job insights or company overviews.
- Run separate country searches while keeping their run IDs and outputs distinct.
- Export a saved Dataset to CSV without starting another collection.

## Example result

The [JSON sample](data/sample-output.json) retains every output field from a real three-job result. Descriptions are shortened for this public sample; the [CSV sample](data/sample-output.csv) selects columns useful in spreadsheets. Samples illustrate structure and are not a current vacancies feed.

```json
{
  "id": "B181497240D3438561373E686DCF3405",
  "country": "co",
  "title": "Desarrollador Full Stack Senior Angular / Node.js",
  "company": "Compañía con presencia a nivel nacional",
  "location": "Cúcuta, Norte de Santander",
  "salary": null,
  "url": "https://co.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-full-stack-senior-angular-nodejs-en-cucuta-B181497240D3438561373E686DCF3405"
}
```

This excerpt selects a few fields; use the JSON file for the complete field structure.

## Run without code

1. Open the [hosted Actor](https://apify.com/datascraperes/computrabajo-jobs-extractor?fpr=edudata) and choose **Try for free** or open it in Console.
2. In **Input**, choose a country and enter a job keyword, such as `programador`.
3. Set **Maximum jobs to collect** to 3 for a small first run. City is optional.
4. Click **Start**, then open **Dataset** and the collection summary.
5. Export JSON, CSV or Excel. Review warnings before treating results as complete.

See the [no-code guide](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify currently offers $5 of monthly prepaid usage on its Free plan, with no credit card required. Unused credits expire at the end of the billing cycle; usage is not unlimited. Check [current Apify pricing](https://apify.com/pricing?fpr=edudata) before a large batch.

## Quick start for developers

Install the pinned Python client:

```bash
pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/collect_jobs.py
```

On PowerShell, set `$env:APIFY_API_TOKEN = "your-token"` instead. Never commit your token. Python 3.10+ and Node.js 22+ are supported by these examples. The sample run requests up to three jobs, with a 180-second timeout and USD 0.05 charge cap.

## Input example

The safe submitted example includes all compatible public selectors. Inactive coordinate fields have a separate [alternative input](docs/input-reference.md#coordinate-alternative).

```json
{
  "country": "co",
  "query": "programador",
  "location": "",
  "maxResults": 3,
  "workArrangements": [],
  "postedWithin": "any",
  "sortBy": "relevance",
  "feed": "search",
  "includeDetails": true,
  "includeCompact": false,
  "includeCompanyProfiles": false,
  "categoryIds": [],
  "contractIds": [],
  "salaryIds": [],
  "employmentIds": [],
  "experienceIds": [],
  "maxPages": 10,
  "workplaceTypeIds": [],
  "updatedSinceId": 0
}
```

Full descriptions and defaults are in the [input reference](docs/input-reference.md). Countries are `co`, `mx`, `pe`, `cl`, `ar`; a list of countries is not accepted in a single input.

## Request examples

- [cURL start and read requests](examples/curl-request.md)
- [Python single search](examples/python/collect_jobs.py)
- [Python sequential country workflow](examples/python/batch_job_searches.py)
- [Python existing-Dataset CSV export](examples/python/export_jobs_csv.py)
- [JavaScript single search](examples/javascript/request.mjs)

Python and JavaScript submit one start request and then read the existing run. They do not automatically repeat a start after a timeout, redirect or failed response: inspect Console first because a run may already exist. The Python SDK can retry reads. `SUCCEEDED` is checked separately from `SUMMARY.complete`; partial collections and input corrections are not presented as complete data.

## Output fields

| Field | Meaning |
|---|---|
| `id`, `url` | Job identity and published offer link |
| `title`, `company`, `location`, `country` | Role, employer and country-specific location |
| `salary`, `salaryMin`, `salaryMax` | Published salary information; may be null |
| `description`, `detailStatus` | Requested description and availability |
| `companyProfile`, `companyProfileStatus` | Optional public company overview and availability |

See every field in the [output reference](docs/output-reference.md). Keep missing values null; do not assume salaries share a currency or time period across countries.

## Common use cases

- Compare hiring language across separate country searches.
- Build a role-specific spreadsheet from published job descriptions.
- Import results into an analysis pipeline with explicit collection-status checks.

See [workflow examples](docs/use-cases.md).

## Export Computrabajo jobs to CSV with Python

To export an existing Dataset, pass its ID. This command performs reads and starts no Actor run:

```bash
python examples/python/export_jobs_csv.py YOUR_DATASET_ID --output jobs.csv
```

The script paginates until an empty response and writes UTF-8 CSV. It exports the selected columns, not nested profiles. Reading Dataset contents can itself consume platform usage under your Apify plan.

## Search Colombia and Mexico in separate API runs

```bash
python examples/python/batch_job_searches.py
```

The workflow starts one bounded `ventas` search for Colombia and one for Mexico. Each run has its own charge cap and Dataset. It stops if an earlier collection is incomplete, instead of silently starting further work. Deduplication inside a run does not imply deduplication across separate runs.

## FAQ

See [FAQ](docs/faq.md) for input warnings, empty results, salary values, company coverage and safe retry behavior.

## Limits and pricing

The Actor supports one country per run, at most 1,000 requested unique jobs and up to 1,000 checked pages. These are input limits, not a guarantee of that many matching offers. Details default to enabled; compact insights and company profiles are optional. Company overviews do not include complete review, salary or vacancy catalogues.

The billable event is one unique job saved and verified. Platform use is included in the event price, with no startup event. Current per-event prices and their per-1,000 equivalents are:

| Apify tier | USD per job event | USD per 1,000 events |
|---|---:|---:|
| FREE | 0.001 | 1.00 |
| BRONZE | 0.0009 | 0.90 |
| SILVER | 0.0008 | 0.80 |
| GOLD / PLATINUM / DIAMOND | 0.00075 | 0.75 |

Check the [Actor Pricing tab](https://apify.com/datascraperes/computrabajo-jobs-extractor?fpr=edudata) for current pricing before use. Later Dataset reads/exports follow your platform plan; a charge cap applies to its individual run, not a whole batch of runs.

## Hosted version

The [hosted Computrabajo Actor](https://apify.com/datascraperes/computrabajo-jobs-extractor?fpr=edudata) manages collection and storage. Use its API or Console rather than trying to execute a scraper from this repository.

## Responsible use

Use public job data lawfully and respect source terms and applicable privacy obligations. This is an independent integration guide, not an official Computrabajo product. The MIT license covers the example code and documentation, not third-party job content or trademarks.

## Support

For example-code issues, [open a GitHub issue](https://github.com/datacrawler-edu/computrabajo-jobs-api/issues) with sanitized input and the command. For hosted execution issues, use the [Actor support](https://apify.com/datascraperes/computrabajo-jobs-extractor?fpr=edudata) and include the run ID without tokens or credentials.

## License

Example code and documentation are available under the [MIT License](LICENSE). See [contributing](CONTRIBUTING.md).
