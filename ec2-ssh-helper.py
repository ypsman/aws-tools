#!/usr/bin/python2
import boto.ec2

AWS_REGIONS = ['region1', 'region2']
AWS_KEY = 'KEY'
AWS_SECRET = 'SECRET'
EC2_INSTANCES = []


class awsinstance():
    def __init__(self, **kwargs):
        self.__instid         = kwargs.pop('instid')
        self.__instname       = kwargs.pop('instname', 'None')
        self.__instip         = kwargs.pop('instip', 'None')
        self.namecorrection()

    def __str__(self):
        return str(self.__instid)

    def getip(self):
        return str(self.__instip.ljust(20))

    def name(self):
        return str(self.__instname)

    def namecorrection(self):
        self.__instname = self.__instname.lower()
        self.__instname = self.__instname.replace(" ", "-")

    def show(self):
        print self.__instid
        print self.__instname
        print self.__instip

def awsgetinstances(AWS_REGION):
    conn = boto.ec2.connect_to_region(AWS_REGION, aws_access_key_id=AWS_KEY,
    aws_secret_access_key=AWS_SECRET)
    reservations = conn.get_all_reservations()
    for res in reservations:
        for inst in res.instances:
            inid = inst.id
            instname = inst.tags['Name']
            inid = awsinstance(
            instid=inst.id,
            inststatus=inst.state,
            instname=inst.tags['Name'],
            instip=inst.private_ip_address
            )
            EC2_INSTANCES.append(inid)

def awsgetregions():
    for AWS_REGION in AWS_REGIONS:
        awsgetinstances(AWS_REGION)

def printer_host():
    for x in EC2_INSTANCES:
        print x.getip()+" "+x.name()

def printer_ssh():
    for x in EC2_INSTANCES:
        print "Host "+x.name()
        print "    Hostname "+x.getip()

def main():
    awsgetregions()
    print "___________________"
    print "For /etc/hosts file"
    print "___________________"
    printer_host()
    print "___________________"
    print "for ssh/config file"
    print "___________________"
    printer_ssh()


if __name__ == "__main__":
    main()
