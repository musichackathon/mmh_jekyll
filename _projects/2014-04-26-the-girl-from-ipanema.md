---
date: 2014-04-26
title: "The Girl from Ipanema"
creator_names: ["Andreas Jansson"]
---

Andreas Jansson likes Bossa Nova, but to him the chords are much more interesting than all the other “post colonial bullshit.” So he wanted to figure out a way to make new music that features the harmonies used in Bossa Nova, but uses different rhythms and timbres and textures. What he came up with is software that generates beautiful realizations of Bossa Nova harmonic progressions made from thousands of tiny samples of the top 1000 most popular songs in the US since 1950 according to Billboard. The result has lush timbres, subtle rhythmic layerings, and a meditative tone.

The process for creating this new Bossa Nova and Pop-derived music was somewhat straightforward. Audio of the top 1000 most popular Billboard pop songs was broken down into segments at every attack using The Echo Nest API. The Echo Nest provides an estimation of the strength of each of the twelve pitch classes for every segement, which Jansson used to identify segments that had one, two, or three very prominent pitches and very low strength of all other notes. A harmonic progression was then chosen manually (he used Girl From Ipanema in his demo at the Jazz Hackathon) which was realized by layering repeated segments. For example, if a harmony is {C E G Bb}, five segments might be chosen: {C}, {C G}, {E}, {C E G}, {G Bb}. Because each segment is a different length and the segments are being repeated, the result is a random polyrhythm of several different tempos.

Check out the code here: [https://github.com/andreasjansson/jazzcollage](https://github.com/andreasjansson/jazzcollage)

<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/146668001&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>