# Protocol Message Definitions for XGoldNet Harvesting

# These are example message structures used for communication
# between the harvesting client, Nexus, and other nodes.

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class NodeRegistration:
    node_id: str
    metadata: Dict[str, Any]
    stake_amount: float
    timestamp: str

@dataclass
class PerformanceReport:
    node_id: str
    timestamp: str
    uptime: float
    bandwidth_gb: float
    peer_count: int
    avg_latency_ms: float
    extra_data: Dict[str, Any] = None

@dataclass
class HarvestClaim:
    node_id: str
    period: str
    total_bandwidth: float
    avg_uptime: float
    special_tasks_completed: int
    reputation_score: float
    signature: str = None  # For future cryptographic signing

@dataclass
class SpecialTask:
    task_id: str
    task_type: str  # e.g. "region_coverage", "prototype_data_collection"
    difficulty: int
    bonus_multiplier: float
    description: str

@dataclass
class ClaimValidationResult:
    status: str  # "approved", "rejected", "slashed", "pending"
    amount: float = 0.0
    slash_percentage: float = 0.0
    reason: str = None