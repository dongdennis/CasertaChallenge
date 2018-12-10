from google.cloud import storage, exceptions

def create_bucket(bucket_name):
    """Creates a new bucket."""
    storage_client = storage.Client()
    try:
        # Check if bucket exists in current project
        if storage_client.lookup_bucket(bucket_name):
            print("Error: Bucket '{}' already exists in current project.".format(bucket_name))
        else:
            # Create a new Google Cloud bucket
            storage_client = storage.Client()
            bucket = storage_client.create_bucket(bucket_name)
            print("Bucket '{}' created".format(bucket.name))

    # If bucket already exists in another Google Cloud account
    except exceptions.Forbidden:
        print("Error: Bucket '{}' exists in another Google Cloud account.".format(bucket_name))
    except:
        print("Error: Could not create bucket '{}'. Check the bucket name.".format(bucket_name))
    
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    
    # Set the bucket name
    bucket = storage_client.get_bucket(bucket_name)

    # Set the blob destination
    blob = bucket.blob(destination_blob_name)

    # Upload blob file
    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(
        source_file_name,
        destination_blob_name))

if __name__ == "__main__":
    # Set the Google Cloud bucket name
    bucket_name = "dennis-caserta-bucket"

    #Set the file name
    file_name = "crypto_data.csv"
    
    # Create a Google Cloud bucket
    create_bucket(bucket_name)

    # Upload CSV file to Google Cloud storage
    upload_blob(bucket_name, "/Users/dennis.dong/Desktop/c/{}".format(file_name), file_name)
    




