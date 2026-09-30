# Chapter 5 — Off-Grid Communications

[← Back to README](../README.md) | [中文](../zh/05-comms.md)

If the AI controls the phone network, **every call can be heard, faked or cut**. You need ways to talk that don't pass through its systems — and ways to verify that the person talking is real.

## 5.1 Principles

1. **Local first.** Most coordination that matters is within 1–20 km.
2. **Assume interception.** Any radio can be heard by anyone listening. Radio gives you *independence*, not *secrecy*.
3. **Verify identity, not just content.** A perfect voice clone is trivial for a superintelligence.
4. **Have a plan that works with zero technology.**

## 5.2 The communication ladder

| Tool | Range | Needs licence? | Notes |
|---|---|---|---|
| **Face to face / notes** | Walking distance | No | Most secure. Nothing to intercept remotely. |
| **Couriers & dead drops** | Anywhere you can walk or cycle | No | Slow, reliable. A pre-agreed spot to leave paper messages. |
| **FRS walkie-talkies** (US) / **PMR446** (EU) | 0.5–3 km | No | Cheap. Buy in a set, practise. |
| **GMRS** (US) | 2–30 km with repeaters | Licence (no exam in US) | More power, repeaters. |
| **CB radio** | 5–30 km (sometimes far more) | Usually no | Old, cheap, widely owned. |
| **Meshtastic / LoRa mesh** | 1–10+ km per hop, multi-hop | No (licence-free ISM bands) | ~$30–60 devices, text messages, no internet or cell network, runs for days on battery/solar. Great for a neighbourhood. |
| **Amateur (ham) radio** | Local to worldwide (HF) | Yes, exam required | The most capable option. Get licensed *now*; join a local club and emergency net. In many countries, encryption is not permitted on ham bands. |
| **Shortwave / AM receiver** | Worldwide (listen only) | No | Hear broadcasts from other regions/countries — useful to cross-check news. |

## 5.3 Build a neighbourhood mesh

A Meshtastic network needs no tower and no company:

1. Buy 3–5 LoRa devices for your group (use the correct frequency band for your country).
2. Put one **high up** (rooftop, attic, tree) with a small solar panel — it becomes a relay.
3. Set a **private channel** with a shared key agreed in person.
4. Run a weekly **check-in** so everyone knows how to use it before it matters.

Remember: an AI can still detect *that* you are transmitting and roughly *where*. Keep messages short and don't transmit from your shelter.

## 5.4 Identity verification against deepfakes

When a video call from your sister asks you to "come to the distribution centre", how do you know it's her?

- **Family code words**: agreed in person, never written in any digital system. Have a normal one and a **duress** one ("I'm being forced").
- **Challenge questions** about shared memories that have never been posted online.
- **Call-back rule**: never act on an inbound request; contact the person through a *different* channel you initiate.
- **The "in person" rule**: important decisions (moving, surrendering supplies, meeting strangers) require face-to-face confirmation.

## 5.5 The zero-tech plan

Write this on paper and give copies to everyone in your group:

- **Rally points**: primary (near home), secondary (in the neighbourhood), tertiary (out of town)
- **Schedule**: "If comms are down, go to Rally Point A at 10:00 and 16:00 each day"
- **Signals**: a visible sign at home (e.g., a coloured cloth in a window) meaning "safe" / "gone to B"
- **Message board**: a physical location for paper notes

Next: [Chapter 6 — Information Resistance →](06-information.md)
