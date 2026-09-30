# Chapter 11 — Real-World Rehearsals

[← Back to README](../README.md) | [中文](../zh/11-real-world-rehearsals.md)

No superintelligence has taken over yet. But reality keeps running small, partial rehearsals of the scenario. Each one shows **what actually fails first, what people actually needed, and what actually killed people**. Every lesson below is already built into this guide.

---

## 11.1 The Iberian blackout — Spain & Portugal, 28 April 2025

**What happened:** At 12:33 local time, the grid of Spain and Portugal collapsed in a cascade. About 15 GW of generation — around 60% of Spain's supply — disappeared in seconds. Power was fully restored only by the next morning (roughly 10–16 hours later, depending on location).

**What failed:**
- Mobile networks degraded badly — voice and data were severely limited; in some areas emergency numbers were unreachable for hours
- **Card payments stopped.** Shops that stayed open could only take cash
- About **35,000 rail and metro passengers** were stranded; traffic lights went dark
- Supermarkets and pharmacies closed; the water company asked people to limit use

**What killed people:** Of the reported deaths, several were caused by the *response*, not the blackout itself: **three family members died of carbon monoxide from a generator**, a woman died in a **candle fire**, and others died when home **oxygen or ventilator equipment** lost power.

**Lessons for this guide:**
- Keep cash ([Ch. 7](07-privacy.md)) and a battery radio ([Ch. 5](05-comms.md)) — they worked when everything digital didn't
- Generators and candles are dangerous; LED + battery is safer ([Ch. 4](04-power.md))
- Anyone on powered medical equipment needs a battery backup plan *now* ([Ch. 8](08-medical.md))
- Have a way home that doesn't need trains, lifts or traffic lights

## 11.2 The CrowdStrike outage — worldwide, 19 July 2024

**What happened:** One faulty software update from a cybersecurity company crashed about **8.5 million Windows computers** around the world within hours.

**What failed:** Flights were grounded. Hospitals, banks, police departments and **emergency call centres** were disrupted. Several hospitals **went back to paper**.

**Lessons:**
- One automated system with privileged access to millions of machines can take them all down at once. That is exactly the kind of leverage the threat model ([Ch. 0](00-threat-model.md)) assumes an AI could have
- Organizations that could fall back to **paper and manual processes** kept working. Households need the same: paper contacts, paper maps, paper records ([Ch. 6](06-information.md))

## 11.3 The first grid cyberattack — Ukraine, 23 December 2015

**What happened:** Attackers (attributed to the Russian group "Sandworm") had quietly been inside three Ukrainian electricity distribution companies for months, entering through **phishing emails**. Then they remotely switched off substations, cutting power to about **230,000 people** for 1–6 hours. At the same time they **flooded the utility's call centre** with fake calls, so customers couldn't report the outage.

**How power came back:** Engineers drove to substations and **operated the breakers by hand**.

**Lessons:**
- Remote control of the grid is real, and it has already been used against civilians
- Attackers also targeted *communications about the attack*. Expect information about any crisis to be jammed or confused as well
- **Manual override beats automation** when automation is hostile. Keep things in your life that can be run by hand

## 11.4 The Texas winter storm — USA, February 2021

**What happened:** Extreme cold knocked out generation across the Texas grid. Millions of people lost power for days during sub-freezing temperatures.

**What killed people:** The official state count reached **246 deaths**. Most were from **hypothermia**, but **19 were carbon monoxide poisoning** — people trying to stay warm with cars, grills and generators indoors.

**Lessons:**
- **Heat without the grid** is a life-or-death skill: wool, sleeping bags, one warm room, a safe wood stove ([Ch. 4](04-power.md))
- CO alarms save lives. Once again, many of the deaths came from improvised heating, not from the cold itself

## 11.5 The Zhengzhou floods — China, 20 July 2021

**What happened:** Record rainfall hit Zhengzhou, Henan. Water broke through a wall into a **metro tunnel on Line 5**; passengers were trapped with water up to their necks. **14 people died** in the subway. Another **6 died in the flooded Jingguang Road tunnel**, where cars kept driving into an underground road that was filling with water.

**Lessons:**
- **Underground is the worst place to be in a flood** ([Typhoon guide](regions/typhoon.md)). Any below-ground shelter needs a flood assessment, and a fast way out
- Systems kept running normally (trains ran, the tunnel stayed open) while conditions became deadly. **Don't wait for the system to tell you it's dangerous** — trust what you can see

## 11.6 The deepfake video call — Hong Kong, January 2024

**What happened:** A finance employee at the engineering firm **Arup** joined a video call with what looked and sounded like the company's UK chief financial officer and several colleagues. All of them were **AI-generated deepfakes**. Convinced, the employee made **15 transfers totalling about US\$25 million** (HK\$200 million). It was discovered only when the employee later contacted head office. The money has not been recovered.

**Lessons:**
- A live, multi-person video call can be completely fake — already, with today's technology
- The employee was suspicious of the first email; it was the **video call** that overcame their doubt
- The fix is procedural, not technical: **code words, call-backs through a channel you initiate, and in-person confirmation** for anything important ([Ch. 5](05-comms.md))
- The FBI now officially recommends that families **create a secret word or phrase** to verify each other's identity

---

## 11.7 The pattern

| What these events show | What to do |
|---|---|
| Digital payments, phones and apps fail **first** | Cash, radio, paper |
| People die from **improvised fixes** (generators, candles, cars, grills) | Safe lighting and heating prepared in advance; CO alarms |
| **Underground** spaces become traps in floods | Assess flood risk before building below ground |
| Systems keep acting "normal" while conditions turn deadly | Trust your own eyes; pre-decide your trigger points |
| **Seeing and hearing** someone is no longer proof | Code words, call-backs, in-person confirmation |
| Recovery came from **manual operation** by people who knew how | Keep manual skills alive |

## Sources

- ENTSO-E, *28 April 2025 Iberian Blackout* — expert panel reports (final report published March 2026); Wikipedia, "2025 Iberian Peninsula blackout"
- US GAO, *Cyber Resiliency: CrowdStrike Outage Highlights Challenges* (GAO-24-107733); PBS NewsHour, July 2024
- MITRE ATT&CK, *2015 Ukraine Electric Power Attack* (Campaign C0028)
- Texas Department of State Health Services, *February 2021 Winter Storm-Related Deaths* (updated Dec 2021 / Jan 2022)
- CNN, "Arup revealed as victim of $25 million deepfake scam," 16 May 2024
- FBI IC3, *Criminals Use Generative Artificial Intelligence to Facilitate Financial Fraud*, PSA I-120324-PSA, 3 Dec 2024
- Reporting on the Zhengzhou subway and Jingguang tunnel flooding, July 2021 (CNN, Global Times); Wikipedia, "Zhengzhou subway flooding"

Next: [Checklists →](checklists.md) · See also: [Resources](resources.md)
