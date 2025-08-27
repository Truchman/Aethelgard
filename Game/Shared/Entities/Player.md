# Entity: Player

## Description
The main character controlled by the user.

## Components
- **TransformComponent**: Manages the player's position, rotation, and scale in the game world.
- **HealthComponent**: Manages the player's health points (PV).
- **SpriteComponent**: Manages the visual representation of the player (the sprite).
- **InputComponent**: Handles input from the player (keyboard, mouse, gamepad).
- **PlayerControllerScript**: A script that defines the player's behavior.

## Assets
- **Sprite**: `Assets/Sprites/Player/player.png`
- **Animations**:
  - `Assets/Animations/Player/idle.anim`
  - `Assets/Animations/Player/walk.anim`
  - `Assets/Animations/Player/run.anim`