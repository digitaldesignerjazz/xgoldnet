# Performance Metrics and Reward Allocation

## Key Performance Metrics

### Infrastructure Metrics
- Uptime percentage
- Bandwidth contributed (GB relayed)
- Number of successful peer connections
- Latency to key nodes/regions

### Harvesting-Specific Metrics
- Volume of harvesting claims submitted and accepted
- Quality score of contributed data (for prototype/sensor harvesting)
- Participation in Nexus-assigned special harvesting tasks

### Bonus Metrics
- Running AI agent workloads that contribute to network intelligence
- Geographic coverage contribution
- Participation in prototype data harvesting (Soilnova, etc.)

## Reward Allocation Model

### Base Reward
```
BaseReward = f(Uptime, Bandwidth, Connections) × XGoldRate
```

### Performance Multipliers
- High uptime and low latency → multiplier > 1.0
- Consistent high-quality harvesting claims → bonus multiplier
- Special task completion → significant bonus

### Dynamic Adjustment
Nexus continuously evaluates overall network health and adjusts base rates and multipliers to optimize harvesting efficiency and fairness.

## Distribution
- Rewards distributed periodically (e.g., daily or per epoch)
- Can be claimed in XGold or bridged to other layers (NovaRune, XCoin)
- Slashing applied for poor performance or false reporting