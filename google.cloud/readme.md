- Copy all content from a local directory to a specific bucket-name/full-path (recursive) in google cloud storage:
```python
import glob
from google.cloud import storage

def upload_local_directory_to_gcs(local_path, bucket, gcs_path):
    assert os.path.isdir(local_path)
    for local_file in glob.glob(local_path + '/**'):
        if not os.path.isfile(local_file):
           upload_local_directory_to_gcs(local_file, bucket, gcs_path + "/" + os.path.basename(local_file))
        else:
           remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
           blob = bucket.blob(remote_path)
           blob.upload_from_filename(local_file)


upload_local_directory_to_gcs(local_path, bucket, BUCKET_FOLDER_DIR)
```

-  List all the files in a directory and then download them one by one
```python
from google.cloud import storage

bucket_name = 'your-bucket-name'
prefix = 'your-bucket-directory/'
dl_dir = 'your-local-directory/'

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name=bucket_name)
blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
for blob in blobs:
    filename = blob.name.replace('/', '_') 
    blob.download_to_filename(dl_dir + filename)  # Download
```

- Alternative: multiple-file-download-form-google-cloud-storage
```python
import logging
import os
from google.cloud import storage

global table_id
global bucket_name

logging.basicConfig(format=’%(levelname)s:%(message)s’, level=logging.DEBUG) 
bucket_name = ‘mybucket’
table_id = ‘shakespeare’
storage_client = storage.Client.from_service_account_json(‘/google-cloud/keyfile/service_account.json’)

# The “folder” where the files you want to download are
folder=’/google-cloud/download/{}’.format(table_id)
delimiter=’/’
bucket=storage_client.get_bucket(bucket_name)
blobs=bucket.list_blobs(prefix=table_id, delimiter=delimiter) #List all objects that satisfy the filter.

# Download the file to a destination 
def download_to_local():
    logging.info(‘File download Started…. Wait for the job to complete.’)
    # Create this folder locally if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)
    # Iterating through for loop one by one using API call
    for blob in blobs:
        logging.info(‘Blobs: {}’.format(blob.name))
        destination_uri = ‘{}/{}’.format(folder, blob.name) 
        blob.download_to_filename(destination_uri)
        logging.info(‘Exported {} to {}’.format(
            blob.name, destination_uri))

if __name__ == ‘__main__’:
    download_to_local()
```
