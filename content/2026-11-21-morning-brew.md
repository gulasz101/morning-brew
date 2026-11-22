---
date: 2026-11-21
slug: 2026-11-21-morning-brew
tags: Map Projections, Python Visualization, Cartopy, Matplotlib, Geographic Mapping, Game Boy Music, hUGETracker, Music Tracker, Chiptune, Game Boy Homebrew, DNS, Internet Exchange, GeoDNS, GTA 6
---

Morning Brew for 2026-11-21: 3 items written from 3 hoarded bookmarks and feeds, 0 dropped after a failed retry.

### RSS

## 1. Cartopy - geographic mapping and visualization library - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2020/11/futuristic-vr-headup-display-design-with-orbital-global-network-3d-rendering.jpg)
**Source:** https://www.linuxlinks.com/cartopy-geographic-mapping-visualization-library/ · **Karakeep:** `ge7nzwri8pac2hrxsuuy10e1`

**In short:** Cartopy is SciTools' Python library for maps and geographic plots on top of Matplotlib, under the BSD 3-Clause licence. I would say it is solid for scientific mapping, but nothing for my projects.

**Key points:**
- Free and open source Python library from SciTools / Cartopy contributors.
- BSD 3-Clause 'New' or 'Revised' Licence.
- Extends Matplotlib with GeoAxes and geographic projections.
- Supports Plate Carrée, Mercator, Lambert Conformal, Robinson and Orthographic among others.
- Draws coastlines, borders, rivers and lakes, and reads Natural Earth and shapefile data.
- Transforms points, lines, polygons, images and raster data between coordinate systems.

**Details:** It is the usual scientific-Python stack piece: projections, coordinate transforms, Shapely geometries, gridlines, contours, vector fields and raster plots, with Matplotlib styling on top. The source lists a long feature set and no version number, release date or install size, so I am judging the page rather than a release. It looks quite good job for meteorology, climatology and oceanography work, and the Natural Earth and shapefile support is the practical bit. For me it is a library to read about, not to deploy: no Kubernetes path, no backup story, no metrics, and no fit with the factory or the agents. So yeah, that's that.

**For my projects:** Nothing for my projects.

## 2. hUGETracker - Game Boy music tracker - LinuxLinks, by LinuxLinks
![](https://www.linuxlinks.com/wp-content/uploads/2021/12/Music-Trackers.png)
**Project:** [hUGETracker](https://github.com/SuperDisk/hUGETracker)
**Source:** https://www.linuxlinks.com/hugetracker-game-boy-music-tracker/ · **Karakeep:** `jznzaa7parpmlq7vtnzqg4nl`

**In short:** hUGETracker is Nick Faro's free Game Boy music tracker with four channels and 64-row patterns; I would say it is quite a good job for chiptune work, but it is not worth it for my projects.

**Key points:**
- Developer Nick Faro (SuperDisk); public domain licence
- Four channels: two pulse, one programmable wave, one noise
- Each pattern has 64 rows, with separate note, instrument and effect columns
- Exports standalone Game Boy ROM and GBS files, plus WAV and MP3 renders
- Cross-platform on Linux, macOS and Windows; written in Pascal

**Details:** hUGETracker is a music composition app built around the Game Boy sound hardware, so you get a tracker for the four channels: two pulse, one programmable wave and one noise. It is by Nick Faro (SuperDisk), released as public domain software, and it is written in Pascal, so the source is easy to read if you know the language. Songs are built from 64-row patterns, which that's plenty for a Game Boy loop, with separate note, instrument and effect columns, then combined in an order editor, and each channel can be muted while you listen.

The export side is the useful bit, yeah: standalone Game Boy ROM and GBS files, plus WAV and MP3 renders, and it runs on Linux, macOS and Windows. Unfortunately there is no version number in the piece, so I cannot tell which release this is, and I have not found a reason to fold it into my own projects, so I would say it is quite a good job for chiptune people but not worth it for me.

**For my projects:** Nothing for my projects.

## 3. GTA 6 Just Broke Internet Traffic Records #gta6 #dns #programming, by Better Stack
![](https://i.ytimg.com/vi/sSj40n9FmFg/maxresdefault.jpg)
**Source:** https://www.youtube.com/shorts/sSj40n9FmFg · **Karakeep:** `fe1ohvhq0ikt51qa9cyzj0fv`

**In short:** A short about how GTA 6's 212GB preload moved through CDNs and GeoDNS, with some very large traffic numbers. I would say it is a fun networking anecdote, not something I can use.

**Key points:**
- GTA 6 is a 212GB download; preload opened on 10 November.
- RIPE Labs, with over 15,000 probes, estimated 2.4 exabytes if everyone pulled from one server.
- Sony and Microsoft spread the game across several CDNs; consoles use GeoDNS to get different answers by location.
- Examples in the short: Los Angeles to Farsley, Tokyo to Google Cloud, Istanbul to Amazon CloudFront, Shanghai to Alibaba Cloud.
- Virgin Media UK peaked 3.8% above a Champions League match; DE-CIX hit 22.3 Tbps, about 13 full copies of GTA per second.

**Details:** The short explains the delivery problem behind a 212GB preload. RIPE Labs did the math: 2.4 exabytes from one server would max out a gigabit link for more than 600 years. So Sony and Microsoft spread the files across several CDNs, and the console still has to find the right one. DNS does that with GeoDNS: the same hostname returns different answers depending on where you seem to be, and one answer can hand off to another hostname, so each lookup can land on a different CDN. Los Angeles went to Farsley, Tokyo to Google Cloud, Istanbul to Amazon CloudFront, and Shanghai down a chain to Alibaba Cloud. Paul Vixie once called this a stupid DNS trick, because DNS was not designed for it. RIPE also saw surprisingly few CDN cache servers inside ISPs, and guessed the game is just too large for them. Virgin Media had its biggest peak ever, 3.8% above a Champions League match, and DE-CIX hit 22.3 Tbps, about 13 full copies of GTA every second. So yeah, that is a lot of traffic.

**For my projects:** Nothing for my projects.
