#!/usr/bin/env awk -f

BEGIN {
  FS = OFS = " "

  # build our lookup of zero-padded month numbers
  split("Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec", marr, "|")
  for (i = 1; i <= 12; i++) {
    mhash[marr[i]] = sprintf("%02d", i)
  }
}

{
  # 1:dd 2:mmm 3:yyyy 4:hh 5:mi 6:ss
  split($4, dtarr, "[:/]")

  # replace the column with our reformatted date
  $5 = dtarr[3] "-" mhash[dtarr[2]] "-" dtarr[1] " " dtarr[4] ":" dtarr[5] ":" dtarr[6]

  # print the whole line
  print
}
