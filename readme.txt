STEP 1 (Optional)
To run this add new/updated product_data.json/sales_data.csv to root folder if needed.

STEP 2
Run process_data.py

STEP 3
Press 'y' to proceed if data correct
- Next iteration will display files from step 1. Please manually check for now

STEP 4
View created file aggregated_report.csv in root
- From the examples, the first is incorrect, the second is correct.
- Will add more unit tests/review code to determine this.




Next iteration Goals:
Validate CSV and JSON are correct by user prompts.
Update 1 decimal point to 2 decimal points.
Fix computation error causing 1st example to be incorrect.
    - Seems to be from the multiple sales of same product (total_quantity).
Fix average_transaction_value
    - It is showing as 1/2 the expected value.
Add unit tests for these
Update data_enrichment with code from process_data.py
    - Review data_processing, see what else should be in data_enrichment
    - Double check data_enrichment and see what should be in data_processing


