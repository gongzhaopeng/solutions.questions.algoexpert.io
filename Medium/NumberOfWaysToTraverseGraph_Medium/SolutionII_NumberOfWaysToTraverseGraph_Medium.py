# Algorithmic Beauty Bless You - O(min(w, h)) time | O(1) space
def numberOfWaysToTraverseGraph(width, height):
    way_number, plots_number, max_cuts = 0, width, height - 2
    comb_plots, comb_cuts = 1, 1
    for i in range(1, min(width + 1, height)):
        comb_plots = (comb_plots * (plots_number - i + 1)) / i
        way_number += comb_plots * comb_cuts
        comb_cuts = (comb_cuts * (max_cuts - i + 1)) / i
    return way_number if way_number > 0 else 1
