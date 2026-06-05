# Pseudocode: Metrics Collector for XGoldNet Harvesting Client

class MetricsCollector:
    def __init__(self, mesh_interface):
        self.mesh = mesh_interface

    def collect_standard_metrics(self):
        """Collect basic mesh performance metrics."""
        return {
            "uptime": self.mesh.get_uptime(),
            "bandwidth_contributed_gb": self.mesh.get_bandwidth(),
            "active_peer_count": self.mesh.get_peer_count(),
            "average_latency_ms": self.mesh.get_average_latency(),
            "packet_loss": self.mesh.get_packet_loss()
        }

    def collect_harvesting_specific_metrics(self):
        """Collect metrics specific to harvesting activities."""
        return {
            "harvesting_claims_submitted": self.get_claim_count(),
            "special_tasks_completed": self.get_special_tasks_completed(),
            "data_quality_score": self.calculate_data_quality()  # e.g. for prototype sensors
        }

    def get_full_report(self):
        standard = self.collect_standard_metrics()
        harvesting = self.collect_harvesting_specific_metrics()
        standard.update(harvesting)
        return standard