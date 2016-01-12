import abc

from neutron.api import extensions
from neutron.api.v2 import attributes
from neutron.api.v2 import resource_helper

from networking_l2gw.services.l2gateway.common import constants

RESOURCE_ATTRIBUTE_MAP = {
    constants.L2_REMOTE_GATEWAY_CONNECTIONS: {
        'id': {'allow_post': False, 'allow_put': False,
               'is_visible': True},
        'gateway': {'allow_post': True, 'allow_put': True,
                           'validate': {'type:string': None},
                           'is_visible': True, 'default': ''},
        'network': {'allow_post': True, 'allow_put': True,
                          'validate': {'type:string': None},
                          'is_visible': True, 'default': ''},
        'remote_gateway': {'allow_post': True, 'allow_put': True,
                           'validate': {'type:string': None},
                           'is_visible': True, 'default': ''},
        'seg_id': {'allow_post': True, 'allow_put': True,
                   'validate': {'type:string': None},
                   'is_visible': True},
        'flood': {'allow_post': True, 'allow_put': True,
                  'validate': {'type:string': None},
                  'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'validate': {'type:string': None},
                      'required_by_policy': True,
                      'is_visible': True}
    },
}


class L2remotegatewayconnection(extensions.ExtensionDescriptor):

    @classmethod
    def get_name(cls):
        return "L2 Remote Gateway Connection"

    @classmethod
    def get_alias(cls):
        return "l2-remote-gateway-connection"

    @classmethod
    def get_description(cls):
        return "Define connection between local network and " \
               "a remote gateway using defined segmentation id"

    @classmethod
    def get_updated(cls):
        return "2015-12-31T00:00:00-00:00"

    @classmethod
    def get_resources(cls):
        """Returns Ext Resources."""
        mem_actions = {}
        plural_mappings = resource_helper.build_plural_mappings(
            {}, RESOURCE_ATTRIBUTE_MAP)
        attributes.PLURALS.update(plural_mappings)
        resources = resource_helper.build_resource_info(plural_mappings,
                                                        RESOURCE_ATTRIBUTE_MAP,
                                                        constants.L2GW,
                                                        action_map=mem_actions,
                                                        register_quota=True,
                                                        translate_name=True)
        return resources

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}


class L2RemoteGatewayConnectionPluginBase(extensions.PluginInterface):

    @abc.abstractmethod
    def get_l2_remote_gateway_connections(self, context, filters=None,
                                          fields=None,
                                          sorts=None, limit=None, marker=None,
                                          page_reverse=False):
        pass

    @abc.abstractmethod
    def get_l2_remote_gateway_connection(self, context, id, fields=None):
        pass

    @abc.abstractmethod
    def create_l2_remote_gateway_connection(self, context,
                                            l2_remote_gateway_conn):
        pass

    @abc.abstractmethod
    def update_l2_remote_gateway_connection(self, context, id,
                                            l2_remote_gateway_conn):
        pass

    @abc.abstractmethod
    def delete_l2_remote_gateway_connection(self, context, id):
        pass

