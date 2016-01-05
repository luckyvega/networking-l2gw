from neutronclient.common import extension
from neutronclient.i18n import _


class L2RemoteGatewayConnection(extension.NeutronClientExtension):
    resource = 'l2_remote_gateway_connection'
    resource_plural = 'l2_remote_gateway_connections'
    path = 'l2-remote-gateway-connections'
    object_path = '/%s' % path
    resource_path = '/%s/%%s' % path
    versions = ['2.0']


class L2RemoteGatewaysConnectionList(extension.ClientExtensionList,
                                     L2RemoteGatewayConnection):

    shell_command = 'l2-remote-gateway-connection-list'
    list_columns = ['id', 'gateway', 'network', 'remote_gateway',
                    'seg_id', 'flood']
    pagination_support = True
    sorting_support = True


class L2RemoteGatewayConnectionCreate(extension.ClientExtensionCreate,
                                      L2RemoteGatewayConnection):

    shell_command = 'l2-remote-gateway-connection-create'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'gateway', metavar='<GATEWAY-NAME/UUID>',
            help=_('Descriptive name/UUID for local gateway.'))
        parser.add_argument(
            'network', metavar='<NETWORK-NAME/UUID>',
            help=_('Name of local network to connect to the remote gateway'))
        parser.add_argument(
            'remote_gateway', metavar='<REMOTE-GATEWAY-NAME/UUID>',
            help=_('Descriptive name/UUID for remote gateway.'))
        parser.add_argument(
            '--seg-id', metavar='seg_id',
            help=_('Segmentation ID for the connection to the remote gateway'))
        parser.add_argument(
            '--flood', metavar='flood',
            help=_('Whether to flood un-known MACs and broadcasts '
                   'to remote connection'))

    def args2body(self, parsed_args):
        body = {'l2_remote_gateway_connection':
                    {'gateway': parsed_args.gateway,
                     'network': parsed_args.network,
                     'remote_gateway' : parsed_args.rgw,
                     'seg_id' : parsed_args.seg_id,
                     'flood' : parsed_args.flood},
                    }
        return body


class L2RemoteGatewayConnectionShow(extension.ClientExtensionShow, L2RemoteGatewayConnection):

    shell_command = 'l2-remote-gateway-connection-show'


class L2RemoteGatewayConnectionDelete(extension.ClientExtensionDelete, L2RemoteGatewayConnection):

    shell_command = 'l2-remote-gateway-connection-delete'
