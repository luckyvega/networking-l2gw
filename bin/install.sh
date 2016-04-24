#!/bin/bash -x

if  [ `getenforce` != "Permissive" ]; then
    setenforce permissive
    sed -i 's/enforcing/permissive/g' /etc/sysconfig/selinux
    setsebool secure_mode_policyload on
fi

FROM_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
cd $FROM_DIR 
rm -fr `python setup.py install --record -` build *.egg-info
python setup.py install
neutron-db-manage upgrade head
openstack-service stop neutron
cp usr/lib/systemd/system/neutron-l2gw-agent.service /usr/lib/systemd/system/
cp usr/lib/systemd/system/neutron-server.service /usr/lib/systemd/system/
openstack-service start neutron
echo "redhat based Installtion is done"
