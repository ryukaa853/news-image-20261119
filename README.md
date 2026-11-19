# The World in One Day — 19 November 2026

A one-image summary of Thursday 19 November 2026's world news, drawn as a
newspaper front page (1024x1024 PNG), for the make.fun bounty
`news-image-20261119`.

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

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
