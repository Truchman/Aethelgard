# Entity: WoodLog

## Description
A log of wood that can be collected by the player. It's a [resource](./Resource.md) item.

## Associated Concepts
- **Collection**: Can be gathered by [characters](./Character.md) with the Lumberjack role.

## Related Systems
- [Village Management](../Village/Systems/VillageManagement.md)

## Technical Concepts
- **Components**:
  - **TransformComponent**: Manages the log's position, rotation, and scale.
  - **SpriteComponent**: Manages the visual representation of the log.
  - **ResourceComponent**: Defines the log as a resource that can be collected.
