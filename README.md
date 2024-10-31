# **time-space-python-text-game**

> [!NOTE]
>
> # Ideas
>
> - [ ] Create various rooms with different weather conditions.
> - [ ] Attack system: elemental cards
>   - Elements: Physic, Fire, Ice and Light
>   - Random card choice with better chances at higher levels of magic
>   - Mana points for elemental cards, not for physic attacks
>   - ULTIMATE _**I chose my destiny**_: grants card choice 1 time per room
> - [ ] Enemies drops: coins and xp
> - [ ] Character Skills: Health, magic, agility and speech

> [!WARNING] > [ ] Need to balance mob weaknesses and resistances

<!-- CONTENT SECTION -->

## Contents

[Rooms](#rooms) -
[Main Character](#main-character) -
[Enemies](#enemies) -
[Items](#items) -
[NPCs](#npcs)

<!-- ROOMS SECTION-->
<details>
<summary>Rooms</summary>

# Rooms

- [x] START:
- [x] END:
  - [x] Opened by condition (key, lever or RoomClear)
- [x] GENERAL:
  - [x] Snow:
  - [x] Sand:
  - [x] Cave:
  - NPCs: [Merchant](#merchant) and [Fortune Teller](#fortuneteller)
  - [x] Empty room:
  - NPCs: Merchant
  </details>

<!-- CHARACTER SECTION -->
<details>
<summary>Main Character</summary>

## Main Character

### Stats

> Given points initially 5

- Health (1-5): 5 life points pr/upgrade
- Agility (1-3): Enchances chances of avoid attacks and getting off fights
- Magic (1-5): Increases chances of card choice
- Speech (1-3): Increases chances on trading and conversations with NPCs

</details>

<!-- ENEMIES SECTION -->
<details>
<summary>Enemies</summary>

## Enemies

- Bandits
  - **Weaknesses**: Fire
  - **Resistances**: Light
- Skeletons
  - **Weaknesses**: Light
  - **Resistances**: Physical
- Ice monsters
  - **Weaknesses**: Fire
  - **Resistances**: Ice, Physical
- Zombies
  - **Weaknesses**: Fire
  - **Resistances**: None
  </details>

<!-- ITEMS SECTION -->
<details>
<summary>Items</summary>

## Items

- Torch
- Sword
- Shield
- Backpack
- Greatsword
- Bow and Arrows

</details>

<!-- NPCs SECTION -->
<details>
<summary>NPCs</summary>

## NPCs

- ### Merchant
- ### Fortune Teller
</details>

> [!NOTE]
>
> # ToDo LIST
>
> Finished NEED TO improve story
>
> 1. [x] Virtual environment Creation
> 1. [x] Character Creation
> 1. [x] Saving Files
>    1. [x] Character
>    1. [x] Map and rooms
>    1. [x] Stats
>    1. [x] Mobs
> 1. [x] Map Creation
> 1. [x] Movement Development
> 1. [x] WIN conditions
> 1. [x] Mob Creation
> 1. [x] Character Stats
> 1. [x] Fight Development
>    1. [x] Elements
>    1. [x] Ultimate
> 1. [x] LOSE conditions

You can recreate the environment with

```
mkdir my_new_project          # Create a new project directory
cd my_new_project             # Navigate into the directory
python -m venv venv           # Create a virtual environment
.\venv\Scripts\activate        # Activate on Windows
# or
source venv/bin/activate      # Activate on macOS/Linux
pip install -r requirements.txt # Install dependencies
pip freeze                    # Verify installation (optional)
deactivate                    # Deactivate when done
```
