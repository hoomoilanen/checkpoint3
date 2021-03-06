

import sys
from google.cloud import storage
import os.path
import time
import argparse
parser = argparse.ArgumentParser()

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Blob {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )



def luku():
    import argparse
    parser = argparse.ArgumentParser()
    file = open("checkpoint.txt")
    
    parser.add_argument('rivit', type=int, help='rivien maara')
    args = parser.parse_args()
    x = []
    for index, line in enumerate(file):

        if index == args.rivit:
            break
        x.append(line)
    x.sort(key=len)
    y = ''.join(x)
    print(y)

def wait():
    while not os.path.exists('C:/Users/Henri/Documents/checkpoint3/vko3-2/checkpoint.txt'):
        time.sleep(1)

    if os.path.isfile('C:/Users/Henri/Documents/checkpoint3/vko3-2/checkpoint.txt'):
            luku()
            
    else:
        raise ValueError("%s isn't a file!" % file_path)
download_blob('juukeli', 'checkpoint1', 'checkpoint.txt')
wait()