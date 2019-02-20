class NetworkEvent:

    def __init__(self, timestamp, server, source, packets):
        self.timestamp = timestamp
        self.server = server
        self.source = source
        self.packets = packets if packets else []








