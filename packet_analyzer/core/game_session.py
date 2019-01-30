import os, json

from packet_analyzer.core.network_event import NetworkEvent


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
            parsed_line = json.loads(line)

            network_event = NetworkEvent.from_dict(parsed_line)
            network_events.append(network_event)

        return GameSession(file_path, network_events)