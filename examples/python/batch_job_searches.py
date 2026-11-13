"""Two country searches, sequentially; each starts a separately billed run."""
import json
from common import start_once, wait_for_dataset, iter_rows

def main():
    for country in ['co', 'mx']:
        actor_input = {'query':'ventas', 'country':country, 'maxResults':3}
        run_id = start_once(actor_input, maximum_usd=0.05)
        dataset_id = wait_for_dataset(run_id)
        print(json.dumps({'country':country,'jobs':list(iter_rows(dataset_id))},ensure_ascii=False))

if __name__ == '__main__':
    main()
