# Hungry Ghosts (PS2): PCSX2 options

Optional extras for playing *Hungry Ghosts* (SCPS-15046) in the PCSX2 emulator. They work with
the original Japanese disc and with the English fan translation.

- **Modern controls:** move and strafe with the left stick, look and turn with the right
  stick, attack with R1.
- **Faster camera:** turn and look 25% or 50% faster.
- **Aspect ratios:** 16:10, 16:9, 21:9 and 32:9. The view widens, and the HUD and menus keep
  their original shape.
- **Classic controls:** switches the Modern Controls edition of the translation back to the
  original controls.

Each option is a separate checkbox in PCSX2, and you can turn any of them on or off at any time.

## Which file

PCSX2 matches a patch file to the game by the CRC of its executable:

| your game | file |
|---|---|
| Original Japanese disc | `SCPS-15046_91AA4B28.pnach` |
| English fan translation, standard edition | `SCPS-15046_B3C0E286.pnach` |
| English fan translation, Modern Controls edition | `SCPS-15046_798E3212.pnach` |

To find your CRC, right-click the game in PCSX2's game list → **Properties** → **Summary**.

## Installing

1. Copy the file into PCSX2's `patches` folder. If a file with the same name is already there,
   replace it. Ours includes everything the old one had.
   - Windows: `Documents\PCSX2\patches`. In a portable install, use the `patches` folder next
     to PCSX2.
   - Linux: `~/.config/PCSX2/patches`, or `~/.var/app/net.pcsx2.PCSX2/config/PCSX2/patches`
     for the Flatpak.
   - macOS: `~/Library/Application Support/PCSX2/patches`.
   - Not sure? In PCSX2, open **Tools → Open Data Directory** and look for `patches`.
2. Right-click the game → **Properties** → **Patches**, and tick the options you want.
3. Restart the game. The options take effect when the game boots.

## Choosing options

- **Pick one aspect ratio.** If you tick two, only one applies.
- **Don't combine a fan aspect ratio with "Widescreen 16:9".**
  - "Widescreen 16:9" is Arapapa's widescreen patch, included unchanged.
  - Also leave PCSX2's **Enable Widescreen Patches** setting off, since it switches on
    "Widescreen 16:9".
  - "Aspect ratio 16:9 (fan patch)" is the alternative: it keeps the HUD and menus in shape.
- **Pick one camera speed.** If you turn a camera option off, the change applies after the next
  door, or after a restart.
- **Modern and Classic controls:** tick one. If both are ticked, Classic wins.

### Savestates

A savestate holds the whole game as it was when you saved it, including the patch settings
in force at that moment. After changing options, start the game fresh and load your
**memory-card save**. A savestate made before the change can bring the old settings back.

## Display settings for the wide aspect ratios

These are PCSX2 settings under **Settings → Graphics**. Set them there to apply them to every
game, or under the game's **Properties → Graphics** to apply them to this game only.

1. **Aspect ratio:**
   - The **16:9** option sets PCSX2's aspect ratio for you.
   - For **16:10, 21:9 and 32:9**, set **Display → Aspect Ratio → Fit to Window**, and play
     fullscreen on a screen of that shape.
   - Without this setting, PCSX2 shows the picture at 4:3 or 16:9 with black bars, and the
     image looks squashed.
2. **Internal resolution: 3x or higher** (**Rendering → Internal Resolution**). This one matters:
   - To keep its shape on a wide screen, the HUD and menu text is drawn narrower.
   - At native resolution (1x), letters lose pixels and look broken up.
   - 3x looks good, and 4x is sharper if your computer keeps up.
3. **Smoother edges (optional):** tick **Post-Processing → FXAA**.
4. **Movies (optional):** if the game's movies look stretched, set **Display → FMV Aspect
   Ratio Override** to **4:3**.

### What to expect on a wide screen

- **Gameplay:** you see more of the world at the sides. The spirit and vitality gauges stay at
  the screen edges, and the other HUD pieces keep their shape.
- **Menus:**
  - The pause menu, Options and the title menu stay 4:3 in the middle of the screen, and the
    menu background fills the full width.
  - Full-page screens (documents, saving and loading, the rank screen, the opening logos, the
    title slideshow) are shown at 4:3 with bars at the sides.
- **Story screens:** name entry, the judgment and the end-of-game tally and credits keep their 4:3
  layout in the middle; the 3-D scenes behind them fill the width.

## Modern controls

| button | action |
|---|---|
| Left stick | Move forward and back, strafe left and right |
| Right stick | Look around and turn |
| R1 | Attack: tap to strike. Hold to charge or aim, then release to strike, throw or fire |
| L1 + right stick | Swing the arm by hand, as in the original controls |
| L3 (click left stick) | Dash on/off |
| R3 (click right stick) | Recenter the view |
| Other buttons | As in the original game, including your choices in Options → Controls |

- When you're using a tool or picking something up, the right stick moves your arm as in the
  original game, and R1 uses the item.
- Ranged weapons: hold R1 to draw, aim with the right stick, and release to fire.
- "Look up/down: Normal/Reverse" in Options → Controls applies to the right stick.
- Except in the Modern Controls edition, the Controls screen in Options still shows the original
  layout. A patch file can change the controls but not that picture.

## Known limitations

- At the wide aspect ratios, nearby scenery at the far left or right edge can occasionally drop out
  when you stand right next to it (for example, beside a ledge in the bog). The game's renderer was
  built for the 4:3 view; turning toward the spot shows it normally.
- These options are for PCSX2 only. On a real PS2, the Modern Controls edition of the
  translation has the modern controls built in.

## Credits

- Widescreen 16:9: **Arapapa** (from PCSX2's patch collection, included unchanged).
- Modern controls, Classic controls, faster camera, aspect ratios and HUD/menu layout:
  **Mord of Swoonlight**.

*Hungry Ghosts* © 2003 Deep Space Inc. / Sony Computer Entertainment Inc. This is an unofficial
fan project, free and not for sale.
