import json, os, importlib, subprocess, sys

from packet_analyzer.core.kaitai_item import KaitaiItem


# Build ksy
cwd = os.getcwd()

description = cwd + "\\packet.ksy"
result = subprocess.run(["kaitai-struct-compiler.bat", "--debug", "-t", "python", description], stdout=sys.stdout)
lib = importlib.reload(__import__("packet"))

Packet = getattr(lib, "Packet")


class NetworkEvent:

    def __init__(self, timestamp, server, source, packets):
        self.timestamp = timestamp
        self.server = server
        self.source = source

        # Should packets be _read() here or not?
        # May be useful a list that parses packets on request.
        self.packets = packets

    @classmethod
    def from_dict(cls, d):
        timestamp = d["timestamp"]
        server = d["server"]
        source = d["source"]

        network_event = NetworkEvent(timestamp, server, source, None)

        packets = []
        for idx, packet_bytes in enumerate(d["packets"]):
            packet = Packet.from_bytes(bytes.fromhex(packet_bytes))
            kaitai_packet = KaitaiItem(str(idx), packet, None, None, network_event)
            packets.append(kaitai_packet)

        network_event.packets = packets
        return network_event

    @property
    def packet_count(self):
        return len(self.packets)








