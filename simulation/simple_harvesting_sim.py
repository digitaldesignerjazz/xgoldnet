# Simple Simulation: XGoldNet Harvesting with Multiple Virtual Nodes

# This script simulates several nodes reporting to a mock Nexus
# and claiming XGold rewards. Useful for testing logic before real implementation.

from dataclasses import dataclass
import random

@dataclass
class MockNexus:
    def register_node(self, node_id, metadata, stake):
        print(f"[Nexus] Registered node {node_id}")
        return type('obj', (object,), {'success': True, 'initial_stake': stake})()

    def submit_performance_report(self, report):
        print(f"[Nexus] Received report from {report['node_id']}")

    def validate_harvest_claim(self, node_id, claim, reputation):
        # Simple approval logic for simulation
        if claim['avg_uptime'] > 0.85 and claim['bandwidth_gb'] > 10:
            amount = claim['bandwidth_gb'] * 0.5 + (reputation * 0.1)
            return type('obj', (object,), {'status': 'approved', 'amount': round(amount, 2)})()
        else:
            return type('obj', (object,), {'status': 'rejected', 'reason': 'Low performance'})()

    def get_available_special_tasks(self, node_id):
        if random.random() > 0.7:
            return [type('obj', (object,), {
                'id': f'task_{random.randint(1000,9999)}',
                'difficulty': random.randint(1,5),
                'bonus': random.uniform(1.0, 3.0)
            })()]
        return []


class VirtualNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.client = None  # Will be set later

    def run_harvesting_cycle(self, nexus):
        # Simulate metrics
        uptime = random.uniform(0.7, 1.0)
        bandwidth = random.uniform(5, 80)

        # Simple local claim generation
        claim = {
            "period": "last_24h",
            "bandwidth_gb": bandwidth,
            "avg_uptime": round(uptime, 2),
            "special_tasks": 0,
            "reputation": 85
        }

        result = nexus.validate_harvest_claim(self.node_id, claim, claim['reputation'])
        if result.status == "approved":
            print(f"[{self.node_id}] Earned {result.amount} XGold")
        else:
            print(f"[{self.node_id}] Claim rejected")


if __name__ == "__main__":
    print("=== XGoldNet Harvesting Simulation ===\n")

    nexus = MockNexus()
    nodes = [VirtualNode(f"node_{i}") for i in range(5)]

    for cycle in range(3):
        print(f"\n--- Cycle {cycle + 1} ---")
        for node in nodes:
            node.run_harvesting_cycle(nexus)

    print("\nSimulation complete.")