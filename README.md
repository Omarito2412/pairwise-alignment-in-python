# Pairwise List Alignment in Python3

## What is this?
I forked this repo to revive it and to add support for word level alignment.

The way this works is by aligning two lists of words instead of aligning two strings.

This is very useful if you're trying to align two files in which some damage might have occurred to one of which.


## Usage
I've added a main.py in which you can understand how this works.

There is also the original command line scripts needle and water.

You can run them this way

```
./needle FILE1 FILE2
./water FILE1  FILE2
```

Another way is if you're interested in the alignments.

```
from alignment import needle

# seq1, seq2 are two lists of words
seq1_aligned, seq2_aligned = needle(seq1, seq2)
```

Original Smith-Waterman implementation in Python was forked from
http://narnia.cs.ttu.edu/drupal/node/104
by Forrest Sheng Bao http://fsbao.net
a free software licensed under GNU General Public License (GPL)

A copy of GPL version 3 has been placed into the file LICENSE.
