# Aethelgard Game Plan

This directory contains the central design and systems documentation for Aethelgard. The plan is organized into clear categories, with all documents heavily interlinked.

## Core Game Design
High-level documents that define the game's vision and architecture.
- **[Architecture and UI](./Game/Design/ArchitectureAndUI.md)**: Outlines the technical architecture, camera, and UI.
- **[Art Style Guide](./Game/Design/StyleGuide.md)**: Defines the 2D isometric pixel art style.

## Core Gameplay Mechanics
Documents detailing the dynamic elements of the game.
- **[Day-Night Cycle](./Game/Gameplay/DayNightCycle.md)**: Describes how the time of day affects gameplay.
- **[Events](./Game/Gameplay/Events.md)**: Details the random and scheduled events that can occur.
- **[Roles and Professions](./Game/Gameplay/Roles.md)**: A detailed breakdown of all character jobs and skills.

## Game Entities
Descriptions of the core objects and items in the game world.
- **[Character](./Game/Entities/Character.md)**: Details on character attributes, needs, and skills.
- **[Flying Island](./Game/Entities/Island.md)**: The player's tile-based, expandable central hub.
- **[Building](./Game/Entities/Building.md)**: The main document for building concepts.
  - **[Specific Buildings](./Game/Entities/Buildings/)**: A directory with detailed documents for each building, like the **[Forge](./Game/Entities/Buildings/Forge.md)** and **[Alchemy Lab](./Game/Entities/Buildings/AlchemyLab.md)**.
- **[Equipment](./Game/Entities/Equipment.md)**: Procedurally generated items.
- **[Resources](./Game/Entities/Resources/)**: A directory for all resources.
  - **[Resource](./Game/Entities/Resources/Resource.md)**: The main document for resource concepts.
  - **[Wood](./Game/Entities/Resources/Wood.md)**: A basic collectible resource.
- **[Ingredient](./Game/Entities/Ingredient.md)**: Components used in crafting.
- **[Territory](./Game/Entities/Territory.md)**: Explorable locations.

## Game Systems
Documents detailing the primary mechanics and loops.
- **[Village Management](./Game/Systems/VillageManagement.md)**: The core system for managing characters and production.
- **[Exploration](./Game/Systems/Exploration.md)**: The system for discovering new territories.
- **[Progression](./Game/Systems/Progression.md)**: The tier-based progression system.
- **[Crafting](./Game/Systems/Crafting.md)**: The system for creating items.
- **[Camera Control](./Game/Systems/CameraControl.md)**: Manages the game's camera.