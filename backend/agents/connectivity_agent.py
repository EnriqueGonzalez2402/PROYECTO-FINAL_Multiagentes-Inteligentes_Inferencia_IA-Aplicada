from serial.tools import list_ports

class ConnectivityAgent:

    def get_connected_nodes(self):

        ports = list(list_ports.comports())

        nodes = []

        for port in ports:

            description = port.description.lower()

            if (
                "cp210" in description
                or "silicon labs" in description
                or "ch340" in description
                or "usb serial" in description
            ):

                nodes.append(
                    {
                        "port": port.device,
                        "description": port.description
                    }
                )

        return nodes

    def verify_nodes(self, expected_nodes):

        nodes = self.get_connected_nodes()

        connected = len(nodes)

        missing = expected_nodes - connected

        if missing < 0:
            missing = 0

        return {
            "expected": expected_nodes,
            "connected": connected,
            "missing": missing,
            "nodes": nodes
        }