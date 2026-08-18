# The window
Type:     object
Status:   live
Reach:    ui
Verified: 2026-08-16 at e652c79

## Is
Everything you see: the tab strip, the terminals, the menus and the settings,
drawn as one web page. It holds no state that matters - it asks for what it
needs by name and draws what comes back.

## Lives at
- `src/index.html:1` - the page itself, and what it loads
- `src/main.js:523` - the first thing it asks for on start
- `src/main.js:3466` - where output from a tab arrives
- `src/styles.css:1` and `src/skins.css:1` - how it looks, and the themes

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| 97 calls, 69 names | window → Command surface | `src/main.js:523` |
| output and exit of every tab | Session → window | `src/main.js:3466` |
| mirrored output of a remote tab | SSH host → window | `src/main.js:4725` |
| the trail of an SSH connection | ssh-audit → window | never arrives |

## Hits
- Nothing on disk directly. Every change that outlives the window goes through
  a named call, which is what makes the surface between the two halves the
  place a rename actually breaks.

## Does not hit
- Config store. The page keeps nothing on disk of its own: the projects, the
  open tabs and the history all reach the config folder through a named call
  into the machine half, never from here.

## Dead here
- The trail sent on `ssh-audit` arrives here and nothing is listening for it
  - `src-tauri/src/sshhost.rs:173` - checked from four directions. The events
  themselves are real and written to disk; see the ssh-audit card.

## Open
What the page does with the twelve channels it does listen for is on the cards
for the nouns that send them; which of them can arrive while the window is in
the background is not answerable from here.
