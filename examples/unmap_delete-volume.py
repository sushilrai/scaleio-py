from scaleiopy.scaleio import ScaleIO
from pprint import pprint
import sys

# How to run:
# python unmap_delete-volume.py ip-to-mdm user pass volume_name

# Whats this code doing:
# Deletes specified volume and unmap from all mapped SDCs

sio = ScaleIO("https://" + sys.argv[1] + "/api",sys.argv[2],sys.argv[3],False,"ERROR") # HTTPS must be used as there seem to be an issue with 302 responses in Requests when using POST

sio.provisioning.delete_volume(sio.provisioning.get_volume_by_name(sys.argv[4]), 'ONLY_ME', autoUnmap=True)