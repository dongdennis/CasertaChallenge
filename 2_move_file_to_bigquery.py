from google.cloud import bigquery

def create_bq_dataset(dataset_name):
    """Create a BigQuery Dataset"""
    client = bigquery.Client()

    # Create a DatasetReference using a chosen dataset name.
    dataset_ref = client.dataset(dataset_name)

    # Construct a full Dataset object to send to the API.
    dataset = bigquery.Dataset(dataset_ref)

    # Specify the geographic location where the dataset should reside.
    dataset.location = "US"

    # Send the dataset to the API for creation.
    dataset = client.create_dataset(dataset)  # API request

def create_bq_table(dataset_name):
    """Create a BigQuery Table"""
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_name)

    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.skip_leading_rows = 1

    # The source format defaults to CSV, so the line below is optional.
    job_config.source_format = bigquery.SourceFormat.CSV
    uri = "gs://dennis-caserta-bucket/crypto_data.csv"
    
    load_job = client.load_table_from_uri(
        uri,
        dataset_ref.table('crypto_data'),
        job_config=job_config)  # API request
    print('Starting job {}'.format(load_job.job_id))

    load_job.result()  # Waits for table load to complete.
    print('Job finished.')

    destination_table = client.get_table(dataset_ref.table('crypto_data'))
    print('Loaded {} rows.'.format(destination_table.num_rows))

if __name__ == "__main__":
    # Set the dataset name
    dataset_name = "crypto_dataset"

    # Create a BigQuery dataset
    create_bq_dataset(dataset_name)
    
    # Create a BigQuery table
    create_bq_dataset(dataset_name)