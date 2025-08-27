# Aethelgard Game Plan

This directory contains the central design and systems documentation for the game Aethelgard. The plan is organized into three main categories: core game design concepts, game entities, and game systems.

## Core Game Design

High-level documents that define the overall vision and architecture of the game.

- **[Architecture and UI](./Game/Design/ArchitectureAndUI.md)**: Outlines the technical architecture, camera controls, and user interface design.
- **[Art Style Guide](./Game/Design/StyleGuide.md)**: Defines the visual style as 2D isometric colorful pixel art.

## Game Entities

These documents describe the core objects and items that exist within the game world.

- **[Character](./Game/Entities/Character.md)**: The player-controlled characters who can be assigned roles.
- **[Flying Island](./Game/Entities/Island.md)**: The player's central hub and base of operations.
- **[Territory](./Game/Entities/Territory.md)**: Explorable locations that provide resources.
- **[Building](./Game/Entities/Building.md)**: Structures that enable production and new game mechanics.
- **[Equipment](./Game/Entities/Equipment.md)**: Procedurally generated items crafted by the player.
- **[Resource](./Game/Entities/Resources/Resource.md)**: Materials used for crafting, building, and progression.
- **[Ingredient](./Game/Entities/Ingredient.md)**: Components used in Alchemy and Smithing.
- **[WoodLog](./Game/Entities/WoodLog.md)**: A basic collectible resource.

## Game Systems

These documents detail the primary mechanics and gameplay loops.

- **[Village Management](./Game/Systems/VillageManagement.md)**: The core system for managing characters, roles, and production chains.
- **[Exploration](./Game/Systems/Exploration.md)**: The system for discovering new territories and resources.
- **[Progression](./Game/Systems/Progression.md)**: Details the tier-based progression system driven by Energy accumulation.
- **[Progression System Design](./Game/Systems/ProgressionSystem.md)**: The high-level design of the progression system.
- **[Crafting](./Game/Systems/Crafting.md)**: The system for creating equipment and consumables.
- **[Alchemy and Smithing](./Game/Systems/AlchemyAndSmithing.md)**: The high-level design of the crafting systems.
- **[Camera Control](./Game/Systems/CameraControl.md)**: Manages the 2D isometric camera.
