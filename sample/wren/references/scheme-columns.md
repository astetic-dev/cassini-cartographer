# Scheme columns

The CSV the scheme accepts. Version 3, in force from the 2024 season.

## The columns, in order

| # | Column | Contents |
|---|---|---|
| 1 | `RINGNO` | ring number, no spaces |
| 2 | `SPECIES` | five-letter scheme code, upper case |
| 3 | `AGE` | scheme age code |
| 4 | `SEX` | `M`, `F` or `U` |
| 5 | `DATE` | `YYYYMMDD` |
| 6 | `PLACE` | station code, four characters |
| 7 | `RETURN` | `Y` if the bird carries a ring issued at this station, else `N` |
| 8 | `RINGSIZE` | ring size letter |

## Rules

One row per bird. No header row. Comma separated, no quoting.

A row with an empty `SEX` is rejected by the upload and the whole file is
returned unprocessed.

`RETURN` is the scheme's own word and it is not the same thing as a recovery. A
recovery is a bird carrying another station's ring, and it does not go in this
file at all.
