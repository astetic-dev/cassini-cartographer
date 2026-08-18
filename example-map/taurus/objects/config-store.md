# Config store
Type:     store
Status:   live
Reach:    internal
Verified: 2026-08-16 at e652c79

## Is
One folder outside the program where everything that has to survive a restart
is kept: seven files and two folders, in plain JSON and plain text. It is the
only part of Taurus that outlives the code that wrote it.

## Lives at
- `src-tauri/src/lib.rs:61` - where the folder is, and the one setting that moves it
- `src-tauri/src/lib.rs:80` - the projects file
- `src-tauri/src/lib.rs:1299` - the open tabs
- `src-tauri/src/lib.rs:1366` - the session history
- `src-tauri/src/sshhost.rs:75` - the machines allowed to knock

## Moves by
| edge | direction | anchor |
|------|-----------|--------|
| open tabs, rewritten whole | Session → Config store | `src-tauri/src/lib.rs:1303` |
| history, rewritten whole | Session history → Config store | `src-tauri/src/lib.rs:1384` |
| peers, rewritten whole | Peer register → Config store | `src-tauri/src/sshhost.rs:122` |
| one line appended per event | ssh-audit → Config store | `src-tauri/src/sshhost.rs:169` |

## Hits
- Every file already written on somebody's machine. Change what a field is
  called and the old files do not change with it; they are read by the next
  version as they are.
- The folder is `%APPDATA%\Taurus` unless an environment setting names another
  one, which is how a second copy of Taurus runs beside the first without the
  two seeing each other's state.

## Does not hit
- The window. Nothing on screen reads or writes these files. Every path to them
  runs through a named call into the machine half, which is why a change to a
  file's shape shows up as a broken command rather than as a broken page.

## Open
Nothing here migrates an older file to a newer shape on start. Whether that has
been needed yet is not answerable from the code.
