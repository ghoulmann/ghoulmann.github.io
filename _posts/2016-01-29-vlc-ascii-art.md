---
layout: post
title:  "VLC Output ascii Video"
date:   2016-01-29
categories: video vlc
---

Well, I'm late to this party.

It seems that mplayer(1) isn't available for my Wily desktop. But torrentfreak had just turned my on to the existence of Matrix-Ascii -- here's a short clip from YouTube:

<iframe width="560" height="315" src="https://www.youtube.com/embed/F1-glc16PHg" frameborder="0" allowfullscreen></iframe>

Feeling a bit in the dark about how to do this, and being uncomfortable with that, I started looking into how to accomplish something similar with my own video. The first solution I came across was mplayer with lib-aa. The problem that I had with that first solution is described [here](http://askubuntu.com/questions/491471/mplayer-aalib-missing-vo-aa-not-working); however, the solution isn't working with Wily.

I eventually came upon this [post](http://www.tweakandtrick.com/2014/04/vlc-ascii.html). It's from 2014, but it still offers helpful direction for producing ascii output from video files.

Note that VLC does both color and monochrome ascii output.
