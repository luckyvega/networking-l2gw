from neutronclient.common import extension
from neutronclient.i18n import _


class L2RemoteGateway(extension.NeutronClientExtension):
    resource = 'l2_remote_gateway'
    resource_plural = 'l2_remote_gateways'
    path = 'l2-remote-gateways'
    object_path = '/%s' % path
    resource_path = '/%s/%%s' % path
    versions = ['2.0']


class L2RemoteGatewaysList(extension.ClientExtensionList, L2RemoteGateway):
    """List remote gateways"""

    shell_command = 'l2-remote-gateway-list'
    list_columns = ['id', 'name','ipaddr']
    pagination_support = True
    sorting_support = True


class L2RemoteGatewayCreate(extension.ClientExtensionCreate, L2RemoteGateway):
    """Create remote gateway information."""

    shell_command = 'l2-remote-gateway-create'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', metavar='<REMOTE-GATEWAY-NAME>',
            help=_('Descriptive name for remote gateway.'))
        parser.add_argument(
            'ipaddr', metavar='<IP-ADDRESS>',
            help=_('IP Address of the remote gateway.'))

    def args2body(self, parsed_args):
        body = {'l2_remote_gateway': {'name': parsed_args.name,
                               'ipaddr': parsed_args.ipaddr}, }
        return body


class L2RemoteGatewayShow(extension.ClientExtensionShow, L2RemoteGateway):
    """Show information of a given remote gateway."""

    shell_command = 'l2-remote-gateway-show'


class L2RemoteGatewayDelete(extension.ClientExtensionDelete, L2RemoteGateway):
    """Delete a given remote gateway."""

    shell_command = 'l2-remote-gateway-delete'


class L2RemoteGatewayUpdate(extension.ClientExtensionUpdate, L2RemoteGateway):
    """Update a given remote gateway."""

    shell_command = 'l2-remote-gateway-update'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--name', metavar='name',
            help=_('Descriptive name of remote gateway.'))
        parser.add_argument(
            '--ipaddr', metavar='ipaddr',
            help=_('IP address of remote gateway.'))

    def args2body(self, parsed_args):
        params = {}
        body = {'l2_remote_gateway': params}

        if parsed_args.name:
            params['name'] = parsed_args.name
        if parsed_args.ipaddr:
            params['ipaddr'] = parsed_args.ipaddr

        return body
