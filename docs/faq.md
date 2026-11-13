# FAQ

## Is this a standalone Computrabajo scraper?

No. These are clients for the hosted Apify Actor. No Computrabajo account is required by the public input contract; API examples require your Apify token.

## Which countries work?

Colombia, Mexico, Peru, Chile and Argentina, one country per run. Other countries are not advertised as supported.

## Why did a successful run return zero jobs?

Check SUMMARY: a complete search can have no matches, while invalid_input requests corrections. Invalid input is reported in logs and produces no job events. Apify may reject schema-invalid submissions before the Actor starts.

## Does SUCCEEDED mean the collection is complete?

No. Require status complete and complete true in SUMMARY. Partial output remains usable with its warnings. The client examples stop instead of hiding that distinction.

## Should I repeat a start after a network error?

Not blindly. A paid run may already have started before its response was lost. Inspect recent runs in Console. The examples send one start and use the existing run ID for reads.

## Are salaries and company data always present?

No. Missing salaries may be null, and countries can use different currencies or pay periods. Company overviews are optional and do not contain all employer reviews or salary records.

## Does CSV export start or pay for another collection?

The export script only reads the supplied Dataset. Storage reads can consume platform usage under your plan. It does not start an Actor run.
