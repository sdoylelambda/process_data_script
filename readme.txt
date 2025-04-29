STEP 1 (Optional)
To run this add new/updated product_data.json/sales_data.csv to root folder if needed.

STEP 2
Run process_data.py

STEP 3
Press 'Y' to proceed if data correct
- Next iteration will display files from step 1. Please manually check for now

STEP 4
View created file aggregated_report.csv in root

Tests
Run pytest root folder in bash after pip installing pytest.

Design
See UPER.txt for design details.

If additional tests fail
May need to update line 24 of data_enrichment to save as `sales_data.csv` - please note this will replace the input file
    - If Dates not formatted where expected.

Next iteration Goals:
Remove redundant calls - Pass data from ingestion
Validate CSV and JSON are correct by user prompts.
Verify correct logic in correct Library: ingestion, enrichment, processing
    - Update data_enrichment with code from process_data.py
    - Review data_processing, see what else should be in data_enrichment
    - Double check data_enrichment and see what should be in data_processing


