import boto3

file = open("access-token", "r")
region = "eu-west-1"
s3 = boto3.client('s3', region_name=region)
bucket = "eng84-ben-test-bucket"


def create_bucket():
    location = {'LocationConstraint': region}
    s3.create_bucket(Bucket=bucket, CreateBucketConfiguration=location)


def list_all():
    list_b = s3.list_buckets()

    print("Buckets:")
    for buck in list_b['Buckets']:
        print(f"{buck['Name']}")


def delete_bucket():
    s3.delete_bucket(Bucket=bucket)


def upload_file(filename):
    s3.upload_file(filename, bucket, filename)


def sync_file(filename):
    s3.download_file(bucket, filename, filename)


def delete_file(filename):
    s3.delete_object(Bucket=bucket, Key=filename)


if __name__ == "__main__":
    # create_bucket()
    # list_all()
    # upload_file("test.md")
    # sync_file("test.md")
    # delete_file("test.md")
    # delete_bucket()
    pass
