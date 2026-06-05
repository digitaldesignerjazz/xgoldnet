# XGoldNet Harvesting Client

This directory contains the harvesting client for XGoldNet.

## Purpose

The harvesting client allows mesh nodes to participate in the XGold harvesting economy by:
- Registering with the network
- Reporting contribution metrics
- Submitting harvesting claims
- Receiving XGold rewards

## Components

- `harvesting_client.py` — Main client logic (pseudocode)
- `metrics_collector.py` — Responsible for gathering performance data from the mesh
- `protocol_messages.py` — Message formats used for communication with Nexus and other nodes

## How to Run (Conceptual)

```bash
python harvesting_client.py
```

The client connects to:
- The local xMesh/NovaNet stack
- The Nexus orchestrator endpoint

## Next Steps for Implementation

- Replace pseudocode with real implementations
- Add proper error handling and retry logic
- Integrate with actual mesh metrics APIs
- Add cryptographic signing for claims and reports
- Implement secure communication with Nexus