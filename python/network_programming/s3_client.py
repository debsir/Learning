import sys
import requests
import requests_aws4 as aws4auth
import xml.etree.ElemntTree as ET
import xml.dom.minidom as minidom

access_id = ''
access_key = ''
region = ''
endpoint = 's3-{}.amazonaws.com'.format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())

def create_bucket(bucket):
    print('Bucket name: {}'.format(bucket))


if __name__ == '__main__':
    cmd, *args = sys.argv[1:]
    globals()[cmd](*args)
