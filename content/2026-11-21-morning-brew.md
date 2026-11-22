---
date: 2026-11-21
slug: 2026-11-21-morning-brew
tags: Map Projections, Python Visualization, Cartopy, Matplotlib, Geographic Mapping, Game Boy Music, hUGETracker, Music Tracker, Chiptune, Game Boy Homebrew, DNS, Internet Exchange, GeoDNS, GTA 6
---

Morning Brew for 2026-11-21: 3 items written from 3 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. Cartopy - geographic mapping and visualization library - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/11/futuristic-vr-headup-display-design-with-orbital-global-network-3d-rendering.jpg)
**Project:** [cartopy](https://github.com/SciTools/cartopy)
**Source:** https://www.linuxlinks.com/cartopy-geographic-mapping-visualization-library/ · **Karakeep:** `ge7nzwri8pac2hrxsuuy10e1`

**In short:** Cartopy is a Python mapping and visualisation library built around Matplotlib, with projections, transforms and geographic features. I would say it is a solid scientific plotting tool, but nothing I need this week.

**Key points:**
- Free and open source Python library from SciTools / Cartopy contributors.
- BSD 3-Clause licence.
- Extends Matplotlib with GeoAxes and geographic projections.
- Supports Plate Carrée, Mercator, Lambert Conformal, Robinson and Orthographic.
- Draws coastlines, borders, rivers and lakes, and reads Natural Earth and shapefiles.
- Can plot points, contours, vector fields and raster data.

**Details:** Cartopy is a Python library for maps and geographic visualisation. It handles coordinate reference systems and transforms spatial data between them, then plots through Matplotlib with GeoAxes. The feature list is practical rather than flashy: coastlines, borders, rivers, lakes, Natural Earth datasets, shapefile reading, Shapely geometry handling, gridlines and map extent control. It can also transform raster images and overlay several datasets on one map. That is a lot of capability for a plotting library, and it sounds stable, but my work is not in meteorology, climatology or oceanography, so I do not have a use for it. The BSD 3-Clause licence is friendly enough, and candidate link 1 points at the SciTools repository. Nothing for my projects.

**For my projects:** Nothing for my projects.

## 2. hUGETracker - Game Boy music tracker - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/12/Music-Trackers.png)
**Source:** https://www.linuxlinks.com/hugetracker-game-boy-music-tracker/ · **Karakeep:** `jznzaa7parpmlq7vtnzqg4nl`

**In short:** hUGETracker is a free, public-domain Game Boy tracker by Nick Faro that works around the console's four audio channels; I would say it is niche but quite complete for chiptune work.

**Key points:**
- Four-channel tracker for the Game Boy pulse, wave and noise channels
- Pattern editor with 64 rows per pattern and an order editor for full songs
- Instrument types for pulse, wave and noise, plus a custom waveform editor
- Tracker effects plus a graphical effect editor instead of manual hex entry
- Exports standalone Game Boy ROM and GBS files, and renders WAV and MP3
- Cross-platform on Linux, macOS and Windows; written in Pascal; public domain

**Details:** hUGETracker is built around the Game Boy sound hardware: two pulse channels, one programmable wave channel and one noise channel. Patterns have 64 rows, which is plenty for chiptune work, and instruments handle volume envelopes, note length, sweep and pulse duty. There is also a custom waveform editor, channel muting, playback from the song start or the current position, and exports to a standalone ROM or GBS file, or to WAV and MP3. It is written in Pascal by Nick Faro under a public domain licence and runs on Linux, macOS and Windows. I read about it, I did not try it, so I cannot judge how stable the editor feels, but the feature list is long for a free tool. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 3. GTA 6 Just Broke Internet Traffic Records #gta6 #dns #programming, by Better Stack
![](https://i.ytimg.com/vi/sSj40n9FmFg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/sSj40n9FmFg · **Karakeep:** `fe1ohvhq0ikt51qa9cyzj0fv`

**In short:** GTA 6 is a 212GB download and its preload pushed ISPs and exchanges to record peaks; the DNS and CDN plumbing behind it is the interesting part, and I would say it is a good networking explainer with nothing for my projects.

**Key points:**
- GTA 6 is a 212GB download and preload opened on 10 November
- Ripe Labs measured it with over 15,000 internet probes
- One server would need 2.4 exabytes and max a gigabit link for more than 600 years
- Virgin Media UK had its biggest traffic peak ever, 3.8% above a Champions League match
- DECIX Frankfurt hit 22.3 Tbps, about 13 full copies of GTA 6 per second

**Details:** GTA 6 is a 212GB download, and when preload opened on 10 November it pushed traffic records across ISPs and internet exchanges. Ripe Labs ran the numbers across more than 15,000 probes: one server would need 2.4 exabytes and would max out a gigabit link for more than 600 years. Sony and Microsoft spread the game across CDNs instead, and GeoDNS gives a different answer depending on where a console seems to be, sometimes handing the lookup off to another hostname and another CDN. Los Angeles ended up at Farsley, Tokyo at Google Cloud, Istanbul at Amazon CloudFront, and Shanghai went down a long chain that finished at Alibaba Cloud. Internet pioneer Paul Vixie once called this a stupid DNS trick because DNS was never designed for it. RIPE also saw surprisingly few ISP cache servers, guessing the game may just take up too much disk space. Virgin Media UK had its biggest traffic peak ever, 3.8% above a Champions League match, and DECIX Frankfurt hit 22.3 Tbps, which works out to about 13 full copies of GTA 6 every second. Nothing for my projects. So yeah, that's that.

**For my projects:** Nothing for my projects.
