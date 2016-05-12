# from charmhelpers.core import hookenv
from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes
# from charms.reactive import is_state
# from charms.reactive import not_unless


class CephPeer(RelationBase):
    scope = scopes.SERVICE

    @hook('{provides:ceph}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
        # service = hookenv.remote_service_name()
        # conversation = self.conversation()

    def set_network(self, network):
        for conversation in self.conversations():
            conversation.set_remote({
                'ceph-public-address': network
            })
        self.set_state('{relation_name}.available')

    # def provide_auth(self, key, auth_supported):
    #     """
    #     Provide a token to a requesting service.
    #     :param str key: The key to access Ceph
    #     :param str auth_supported: Supported auth methods
    #     """
