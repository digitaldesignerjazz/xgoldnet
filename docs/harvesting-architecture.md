# Unified Harvesting Architecture: XGoldNet + XGold + Nexus

## Overview

This document describes how the harvesting system works across multiple layers of the ecosystem.

## Core Components

### 1. XGoldNet (Harvesting Network)
- Runs on top of xMesh / NovaNet
- Nodes register, report metrics, and submit harvesting claims
- Uses `HarvestingClient` to interact with Nexus
- Handles performance tracking, special tasks, and slashing

### 2. Nexus (Central Orchestrator)
- Validates performance reports and harvesting claims
- Assigns special high-value harvesting tasks
- Dynamically adjusts reward parameters
- Acts as the trusted oracle for the harvesting economy

### 3. XGold (Token Layer)
- Rewards are minted based on validated claims from XGoldNet
- Contains emission schedule and reward calculation logic
- Can bridge rewards to other layers (NovaRune, XCoin, etc.)

## Data Flow

1. Mesh Node (via HarvestingClient) 
   → Reports metrics to Nexus
2. Nexus 
   → Validates performance and assigns special tasks
3. Node 
   → Submits HarvestClaim (signed)
4. Nexus 
   → Validates claim → Approves or slashes
5. XGold Layer 
   → Mints reward based on approved claim + reputation
6. Node 
   → Receives XGold (or bridged value)

## Key Interactions

- **Nexus ↔ XGoldNet**: Task assignment, claim validation, dynamic parameters
- **XGoldNet ↔ XGold**: Validated claims trigger reward minting
- **Nexus ↔ XGold**: Can influence emission rates based on overall network health

## Design Principles

- Nexus is the single source of truth for validation and orchestration
- XGoldNet focuses on mesh-native harvesting mechanics
- XGold focuses on token economics and reward distribution
- Modular design allows independent evolution of each layer

## Future Extensions
- On-chain claim validation (when NovaCoin or XCoin has smart contracts)
- Cross-layer reward bridging
- Reputation as a portable score across the ecosystem
- Integration with prototype data harvesting (Soilnova, etc.)