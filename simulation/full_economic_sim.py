# Full Economic XGoldNet + XGold Simulation

# Combines:
# - Persistence (JSON)
# - Text visualization (bars + supply trends)
# - Real XGold minting + supply tracking
# - Slashing and special tasks

 import json
 import os
 import random
 from dataclasses import dataclass, asdict
 from typing import List, Dict

DATA_FILE = "simulation_data.json"

@dataclass
class NodeState:
    node_id: str
    reputation: float = 75.0
    total_earned: float = 0.0
    stake: float = 100.0
    tasks_completed: int = 0

class XGoldLedger:
    """Tracks all XGold minting and supply."""
    def __init__(self):
        self.total_minted = 0.0
        self.mint_records: List[Dict] = []

    def mint(self, node_id: str, amount: float, reason: str = "harvesting", cycle: int = 0):
        self.total_minted += amount
        record = {
            "cycle": cycle,
            "node_id": node_id,
            "amount": amount,
            "reason": reason
        }
        self.mint_records.append(record)
        return record

    def get_stats(self):
        return {
            "total_minted": round(self.total_minted, 2),
            "total_mints": len(self.mint_records)
        }

class FullEconomicSimulation:
    def __init__(self, num_nodes: int = 6, load_existing: bool = True):
        self.nodes: Dict[str, NodeState] = {}
        self.cycle = 0
        self.xgold = XGoldLedger()
        self.history: List[Dict] = []

        if load_existing and os.path.exists(DATA_FILE):
            self._load()
        else:
            for i in range(num_nodes):
                self.nodes[f"node_{i}"] = NodeState(f"node_{i}")

    def _save(self):
        data = {
            "cycle": self.cycle,
            "nodes": {k: asdict(v) for k, v in self.nodes.items()}
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def _load(self):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        self.cycle = data.get("cycle", 0)
        for nid, ndata in data.get("nodes", {}).items():
            self.nodes[nid] = NodeState(**ndata)

    def _get_reward(self, bandwidth: float, reputation: float) -> float:
        return round(bandwidth * 0.75 + reputation * 0.25, 2)

    def run_cycle(self):
        self.cycle += 1
        print(f"\n=== Cycle {self.cycle} ===")
        cycle_total = 0.0

        for node_id, node in self.nodes.items():
            uptime = random.uniform(0.75, 1.0)
            bandwidth = random.uniform(10, 170)

            if uptime > 0.82:
                reward = self._get_reward(bandwidth, node.reputation)
                node.total_earned += reward
                node.reputation = min(100.0, node.reputation + 1.0)

                self.xgold.mint(node_id, reward, cycle=self.cycle)
                cycle_total += reward
                print(f"  {node_id}: +{reward:.2f} XGold | Rep: {node.reputation:.1f}")
            else:
                loss = 5.0
                node.stake -= loss
                node.reputation = max(0.0, node.reputation - 6)
                print(f"  {node_id}: SLASHED")

            if random.random() > 0.78:
                bonus = random.uniform(20, 80)
                node.total_earned += bonus
                node.tasks_completed += 1
                node.reputation += 3
                self.xgold.mint(node_id, bonus, reason="special_task", cycle=self.cycle)
                cycle_total += bonus
                print(f"  {node_id}: SPECIAL TASK +{bonus:.2f}")

        self.history.append({"cycle": self.cycle, "minted": cycle_total})
        self._save()

    def visualize(self):
        print("\n========== VISUALIZATION ==========")
        print("Total Earned:")
        for nid, node in sorted(self.nodes.items()):
            length = int(node.total_earned / 12)
            print(f"{nid}: {'█' * length} {node.total_earned:.2f}")

        print("\nXGold Minted per Cycle:")
        for h in self.history[-8:]:
            bar = '█' * int(h['minted'] / 8)
            print(f"Cycle {h['cycle']}: {bar} {h['minted']:.2f}")

    def print_summary(self):
        stats = self.xgold.get_stats()
        print("\n========== FINAL SUMMARY ==========")
        for nid, node in self.nodes.items():
            print(f"{nid}: Earned={node.total_earned:.2f} | Rep={node.reputation:.1f}")
        print(f"\nTotal XGold Minted: {stats['total_minted']}")
        print(f"Total Mints: {stats['total_mints']}")

if __name__ == "__main__":
    sim = FullEconomicSimulation(num_nodes=5, load_existing=True)
    for _ in range(5):
        sim.run_cycle()
    sim.visualize()
    sim.print_summary()