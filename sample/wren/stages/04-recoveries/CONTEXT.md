# 04 recoveries - notices for birds ringed elsewhere

One job: pull the week's returns that carry another station's ring and write one
notice per ring.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Working | `../01-tally/output/week-<nn>-tally.md` | Returns rows | the birds caught again |
| Working | `../../input/week-28.md` | Full file | the ring numbers |

## Process

1. Read the returns rows in the tally.
2. Split rings issued by this station from rings issued elsewhere.
3. Write one notice per foreign ring: ring number, species, date, net.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Recovery notices | `output/recoveries-week-<nn>.md` | markdown |

## Human check

The warden checks each notice against the ring before it is sent.
