from kaitaistruct import KaitaiStruct

from anytree.node.nodemixin import NodeMixin


class Node(NodeMixin):
    def __init__(self, name, value, parent=None):
        super(Node, self).__init__()
        self.name = name
        self.value = value
        self.parent = parent

    @property
    def class_name(self):
        return self.value.__class__.__name__


class KSNode(Node):

    def __init__(self, name, value, start, end, buffer, parent=None):
        super(KSNode, self).__init__(name, value, parent)
        self.buffer = buffer


def construct_protocol_tree(game_sesion):
    game_session_node = Node("Game session", game_sesion)

    for i, network_event in enumerate(game_sesion.network_events):
        network_event_node = Node(str(i), network_event, game_session_node)

        Node("timestamp", network_event.timestamp, network_event_node)
        Node("server", network_event.server, network_event_node)
        Node("source", network_event.source, network_event_node)

        packet_list_node = Node("packets", network_event.packets, network_event_node)

        def node_from_ks_instance(name, value, start, end, buffer, parent_node):
            k_node = KSNode(name, value, start, end, buffer, parent_node)

            if isinstance(value, (KaitaiStruct, list)):
                if isinstance(value, KaitaiStruct):
                    for k in value.SEQ_FIELDS:
                        v = getattr(value, k)

                        s = value._debug[k]["start"]
                        e = value._debug[k]["end"]

                        try:
                            value._io.seek(s)
                            b = value._io.read_bytes(e - s)
                        except EOFError:
                            s = None
                            e = None
                            b = None

                        node_from_ks_instance(k, v, s, e, b, k_node)

                elif isinstance(value, list):
                    for n, el in enumerate(value):
                        s = parent_node.value._debug[name]["arr"][n]["start"]
                        e = parent_node.value._debug[name]["arr"][n]["end"]

                        parent_node.value._io.seek(s)
                        b = parent_node.value._io.read_bytes(e - s)

                        node_from_ks_instance(str(n), el, s, e, b, k_node)

        for j, packet in enumerate(network_event.packets):
            packet._io.seek(0)
            buffer = packet._io.read_bytes_full()
            node_from_ks_instance(str(j), packet, None, None, buffer, packet_list_node)

    return game_session_node





























def build_prototree(game_session):

    def expand_ks_node(ks_node):
        if isinstance(ks_node, KaitaiStruct):
            pass
        if isinstance(ks_node, list):
            pass
        return

    root = Node(name="Network Events", value=game_session)

    for i, network_event in enumerate(game_session.network_events):
        ne_node = Node(parent=root, name=str(i), value=network_event)

        ne_timestamp_node = Node(parent=ne_node, name="timestamp", value=network_event.timestamp)
        ne_server_node = Node(parent=ne_node, name="server", value=network_event.server)
        ne_source_node = Node(parent=ne_node, name="source", value=network_event.source)
        ne_packets_node = Node(parent=ne_node, name="packets", value=network_event.packets)


        for j, packet in enumerate(network_event.packets):
            p_node = Node(parent=ne_packets_node, name=str(j), value=packet)

            public_members = packet.SEQ_FIELDS
            for k in public_members:
                Node(parent=p_node, name=k, value=getattr(packet, k))

    return root
