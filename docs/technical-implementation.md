# Technical Implementation on Existing Mesh Stack

## Overview
XGoldNet is designed to be built as an overlay on top of the existing xMesh / NovaNet infrastructure rather than requiring a completely new network stack.

## Implementation Approach

### 1. Protocol Layer
- Extend existing mesh protocols with harvesting-specific messages (registration, contribution reports, claim submissions)
- Lightweight client/agent that nodes can run alongside their mesh software

### 2. Nexus Integration
- Use existing Nexus communication channels (or extend them) for task assignment and performance reporting
- Leverage Nexus as the authoritative source for reward calculations and validation

### 3. Data Collection
- Nodes report standard mesh metrics (already available)
- Additional harvesting-specific metrics collected via lightweight agents
- Integration with prototype systems (e.g., Soilnova sensor data) for bonus harvesting

### 4. Reward Distribution
- Rewards calculated by Nexus
- Distribution handled via XGold token layer or bridged mechanisms
- Periodic settlement (daily/epoch-based)

## Technology Choices
- Python or Rust for harvesting client/agent
- Integration with existing Yggdrasil / xMesh tooling
- Event-driven architecture for real-time Nexus coordination

## Phased Rollout
1. Simulation and modeling using current Nexus instance
2. Testnet with volunteer nodes
3. Mainnet integration with NovaRune and XGold layers

## Open Questions
- Exact message formats for harvesting protocols
- Slashing and dispute resolution mechanisms
- Optimal reward frequency and claim process