# Advanced Pseudocode: XGoldNet Harvesting Client (v2)

# This version includes:
# - Detailed claim validation logic
# - Slashing handling
# - Special task integration
# - Better structure and comments

class HarvestingClient:
    def __init__(self, node_id, nexus, mesh):
        self.node_id = node_id
        self.nexus = nexus
        self.mesh = mesh
        self.stake = 0.0
        self.reputation = 100.0
        self.history = []
        self.active_tasks = []

    # ------------------ Registration ------------------
    def register(self, metadata):
        result = self.nexus.register_node(self.node_id, metadata, self.stake)
        if result.success:
            self.stake = result.initial_stake
        return result.success

    # ------------------ Metrics & Reporting ------------------
    def collect_and_report_metrics(self):
        metrics = self.mesh.get_performance_metrics()
        report = {
            "node_id": self.node_id,
            "timestamp": now(),
            "uptime": metrics.uptime,
            "bandwidth_gb": metrics.bandwidth,
            "peers": metrics.peers,
            "latency": metrics.latency
        }
        self.history.append(report)
        self.nexus.submit_performance_report(report)

    # ------------------ Harvest Claim Logic ------------------
    def submit_harvest_claim(self):
        claim = self._generate_claim()
        validation = self.nexus.validate_harvest_claim(self.node_id, claim, self.reputation)

        if validation.status == "approved":
            self._credit_reward(validation.amount)
            self.reputation = min(100.0, self.reputation + 2)
        elif validation.status == "slashed":
            self._apply_slashing(validation.slash_percent)
        else:
            print("Claim pending or rejected:", validation.reason)

    def _generate_claim(self):
        recent = self.history[-30:] if self.history else []
        if not recent:
            return None

        total_bw = sum(r["bandwidth_gb"] for r in recent)
        avg_uptime = sum(r["uptime"] for r in recent) / len(recent)

        return {
            "period": "last_24h",
            "bandwidth_gb": total_bw,
            "avg_uptime": round(avg_uptime, 2),
            "special_tasks": len(self.active_tasks),
            "reputation": self.reputation
        }

    # ------------------ Slashing ------------------
    def _apply_slashing(self, percent):
        loss = self.stake * (percent / 100.0)
        self.stake -= loss
        self.reputation = max(0.0, self.reputation - 15)
        print(f"[SLASH] Lost {loss:.2f} stake. Reputation now: {self.reputation}")

    def _credit_reward(self, amount):
        print(f"[REWARD] +{amount} XGold credited")
        # TODO: Actual token credit or bridge call

    # ------------------ Special Tasks ------------------
    def check_for_special_tasks(self):
        tasks = self.nexus.get_available_special_tasks(self.node_id)
        for task in tasks:
            if self._can_handle_task(task):
                self.active_tasks.append(task)
                self.nexus.accept_task(self.node_id, task.id)

    def _can_handle_task(self, task):
        return task.difficulty <= (self.reputation / 20)  # simple capability check

    def complete_special_task(self, task_id):
        for task in self.active_tasks:
            if task.id == task_id:
                self.active_tasks.remove(task)
                bonus = task.bonus * 100
                self._credit_reward(bonus)
                self.reputation += 5
                return True
        return False

    # ------------------ Main Loop ------------------
    def run(self):
        print("Starting XGoldNet Harvesting Client...")
        self.register({"location": "Hannover", "type": "relay"})

        while True:
            self.collect_and_report_metrics()
            self.check_for_special_tasks()
            self.submit_harvest_claim()
            sleep(3600)  # hourly cycle


# Placeholder functions
def now(): pass
def sleep(seconds): pass