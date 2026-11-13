# Run from Apify Console

Open the [Actor](https://apify.com/datascraperes/computrabajo-jobs-extractor?fpr=edudata), sign in and choose a supported country. Enter a keyword such as `programador`, leave City empty initially and request three jobs. Start the run, inspect its Dataset and check the collection summary. Export JSON, CSV or Excel.

If City is provided, it must resolve uniquely inside the chosen country. For coordinates, supply latitude, longitude and distance together and clear City. Do not put several countries in one field. Advanced numeric filters are country-specific; prefer the friendly form controls when available. Missing or invalid filters are explained rather than silently ignored.

A successful platform status can contain an input correction or partial collection. Inspect SUMMARY and warnings before using the output as complete. See the [input reference](input-reference.md) and [output reference](output-reference.md).
