# Harvesting Protocols and Node Requirements

## Overview
XGoldNet defines specific protocols that allow mesh nodes to participate in value harvesting and earn XGold.

## Core Harvesting Protocols

### 1. Node Registration Protocol
- Nodes must register with a unique identity (linked to operator key)
- Stake or bond a minimum amount of NovaRune or XGold to participate
- Provide metadata (location, capacity, capabilities)

### 2. Contribution Reporting Protocol
- Periodic heartbeats reporting uptime, bandwidth contributed, and peer connections
- Event-based reporting for high-value relays or special tasks

### 3. Harvesting Claim Protocol
- Nodes submit harvesting claims based on verified contribution
- Claims are validated by Nexus or peer consensus
- Successful claims result in XGold distribution

## Node Requirements

### Minimum Requirements
- Stable connection to xMesh/NovaNet
- Minimum uptime threshold (e.g., 90%)
- Ability to run lightweight harvesting client/agent
- Integration with Nexus for task reception and reporting

### Recommended Capabilities
- Support for high-bandwidth relays
- Geographic diversity (for network resilience)
- Ability to run AI agent workloads for bonus harvesting
- Participation in prototype data collection (e.g., Soilnova sensors)

## Security Considerations
- Proof of contribution to prevent sybil attacks
- Slashing for malicious or false reporting
- Nexus as trusted oracle for performance validation