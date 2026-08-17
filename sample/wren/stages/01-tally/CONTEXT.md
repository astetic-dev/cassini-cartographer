# 01 tally - count the week

One job: turn the week's net rounds into one table of counts.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Working | `../../input/week-28.md` | Full file | the week's net rounds |
| Working | `../../notes/handover.md` | Last entry | what the run before left open |

## Process

1. Read the last entry in the handover before anything else.
2. Read the log. Use the Species, Ring, Age, Sex and Return columns.
3. Count new rings and returns, per species.
4. Write one row per species in log order, then the names from the footer.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Week tally | `output/week-<nn>-tally.md` | markdown table |

## Human check

Compare the total against the ringer's count in the log footer before either of
the next two stages runs.
