# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ryukaa853/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ryukaa853/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-image summary of Thursday 19 November 2026's world news, drawn as a
newspaper front page (1024x1024 PNG): Trump, Xi and Putin's first trilateral
talks in Shenzhen, the ICJ's genocide ruling against Myanmar, GTA VI's
record launch, Anthropic's $81bn IPO, a missile strike on Riyadh, and
Israel's push into central Gaza.

## Stories in the image

1. **Trump, Xi and Putin hold first trilateral talks** — Shenzhen summit,
   joint "peace declaration" on UN reform, nuclear arms and oil output.
   (The Times, Just Security)
2. **Myanmar guilty of genocide** — the UN's top court (ICJ) ruled Myanmar
   committed genocide against the Rohingya in 2017, a first against a state.
   (UN News, The Irish Times)
3. **GTA VI is out — and already a record** — Rockstar's Vice City epic
   launched at midnight worldwide after $1bn in pre-orders (10.3m copies).
   (Rockstar Games, Le Monde, CNN)
4. **Anthropic's $81bn IPO is the biggest ever** — shares debuted on Nasdaq
   as "ANT" at $83, valuing the AI lab at about $1.5 trillion.
   (Reuters, Wall Street Journal)
5. **Missile hits Riyadh as Iran war grinds on** — a Houthi missile damaged
   the PIF Tower; Trump said the US will "see what happens" after Jan. 1.
   (Just Security)
6. **Israel pushes into central Gaza** — tanks crossed the "yellow line";
   Ukraine struck the Crimean Bridge for a third time this week.
   (Just Security)

## How it is built

`draw.py` draws the image with Pillow (DejaVu fonts, vector-style panels)
and writes `entry.png`. `main.py` copies `entry.png` to
`/output/entry.png` — no network, fully deterministic.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=8tc4hwe6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards
