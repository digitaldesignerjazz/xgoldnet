# Persistent + Visual XGoldNet Harvesting Simulation

# Features:
# - Persistence: Saves and loads node states using JSON
# - Visualization: Text-based charts and trends
# - Integrated with XGold reward logic

 import json
 import os
 import random
 from dataclasses import dataclass, asdict
 from typing import Dict

DATA_FILE = "simulation_data.json"

@dataclass
class NodeState:
    node_id: str
    reputation: float = 75.0
    total_earned: float = 0.0
    stake: float = 100.0
    tasks_completed: int = 0

class PersistentVisualSimulation:
    def __init__(self, num_nodes: int = 6, load_existing: bool = True):
        self.nodes: Dict[str, NodeState] = {}
        self.cycle = 0
        self.history = []  # For visualization trends

        if load_existing and os.path.exists(DATA_FILE):
            self._load_state()
        else:
            for i in range(num_nodes):
                self.nodes[f"node_{i}"] = NodeState(node_id=f"node_{i}")

    def _save_state(self):
        data = {
            "cycle": self.cycle,
            "nodes": {k: asdict(v) for k, v in self.nodes.items()}
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def _load_state(self):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        self.cycle = data.get("cycle", 0)
        for nid, ndata in data["nodes"].items():
            self.nodes[nid] = NodeState(**ndata)

    def _calculate_reward(self, bandwidth: float, reputation: float, special_tasks: int):
        base = bandwidth * 0.75
        rep_bonus = reputation * 0.25
        special_bonus = special_tasks * 20
        return round(base + rep_bonus + special_bonus, 2)

    def run_cycle(self):
        self.cycle += 1
        print(f"\n=== Cycle {self.cycle} ===")
        cycle_earnings = {}

        for node_id, node in self.nodes.items():
            uptime = random.uniform(0.76, 1.0)
            bandwidth = random.uniform(12, 160)

            if uptime > 0.82:
                reward = self._calculate_reward(bandwidth, node.reputation, 0)
                node.total_earned += reward
                node.reputation = min(100.0, node.reputation + 1.0)
                cycle_earnings[node_id] = reward
                print(f"  {node_id}: +{reward:.2f} XGold | Rep: {node.reputation:.1f}")
            else:
                slash = 4.0
                node.stake -= slash
                node.reputation = max(0.0, node.reputation - 7)
                print(f"  {node_id}: SLASHED {slash} | Rep: {node.reputation:.1f}")

            # Special task chance
            if random.random() > 0.78:
                bonus = random.uniform(25, 90)
                node.total_earned += bonus
                node.tasks_completed += 1
                node.reputation = min(100.0, node.reputation + 4)
                print(f"  {node_id}: SPECIAL TASK +{bonus:.2f} bonus!")

        self.history.append(cycle_earnings)
        self._save_state()

    def visualize(self):
        print("\n========== VISUALIZATION ==========")
        print("Total Earned per Node:")
        for nid, node in sorted(self.nodes.items()):
            bar = "█" * int(node.total_earned / 20)
            print(f"{nid}: {bar} {node.total_earned:.2f} XGold")

        print("\nReputation Trend (last 5 cycles):")
        for nid in self.nodes:
            recent = [h.get(nid, 0) for h in self.history[-5:]]
            if recent:
                trend = " ".join([f"{v:.0f}" for v in recent])
                print(f"{nid}: {trend}")

    def print_summary(self):
        print("\n========== FINAL SUMMARY ==========")
        total = sum(n.total_earned for n in self.nodes.values())
        for nid, node in self.nodes.items():
            print(f"{nid}: Earned={node.total_earned:.2f} | Rep={node.reputation:.1f} | Tasks={node.tasks_completed}")
        print(f"\nTotal XGold distributed: {total:.2f}")

if __name__ == "__main__":
    sim = PersistentVisualSimulation(num_nodes=5, load_existing=True)
    for _ in range(3):
        sim.run_cycle()
    sim.visualize()
    sim.print_summary()