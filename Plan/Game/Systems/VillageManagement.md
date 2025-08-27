# Village Management: Passive Management and Island Development

## Description
The game takes place on a [flying island](../../Game/Entities/Island.md) that serves as the main hub and operational base. The core mechanic is the passive management of its inhabitants.

## Associated Concepts
## Passive Character Management
The core of the game is managing [Characters](../Entities/Character.md) indirectly. The player acts as a village overseer, making high-level decisions that the characters then execute autonomously based on a set of rules.

- **The Management Board**: This is the primary UI for passive management. From this screen, the player can:
  - Assign or change a character's [Role](../Gameplay/Roles.md).
  - Set production priorities for each building (e.g., telling the Forge to prioritize crafting swords over armor).
  - View the current status and needs of all characters.

- **Task Queues & Priorities**: Characters decide their actions based on a priority system.
  1.  **Needs**: Fulfilling personal needs (eating, sleeping) always comes first.
  2.  **Assigned Role**: A character will automatically find their assigned job building and begin work.
  3.  **Building Priority**: They will work on tasks based on the priority set by the player in the Management Board.
  4.  **Idle Behavior**: If a character has no pressing needs and no work to do, they will wander, socialize, or perform minor upkeep, which provides a small boost to village morale.

- **Schedules & The Day-Night Cycle**: Character behavior is tied to the [Day-Night Cycle](../Gameplay/DayNightCycle.md). They work during the day and return to their homes to rest at night, automatically managing their own stamina.
- **Population Management**: The player must make strategic decisions regarding the composition of their population, in particular by determining the "Job ratio" for newcomers. For example, an early development phase might require a higher ratio of basic [resource](../Entities/Resources/Resource.md) gatherers (wood, stone), while a later phase would focus on skilled artisans (alchemists, blacksmiths). This crew management mechanic adds a layer of depth beyond simple construction and collection.
- **Production Chains**: The table below illustrates the relationship between roles, [buildings](../../Game/Village/Entities/Building.md), and [resources](../../Game/Entities/Resource.md), offering a structured view of the production chains.

| Role | Associated Building | Resources Produced | Dependencies & Synergies |
|---|---|---|---|
| Lumberjack | Forest | Wood | Consumption by the forge and constructions |
| Miner | Mine | Minerals | Essential for the forge |
| Cook | Kitchen | Food, Boosts | Required to supply the kitchen and produce temporary boosts |
| Blacksmith | Forge | Equipment, Alloys | Requires wood, minerals, and unique resources |
| Alchemist | Alchemy Lab | Pills, Active Principles | Requires exploration resources for the creation of pills |

## Related Entities
- [Flying Island](../Entities/Island.md)
- [Character](../Entities/Character.md)
- [Building](../Entities/Building.md)
e resources |
| Alchemist | Alchemy Lab | Pills, Active Principles | Requires exploration resources for the creation of pills |

## Related Systems
- [Village Management](../../Game/Village/Systems/VillageManagement.md)

## Related Documents
- [Village Management](../../GameDesign/VillageManagement.md)
