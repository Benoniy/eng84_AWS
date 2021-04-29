import boto3

file = open("access-token", "r")
ak = file.readline().strip("\n")
sak = file.readline().strip("\n")
region = "eu-west-1"
s3 = boto3.client('s3', aws_access_key_id=ak, aws_secret_access_key=sak, region_name=region)


def create_bucket():
    location = {'LocationConstraint': region}
    s3.create_bucket(Bucket="eng84-ben-test-bucket", CreateBucketConfiguration=location)


def list_all():
    list_b = s3.list_buckets()

    print("Buckets:")
    for bucket in list_b['Buckets']:
        print(f"{bucket['Name']}")


def delete_bucket():
    pass


if __name__ == "__main__":
    list_all()
