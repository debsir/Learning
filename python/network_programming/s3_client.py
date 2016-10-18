import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

access_id = 'AKIAIALXFBMSTE27IXYA'
access_key = 'hS3giagKSdTJoVwpxfu5V6F8mStAXJflld3bceqf'
region = '<REGION>'
endpoint = 's3={}.amazonaws.com'.format(region)
auth = aws4auth.AWS4auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml__pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())

def create_bucket(bucket):
        print('Bucket name: {}'.format(bucket))

if __name__ == '__main__':
    cmd, *args = sys.argv[1:]
    globals()[cmd](*args)
