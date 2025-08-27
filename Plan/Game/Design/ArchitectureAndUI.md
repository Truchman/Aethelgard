# Technical Architecture and User Interface (UI)

## Description
This document outlines the technical architecture and user interface design for Aethelgard.

## Associated Concepts
- **Art Style**: The game's art style is [2D isometric pixel art](../Art/StyleGuide.md).
- **Camera**: The game uses a fixed 2D isometric camera. Camera controls are touch-friendly.
  - **Zoom**: Zooming is handled by adjusting the camera's `orthographicSize` property. Players can zoom out to see nearby opportunities, the sector map, or the region map. Zooming is controlled by the mouse scroll wheel or pinch gestures.
  - **Recentering**: A button allows the player to recenter the view on the main character.
- **UI**: The UI is designed to be simple and intuitive.
  - **Main HUD**: Key camp information is displayed at the top of the screen, with main menu buttons at the bottom.
  - **Contextual Menus**: Building and character menus are accessed by clicking directly on the entity or through a general menu.
- **Island Movement**: The movement of the [island](../Entities/Island.md) is not instantaneous.

## Related Systems
- [Camera Control](../Systems/CameraControl.md)