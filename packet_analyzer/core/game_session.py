import os, json
from io import BytesIO

from kaitaistruct import KaitaiStream

from packet_analyzer.core.network_event import NetworkEvent
from packet_analyzer.parsers.packet import Packet


class GameSession:

    def __init__(self, file_path, network_events):
        self.file_path = file_path
        self.network_events = network_events

    @classmethod
    def from_file(cls, file_path):
        if not os.path.exists(file_path):
            return None

        network_events = []

        file_stream = open(file_path, 'r')
        lines = file_stream.readlines()
        for line in lines:
            parsed_network_event = json.loads(line)

            network_event = NetworkEvent(parsed_network_event["timestamp"], parsed_network_event["server"],
                                         parsed_network_event["source"], None)

            for packet_hex_string in parsed_network_event["packets"]:
                # Converts hex string to bytes and creates kaitai stream object
                packet_raw_bytes = bytes.fromhex(packet_hex_string)
                io = KaitaiStream(BytesIO(packet_raw_bytes))

                # Creates packet object based on stream and network event source
                try:
                    packet = Packet(network_event.source, io)
                    network_event.packets.append(packet)

                except EOFError:
                    # Do something with broken packets.
                    # Currently we ignore them
                    print("ERROR PARSING PACKET: {}".format(packet_hex_string))

            network_events.append(network_event)

        return GameSession(file_path, network_events)
