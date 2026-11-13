# Input reference

One country per run. The Actor form and current schema are authoritative. Friendly selectors may coexist with matching legacy values; conflicting aliases cause an input warning.

| Field | Type | Default | Meaning |
|---|---|---|---|
| `country` | string | `"co"` | Choose the country where you want to find jobs. One country per run. |
| `query` | string | `""` | For example: programador, accountant or sales. Leave empty to search all jobs in the selected country. |
| `location` | string | `""` | Enter a city in the selected country, for example Bogota. Leave empty for all cities. Do not combine with coordinates. |
| `maxResults` | integer | `100` | Choose 1 to 1,000 unique jobs. The example collects only 3 jobs. |
| `workArrangements` | array | `[]` | Select on-site, hybrid or remote jobs. Leave empty to include every arrangement. |
| `postedWithin` | string | `"any"` | Choose how recently a job was updated. Any time does not add a date filter. |
| `sortBy` | string | `"relevance"` | Relevance or salary, as ranked by the source. The new-offers feed retains its source ordering. |
| `feed` | string | `"search"` | Search all matching jobs, or use the new-offers feed. New offers requires the Most relevant sort option. |
| `includeDetails` | boolean | `true` | Add the published full description, contract, education and dates. |
| `includeCompact` | boolean | `false` | Add published skills, salary insights and expiry information. Availability varies. |
| `includeCompanyProfiles` | boolean | `false` | Add the public company overview, mission and awards when available. This does not collect complete review, salary or company-job catalogues. |
| `latitude` | number | `null` | Geographic center. Set latitude, longitude and distance together; omit when using city. |
| `longitude` | number | `null` | Geographic center longitude. Omit when using city. |
| `distance` | integer | `null` | Geographic radius. Requires both coordinates. |
| `categoryIds` | array | `[]` | Optional country-specific IDs. Usually leave empty. Add whole-number IDs only; invalid options produce an input-correction message. |
| `contractIds` | array | `[]` | Optional country-specific IDs. Usually leave empty. Add whole-number IDs only; invalid options produce an input-correction message. |
| `salaryIds` | array | `[]` | Optional country-specific IDs. Usually leave empty. Add whole-number IDs only; invalid options produce an input-correction message. |
| `employmentIds` | array | `[]` | Optional country-specific IDs. Usually leave empty. Add whole-number IDs only; invalid options produce an input-correction message. |
| `experienceIds` | array | `[]` | Optional country-specific IDs. Usually leave empty. Add whole-number IDs only; invalid options produce an input-correction message. |
| `maxPages` | integer | `100` | Stop after this many search pages. A page cap reached before the requested results or proven source end is reported as partial. |
| `workplaceTypeIds` | array | `[]` | Legacy API field: 1 on-site, 2 hybrid, 3 remote. Use Work arrangement in the form. |
| `updatedSinceId` | integer | `0` | Legacy API field: 0, 1, 2, 3, 7, 15, 30 or 90 days. Use the Updated within dropdown instead. Do not combine different windows. |

## Coordinate alternative

Use all three coordinate fields together and leave City empty. These are an alternative to city matching, not additional independent filters. The neutral example below selects the same country but does not guarantee matching jobs.

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
  "latitude": 4.65,
  "longitude": -74.08,
  "distance": 5,
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

IDs are country-specific supported filter values. Unsupported IDs or an ambiguous city yield `invalid_input` without widening the search. A malformed submission may be rejected by Apify before a run starts.
