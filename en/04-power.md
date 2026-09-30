# Chapter 4 — Off-Grid Power

[← Back to README](../README.md) | [中文](../zh/04-power.md)

In an AI-run world, the grid may not fail — it may be **selectively switched off**. Smart meters make it possible to cut power to a single house. Your goal: **keep the essentials running with zero grid connection.**

## 4.1 Decide what actually needs power

| Priority | Load | Typical daily need |
|---|---|---|
| 1 | LED lighting (a few bulbs, a few hours) | 20–50 Wh |
| 1 | Radio receiver, LoRa mesh node | 5–20 Wh |
| 1 | Charging batteries, headlamps | 20–50 Wh |
| 2 | Water pump (DC), small fan | 100–300 Wh |
| 3 | Small DC fridge | 300–600 Wh |
| ✗ | Electric heating, AC, oven | Forget it off-grid on a budget |

A realistic "essentials" budget is **100–300 Wh per day**. That's cheap.

## 4.2 Budget systems

| Level | Kit | Approx. cost |
|---|---|---|
| **Pocket** | Hand-crank radio/light, 2–3 USB power banks, AA/AAA NiMH batteries + solar charger | $50–150 |
| **Room** | 100–200 W folding solar panel + 0.5–1 kWh LiFePO₄ "power station" | $300–800 |
| **House** | 400–800 W panels + 2–5 kWh LiFePO₄ battery + charge controller + inverter | $1,500–4,000 |

**Why LiFePO₄ (lithium iron phosphate):** thousands of cycles, much lower fire risk than other lithium chemistries, no maintenance.

## 4.3 Keep it *independent*

This matters more than capacity:

- **Disable cloud features.** Many power stations, inverters and batteries have Wi-Fi/Bluetooth apps and remote firmware updates. Buy models that **work fully offline**, and keep them offline.
- **Don't grid-tie your backup.** A grid-tied solar system shuts off when the grid goes down (anti-islanding), and its smart inverter can be controlled remotely. Keep a separate, standalone system.
- **Prefer "dumb" components**: manual switches, analog charge controllers, standard connectors (Anderson, XT60, 12 V "cigarette").
- **Store spares**: fuses, cables, a multimeter, a second charge controller.
- **EMP/Faraday storage** for spare electronics: a sealed metal ammo can or galvanized trash can with a lid, items insulated from the metal with cardboard. Test with a phone inside — if it rings, it's not sealed.

## 4.4 Non-electric energy

The most resilient energy doesn't need electricity at all:

- **Heat:** wood stove (with chimney, CO alarm), wool clothing, sleeping in one warm room
- **Cooking:** rocket stove, solar oven, "haybox" retained-heat cooker (saves ~50% fuel) — **outdoors or properly vented only**
- **Light:** daylight schedules; go to bed early
- **Mechanical:** hand tools, bicycles, hand-crank grain mills, manual washing (plunger + bucket)

## 4.5 Fuel cautions

- Generators are loud, thermal-visible, fuel-hungry, and a leading cause of post-disaster **carbon monoxide deaths**. Run them only outdoors, >6 m (20 ft) from windows and doors.
- Stored gasoline degrades in months without stabilizer; propane stores indefinitely.

Next: [Chapter 5 — Off-Grid Communications →](05-comms.md)
