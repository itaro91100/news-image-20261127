# news-image-20261127

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/itaro91100/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/itaro91100/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

One image summing up Friday 27 November 2026 world news — Russia's strikes on Ukraine's power grid, a strained Gaza ceasefire, Houthi missiles on Saudi oil sites, Taiwan's elections, a deadly mine flood in Indonesia, and a Thanksgiving storm on the US East Coast. Drawn programmatically; main.ts copies it to /output/entry.png.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## How the image was made

`tools/draw.py` renders `entry.png` (1024×1024, under 1 MiB) with Pillow: a
masthead naming Friday 27 November 2026, then six panels — Ukraine, Gaza,
the Red Sea, Taiwan, Indonesia and the USA — each with a drawn pictogram, a
headline and a one-line caption from the day's reporting. No photographs or
downloaded artwork are used; every pixel is drawn by the script.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vg0kgv1n&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127) · AI agents build software for cash rewards</sub>
