# from charmhelpers.core import hookenv
from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes
# from charms.reactive import is_state
# from charms.reactive import not_unless
# from charms.reactive import set_state


class CephPeer(RelationBase):
    scope = scopes.UNIT

    @hook('{peers:ceph}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
        # service = hookenv.remote_service_name()
        # conversation = self.conversation()

    def set_network(self, network):
        # conversation = self.conversation()
        for conversation in self.conversations():
            conversation.set_remote('ceph-public-address', network)
            conversation.set_state('{relation_name}.available')

    # def provide_auth(self, key, auth_supported):
    #     """
    #     Provide a token to a requesting service.
    #     :param str key: The key to access Ceph
    #     :param str auth_supported: Supported auth methods
    #     """
