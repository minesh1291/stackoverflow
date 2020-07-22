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
