<<<<<<< HEAD
=======
#!/usr/bin/python3

>>>>>>> bf8703e394be05ac6141e480c1fd80262ba52676
import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

access_id = 'AKIAIALXFBMSTE27IXYA'
access_key = 'hS3giagKSdTJoVwpxfu5V6F8mStAXJflld3bceqf'
<<<<<<< HEAD
region = '<REGION>'
endpoint = 's3={}.amazonaws.com'.format(region)
auth = aws4auth.AWS4auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml__pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())

def create_bucket(bucket):
        print('Bucket name: {}'.format(bucket))
=======
region = 'us-west-2'
endpoint = 's3-{}.amazonaws.com'.format(region)
auth = aws4auth.AWS4Auth(access_id, access_key, region, 's3')
ns = 'http://s3.amazonaws.com/doc/2006-03-01/'

def xml_pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())

def create_bucket(bucket):
    print('Bucket name: {}'.format(bucket))
    XML = ET.Element('CreateBucketConfiguration')
    XML.attrib['xmlns'] = ns
    location = ET.SubElement(XML, 'LocationConstraint')
    location.text = auth.region
    data = ET.tostring(XML, encoding='utf-8')
    url = 'http://{}.{}'.format(bucket, endpoint)
    r = requests.put(url, data=data, auth=auth)
    if r.ok:
        print('Created bucket {}'.format(bucket))
    else:
        xml_pprint(r.text)

def delete_bucket(bucket):
    url = 'http://{}.{}'.format(bucket, endpoint)
    r = requests.delete(url, auth=auth)
    if r.ok:
        print('Deleted bucket {}'.format(bucket))
    else:
        xml_pprint(r.text)
>>>>>>> bf8703e394be05ac6141e480c1fd80262ba52676

if __name__ == '__main__':
    cmd, *args = sys.argv[1:]
    globals()[cmd](*args)
