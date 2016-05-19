# Installation on a packestack based machine 

## Controller node installation
- Install git 
```
sudo yum install git
```
- clone this repository and run install script 
```
git clone https://github.com/oferby/networking-l2gw
cd networking-l2gw && sudo ./bin/install.sh
```
- stop neutron service and enable l2-agent
```
openstack-service stop neutron
openstack-service enable neutron-l2gw-agent
```
- edit configuration files

- /etc/neutron/neutron.conf
```
[DEFAULT]
core_plugin =neutron.plugins.ml2.plugin.Ml2Plugin
service_plugins =networking_l2gw.services.l2gateway.plugin.L2GatewayPlugin,router

``` 
- /etc/neutron/l2gateway_agent.ini
``` 
[DEFAULT]

[ovsdb]
ovsdb_hosts = NAME_OF_BGW1:MGMT_IP1:OVSDB_PORT1,NAME_OF_BGW2:MGMT_IP2:OVSDB_PORT2
enable_manager = False
``` 
- /etc/neutron/l2gw_plugin.ini
```
[DEFAULT]
[service_providers]
service_provider=L2GW:l2gw:networking_l2gw.services.l2gateway.service_drivers.rpc_l2gw.L2gwRpcDriver:default
```
- /etc/neutron/plugins/ml2/openvswitch_agent.ini
```
[ovs]
local_ip = LOCAL_DATA_IP
enable_tunneling=True
[agent]
tunnel_types =vxlan
l2_population = True
arp_responder = True
prevent_arp_spoofing = True
dont_fragment = ###False | True
enable_distributed_routing = ### False | True
[securitygroup]
enable_security_group = True
```
- /etc/neutron/plugins/ml2/ml2_conf.ini
```
[ml2]
type_drivers = vxlan
mechanism_drivers =openvswitch,l2population
[vxlan]
enable_vxlan = True
local_ip = ##LOCAL_DATA_IP
l2_population = True
[ovs]
enable_tunneling = True
datapath_type = system
local_ip = ##LOCAL_DATA_IP
l2_population = True
[securitygroup]
enable_security_group = True
```
- start neutron service
```
openstack-service start neutron
```
