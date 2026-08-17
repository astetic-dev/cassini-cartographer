# 02 return - build the scheme return

One job: write the return a ringer types into the scheme's web form.

## Inputs

| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Working | `../01-tally/output/week-<nn>-tally.md` | Full file | the counts |

## Process

1. Read the tally.
2. Write one line per bird: species, ring number, age, sex, date.
3. Mark a return with `Y`. A return is a bird ringed at this station before.
4. Leave out any bird carrying another station's ring. The scheme takes those
   through its recoveries portal, not through this form.

## Outputs

| Artifact | Location | Format |
|---|---|---|
| Scheme return | `output/return-week-<nn>.md` | markdown table |

## Human check

A ringer copies the table into the scheme's web form by hand. Nothing in this
workspace submits it, and nothing here reads it back.
