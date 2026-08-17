# The weekly run

Three stages. The log arrives Monday, the return and the post go out the same
morning.

## Task routing

| Task | Stage |
|---|---|
| Count the week | `stages/01-tally/CONTEXT.md` |
| Build the scheme return | `stages/02-return/CONTEXT.md` |
| Write the station post | `stages/03-post/CONTEXT.md` |

## Order

01 runs first and writes the tally. 02 and 03 both read that tally. They do not
read each other, and the order between them does not matter.

## Standing rules

**Species names.** Every species name written by any stage follows the naming
standard in `references/`. The stage contracts do not repeat this and do not list
it under `Inputs`.

**One week per run.** A run covers one week. The week number comes from the log's
filename and every artifact carries it.

**The ringer's count wins.** Where a stage total disagrees with the count in the
log footer, the run stops and the warden is asked.
