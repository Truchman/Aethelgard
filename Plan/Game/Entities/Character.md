# Entity: Character

## Description
A character controlled by the user, living on the [flying island](../../Entities/Island.md). The user can recruit multiple characters and assign them roles to automate tasks.

## Associated Concepts
- **Roles**: Characters can be assigned various professions that determine their tasks and abilities, such as Lumberjack, Miner, Cook, Blacksmith, and Alchemist.
- **Progression**: Characters advance through tiers via the [Progression System](../../Systems/Progression.md).

## Related Systems
- [Village Management](../Systems/VillageManagement.md)
- [Progression System](../Systems/Progression.md)

## Technical Concepts
- **Components**:
  - **TransformComponent**: Manages the character's position, rotation, and scale.
  - **HealthComponent**: Manages the character's health points.
  - **SpriteComponent**: Manages the visual representation of the character.
  - **InputComponent**: Handles input from the user for direct control.
  - **PlayerControllerScript**: A script that defines the character's behavior.
