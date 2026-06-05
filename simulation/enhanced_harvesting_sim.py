# Enhanced XGoldNet Harvesting Simulation

# Features:
# - Multiple nodes with reputation
# - Slashing mechanics
# - Special tasks
# - Statistics and summary at the end

 import random
 from dataclasses import dataclass, field
 from typing import List, Dict

@dataclass
class NodeState:
    node_id: str
    stake: float = 100.0
    reputation: float = 80.0
    total_earned: float = 0.0
    total_slashed: float = 0.0
    tasks_completed: int = 0

@dataclass
class MockNexus:
    def validate_claim(self, node: NodeState, claim: dict):
        if claim['avg_uptime'] < 0.8:
            return {'status': 'slashed', 'slash_percent': 10}
        amount = claim['bandwidth_gb'] * 0.8 + (node.reputation * 0.2)
        return {'status': 'approved', 'amount': round(amount, 2)}

    def get_special_task(self):
        if random.random() > 0.6:
            return {
                'id': f"task_{random.randint(10000,99999)}",
                'difficulty': random.randint(2, 6),
                'bonus': round(random.uniform(1.5, 4.0), 2)
            }
        return None

class EnhancedSimulation:
    def __init__(self, num_nodes: int = 8):
        self.nodes: Dict[str, NodeState] = {}
        for i in range(num_nodes):
            self.nodes[f"node_{i}"] = NodeState(node_id=f"node_{i}")
        self.nexus = MockNexus()
        self.history = []

    def run_cycle(self, cycle_num: int):
        print(f"\n=== Cycle {cycle_num} ===")
        for node_id, node in self.nodes.items():
            # Simulate performance
            uptime = random.uniform(0.75, 1.0)
            bandwidth = random.uniform(10, 120)

            claim = {
                "avg_uptime": round(uptime, 2),
                "bandwidth_gb": round(bandwidth, 1)
            }

            result = self.nexus.validate_claim(node, claim)

            if result['status'] == 'approved':
                reward = result['amount']
                node.total_earned += reward
                node.reputation = min(100.0, node.reputation + 1.5)
                print(f"  {node_id}: +{reward} XGold | Rep: {node.reputation:.1f}")
            else:
                slash = node.stake * (result.get('slash_percent', 10) / 100)
                node.stake -= slash
                node.total_slashed += slash
                node.reputation = max(0.0, node.reputation - 8)
                print(f"  {node_id}: SLASHED {slash:.2f} | Rep: {node.reputation:.1f}")

            # Special task chance
            if random.random() > 0.75:
                task = self.nexus.get_special_task()
                if task and task['difficulty'] <= (node.reputation / 15):
                    bonus = task['bonus'] * 30
                    node.total_earned += bonus
                    node.tasks_completed += 1
                    node.reputation += 3
                    print(f"  {node_id}: Completed special task! +{bonus} bonus")

    def print_summary(self):
        print("\n========== SIMULATION SUMMARY ==========")
        total_earned = 0
        for node_id, node in self.nodes.items():
            print(f"{node_id}: Earned={node.total_earned:.2f} | Slashed={node.total_slashed:.2f} | Rep={node.reputation:.1f} | Tasks={node.tasks_completed}")
            total_earned += node.total_earned
        print(f"\nTotal XGold distributed: {total_earned:.2f}")

if __name__ == "__main__":
    sim = EnhancedSimulation(num_nodes=6)
    for cycle in range(5):
        sim.run_cycle(cycle + 1)
    sim.print_summary()