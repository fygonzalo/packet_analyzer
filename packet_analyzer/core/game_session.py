import os, json
from io import BytesIO
import traceback
from enum import Enum

from kaitaistruct import KaitaiStream

from packet_analyzer.core.network_event import NetworkEvent
from packet_analyzer.parsers.packet import Packet


class ServerType(Enum):
    Game = 0
    Login = 1


class NetworkSource(Enum):
    Server = 0
    Client = 1


class GameSession:

    def __init__(self, file_path, network_events):
        self.file_path = file_path
        self.network_events = network_events

    @classmethod
    def from_file(cls, file_path):
        #TODO IMPROVE THIS!

        if not os.path.exists(file_path):
            return None

        network_events = []

        game_server_addresses = []

        file_stream = open(file_path, 'r')
        lines = file_stream.readlines()
        for line in lines:
            parsed_network_event = json.loads(line)

            network_event = NetworkEvent(parsed_network_event["timestamp"], parsed_network_event["server"],
                                         parsed_network_event["source"], None)

            server_type = ServerType.Login
            if network_event.server in game_server_addresses:
                server_type = ServerType.Game

            network_source = NetworkSource.Server
            if network_event.source == "Client":
                network_source = NetworkSource.Client

            for packet_hex_string in parsed_network_event["packets"]:
                # Converts hex string to bytes and creates kaitai stream object
                packet_raw_bytes = bytes.fromhex(packet_hex_string)
                io = KaitaiStream(BytesIO(packet_raw_bytes))

                # Creates packet object based on stream and network event source
                try:
                    packet = Packet(network_source.value, server_type.value, io)
                    network_event.packets.append(packet)

                    if network_event.source == "Server" and packet.header.sequence > 0:
                        for msg_container in packet.content.container:
                            message = msg_container.content
                            if (server_type == ServerType.Login and message.code == 4) or (server_type == ServerType.Game and message.code == 12):
                                game_server_address = message.content.content
                                ip = game_server_address.ip
                                port = game_server_address.port
                                new_game_server_address = "{}:{}".format(ip, port)

                                if not new_game_server_address in game_server_addresses:
                                    game_server_addresses.append(new_game_server_address)

                except EOFError as eof_error:
                    # Do something with broken packets.
                    # Currently we ignore them
                    print("ERROR PARSING PACKET: {}".format(packet_hex_string))
                    print("SOURCE: {}".format(parsed_network_event["source"]))
                    print("SERVER TYPE: {}".format("Game" if server_type == ServerType.Game else "Login"))
                    print("EXCEPTION:")
                    print(traceback.print_exc())
                    print()

            network_events.append(network_event)

        return GameSession(file_path, network_events)
