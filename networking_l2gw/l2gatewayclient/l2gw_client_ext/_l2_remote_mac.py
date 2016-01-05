from neutronclient.common import extension
from neutronclient.i18n import _


class L2RemoteMac(extension.NeutronClientExtension):
    resource = 'l2_remote_mac'
    resource_plural = '/%ss' % resource
    path = 'l2-remote-macs'
    object_path = '/%s' % path
    resource_path = '/%s/%%s' % path
    versions = ['2.0']


class L2RemoteMacList(extension.ClientExtensionList,
                                     L2RemoteMac):

    shell_command = 'l2-remote-mac-list'
    list_columns = ['id', 'mac', 'ipaddr', 'remote_gateway_conn']
    pagination_support = True
    sorting_support = True


class L2RemoteMacCreate(extension.ClientExtensionCreate,
                        L2RemoteMac):

    shell_command = 'l2-remote-mac-create'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'mac', metavar='<MAC>',
            help=_('MAC address of remote host'))
        parser.add_argument(
            'remote_gateway_conn', metavar='<REMOTE-GATEWAY-CONN-UUID>',
            help=_('Remote Gateway Connection UUID.'))
        parser.add_argument(
            '--ipaddr', metavar='ipaddr',
            help=_('IP address of remote host'))

    def args2body(self, parsed_args):
        body = {'l2_remote_mac':
                    {'mac': parsed_args.mac,
                     'network': parsed_args.network,
                     'remote_gateway_conn': parsed_args.remote_gateway_conn},
                }
        if parsed_args.ipaddr:
            body['ipaddr']=parsed_args.ipaddr
        return body


class L2RemoteMacShow(extension.ClientExtensionShow, L2RemoteMac):

    shell_command = 'l2-remote-mac-show'


class L2RemoteMacDelete(extension.ClientExtensionDelete, L2RemoteMac):

    shell_command = 'l2-remote-mac-delete'
