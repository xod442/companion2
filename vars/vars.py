import os

afc_ip = "10.251.1.25"
username = "admin"
password = "admin"
switch_pass = "admin"
auth_header = {}

os.environ['no_proxy'] = afc_ip
os.environ['NO_PROXY'] = afc_ip

base_url = "https://{0}/api/v1/".format(afc_ip)

leaf_switch_list = [
    "10.251.1.12",
    "10.251.1.13",
    "10.251.1.14",
    "10.251.1.15"
    ]

spine_switch_list = [
    "10.251.1.11"
    ]

switch_list = leaf_switch_list + spine_switch_list
fabric_name = "dsa-2"
fabric_description = "Data Center 2 POD 466.2"
vrf_name = "test_VRF"
ntp_name = "ntp-fabric"
dns_afc_name = "dns-fabric"
timezone="America/Los_Angeles"
