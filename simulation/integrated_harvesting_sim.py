# Integrated XGoldNet + XGold Harvesting Simulation

# This simulation connects harvesting claims directly to the XGold reward system.

 import random
 from dataclasses import dataclass

# Import from xgold rewards (in real project this would be proper import)
# For simulation we include a simplified version here

class SimpleXGoldEmission:
    def calculate_harvest_reward(self, claim, reputation):
        base = claim.get('bandwidth_gb', 0) * 0.75
        rep_bonus = reputation * 0.25
        special_bonus = claim.get('special_tasks', 0) * 20
        return round(base + rep_bonus + special_bonus, 2)

    def process_validated_claim(self, node_id, claim, reputation):
        reward = self.calculate_harvest_reward(claim, reputation)
        print(f"  [XGold] Minted {reward} XGold for {node_id}")
        return reward

@dataclass
class Node:
    node_id: str
    reputation: float = 75.0
    total_earned: float = 0.0

class IntegratedSimulation:
    def __init__(self, num_nodes=5):
        self.nodes = {f"node_{i}": Node(f"node_{i}") for i in range(num_nodes)}
        self.xgold = SimpleXGoldEmission()
        self.cycle = 0

    def run_cycle(self):
        self.cycle += 1
        print(f"\n=== Cycle {self.cycle} ===")

        for node_id, node in self.nodes.items():
            # Simulate node performance
            uptime = random.uniform(0.78, 1.0)
            bandwidth = random.uniform(15, 150)

            claim = {
                "bandwidth_gb": round(bandwidth, 1),
                "avg_uptime": round(uptime, 2),
                "special_tasks": 0
            }

            # Simulate Nexus validation
            if uptime > 0.85:
                reward = self.xgold.process_validated_claim(node_id, claim, node.reputation)
                node.total_earned += reward
                node.reputation = min(100.0, node.reputation + 1.2)
            else:
                # Simple slashing simulation
                loss = 5.0
                node.reputation = max(0.0, node.reputation - 6)
                print(f"  {node_id}: SLASHED (low uptime)")

            # Occasional special task
            if random.random() > 0.8:
                bonus = random.uniform(30, 80)
                node.total_earned += bonus
                node.reputation += 4
                print(f"  {node_id}: Completed special task! +{bonus} bonus XGold")

    def print_final_stats(self):
        print("\n========== FINAL STATISTICS ==========")
        total = 0
        for nid, node in self.nodes.items():
            print(f"{nid}: Earned = {node.total_earned:.2f} XGold | Reputation = {node.reputation:.1f}")
            total += node.total_earned
        print(f"\nTotal XGold minted this run: {total:.2f}")

if __name__ == "__main__":
    sim = IntegratedSimulation(num_nodes=6)
    for _ in range(4):
        sim.run_cycle()
    sim.print_final_stats()