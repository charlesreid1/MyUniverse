# Film Noir Monologue

This readme breaks down the Film Noir Monologue table generator example,
and how this (non-trivial) table generator works. In short, it uses
multiple lists and cross-references to enable templates.

## Before starting

To start out, open `Data/Tables/test.db` in a SQLite explorer program.

Select the `TableLines` table, and filter which values are being viewed
by filtering to rows whose `TableName` column is `Film Noir Monologue`.

## Start

The Noir Film Monologue generator uses multiple lists to generate monologues.
Those are indexed by the `SubTableName` column.

The generator begins with `[Start]`. This bracketed expression means,
look for a sub-table named `Start`, and substitute a random item from
that table in place of `[Start]`.

Most (all?) of the table generators begin with this `[Start]` sub-table.
In the case of the Film Noir Monologue generator, there are six values
in the `[Start]` sub-table:

* `[A]`
* `[B]`
* `[C]`
* `[D]`
* `[E]`
* `[F]`

The table generator will first roll a six-sided die to decide from the
six different outcomes. It will then return the corresponding bracketed
letter.

## Recursive

The process is recursive in the sense that `[A]` actually refers to a
sub-table named `A`. If we look up that sub-table, we see that it only
has a single value:

```
[Intro] I had just [WentTo] [Restaurant] and ordered [RestaurantOrder]...
```

As before, when the generator calls the roll function, it will recurse
and evaluate bracketed expressions, substituting a random item from the
corresponding sub-list.

By printing out tokens as they are parsed in the TableGenerator, you can
see how this process leads to the final assembled monologue. Here are
a few example values:

```
Intro-> "It was as hot as I'd ever remembered it. Just blistering. You could cook breakfast right on the sidewalk."
WentTo -> "cruised into"
Restaurant -> "Dino's"
RestaurantOrder -> "some cold coffee and colder toast"
```

resulting in the opening monologue,

> It was as hot as I'd ever remembered it. Just blistering. You could
> cook breakfast right on the sidewalk. I had just cruised into DIno's
> and ordered some cold coffee and colder toast.


One other note on expressions - they can include
references to other tables, as well as other sub-tables. For example,
there are a few expressions that look like this:

```
[American Census Names.surname]
```

This will substitute a random value from the sub-table `surname`
and the table `American Census Names`. This is a separate table
from the Film Noir Monologue table.

## Defining a Table Generator from .tab files

What if you want to define a table generator database from .tab files,
making it easier to modify/edit/define them in plain text/version
control, and then import them when you are ready to generate stuff?

This can be done! The functionality has been shimmed into the TableGenerator
and TableManager classes. To do this, start by creating a new base directory:

```
mkdir Data.mini
```

You will then define a set of .tab files that contain definitions for tables,
sub-tables, and templates. Take al ook at the baseline examples in `Data.old`.
Film Noir Monologue generator is a bit complicated but there are some simpler
ones with only a few sub-tables.

Alternatively, you can just copy the .tab files straight from the `Data.old`
examples and use them as a starting point to modify them.

`src/Generators/tablegen/table.py` contains the logic for importing data.




