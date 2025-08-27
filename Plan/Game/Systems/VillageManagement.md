# Village Management: Passive Management and Island Development

## Description
The game takes place on a [flying island](../../Game/Entities/Island.md) that serves as the main hub and operational base. The core mechanic is the passive management of its inhabitants.

## Associated Concepts
- **Passive Management**: The player does not directly control the [characters](../../Game/Shared/Entities/Character.md), but assigns them roles or professions so that they automatically perform the tasks necessary for the proper functioning of the island. This mechanic is particularly suitable for mobile games, as it encourages player retention through short and regular sessions.
- **Population Management**: The player must make strategic decisions regarding the composition of their population, in particular by determining the "Job ratio" for newcomers. For example, an early development phase might require a higher ratio of basic [resource](../../Game/Entities/Resource.md) gatherers (wood, stone), while a later phase would focus on skilled artisans (alchemists, blacksmiths). This crew management mechanic adds a layer of depth beyond simple construction and collection.
- **Production Chains**: The table below illustrates the relationship between roles, [buildings](../../Game/Village/Entities/Building.md), and [resources](../../Game/Entities/Resource.md), offering a structured view of the production chains.

| Role | Associated Building | Resources Produced | Dependencies & Synergies |
|---|---|---|---|
| Lumberjack | Forest | Wood | Consumption by the forge and constructions |
| Miner | Mine | Minerals | Essential for the forge |
| Cook | Kitchen | Food, Boosts | Required to supply the kitchen and produce temporary boosts |
| Blacksmith | Forge | Equipment, Alloys | Requires wood, minerals, and unique resources |
| Alchemist | Alchemy Lab | Pills, Active Principles | Requires exploration resources for the creation of pills |

## Related Systems
- [Village Management](../../Game/Village/Systems/VillageManagement.md)

## Related Documents
- [Village Management](../../GameDesign/VillageManagement.md)
