# Wrong neighbours — how to write `Does not hit`

`Hits` is the easy half. Any careful reader produces it, and so does a fresh
chat. `Does not hit` is the half that saves time, because it stops the reader's
**next** move — the plausible one they were about to make.

The card names **one** wrong neighbour: the one a competent reader would guess
next. Not three. Naming three is hedging, and hedging tells the reader nothing
about which guess was the tempting one.

---

## The five false edges

Each of these makes two nouns *look* coupled. None of them is an edge.

### 1 File adjacency

Living in the same file is not an edge.

The most seductive false coupling in any territory with large files. In a
7,000-line file, two nouns can share a file and share nothing else. The file is
a container, not a relationship.

**Tell:** you can describe the connection only as "they're both in X".

### 2 Table adjacency

Sitting in the same registration table, export block or route list is not
coupling.

A table of 73 entries is an alphabet, not a sentence. Two names next to each
other in it have exactly as much to do with each other as two words on the same
page.

**Tell:** the connection disappears if you sort the table differently.

### 3 Name adjacency

A shared verb or a shared prefix is not an edge.

This is where collisions and wrong neighbours meet: the same shared word that
misroutes a reader also makes two nouns look related. `history_forget` and
`peer_forget` share a verb and nothing else.

**Tell:** the connection is entirely in the name, and vanishes on rename.

### 4 Label adjacency

Two controls in the same menu, toolbar or screen are not coupled.

Interface proximity is a layout decision. Two buttons side by side may touch
completely separate machinery.

**Tell:** the connection is spatial, and would vanish in a redesign.

### 5 Channel adjacency

Sharing a channel is not sharing a contract.

Two senders on one channel, with different payload shapes, are two edges that
happen to travel the same wire. Changing one payload does not touch the other
sender — but it may well touch the receiver, which is a different card.

**Tell:** you cannot say what the shared payload is without naming two shapes.

---

## How to pick the one

1. Take the noun. List everything a reader might reasonably think is downstream.
2. Strike out everything that is a real edge — those are `Hits`.
3. From what remains, pick the one with the **strongest false signal**: shared
   name first, then shared interface position, then shared file.
4. Write it with the one sentence that separates them.

The sentence must give the reader something checkable, not just a denial.
Compare:

> Does not hit: the Peer noun.

against

> Does not hit: the Peer noun. The Forget button in the peer list is not this
> noun's Forget — it calls a different command on a different shelf.

The first is a claim. The second lets the reader confirm it in ten seconds and
walk away knowing something.

---

## When there is genuinely no wrong neighbour

Rare, and usually a sign the noun is too small or the census is incomplete. If
it survives review, write it plainly:

> ## Does not hit
> Nothing an experienced reader would guess wrong. This noun has one edge and it
> is in `Hits`.

Do not invent a strawman to fill the field. A field with a fake answer in it is
worse than an honest empty one, because the reader believes it.

---

## The check that catches the error

If the edge table shows a **direct edge** from the noun to the thing the card
says it does not hit, the card is wrong — not the table. Either the edge is real
and it belongs in `Hits`, or it is spurious and the census needs fixing.

This check is worth running mechanically. It is the single most valuable
consistency test over a finished map, because a false `Does not hit` sends a
reader away from something that will in fact break.

**Direct, not reachable — and the difference is not pedantry.** Any territory
whose halves call each other has a cycle in it: a window calls down, a process
pushes back up, and the two are joined in both directions. In a cycle every noun
reaches every other one, so a check run over *paths* condemns every card on the
map, the correct ones included, and the field has to be left empty on exactly
the nouns a reader most needs it on — the hubs. Found the hard way, on a
16-noun map where five nouns reached all the others.

What a card claims is coupling, not reachability: *change this, and that does
not move with it.* Two nouns joined only by the long way round through a hub are
not coupled, and saying so is the whole point of the field. Where the long way
round matters, it is a fact for `Hits` on the hub's own card, which is where a
reader following the chain will already be.
