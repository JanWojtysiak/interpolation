import data_gold
def find_bounding_points(x_new):
    wavelengths = data_gold.WAVELENGTHS_UM
    n_values = data_gold.N_VALUES
    # --- Edge case 1: x_new is smaller than the first known point ---
    if x_new <= wavelengths[0]:
        return (wavelengths[0], n_values[0]), (wavelengths[0], n_values[0])

    # --- Edge case 2: x_new is larger than the last known point ---
    if x_new >= wavelengths[-1]:
        return (wavelengths[-1], n_values[-1]), (wavelengths[-1], n_values[-1])

    for i in range(1, len(wavelengths)):
        if wavelengths[i] >= x_new:
            # The point before it is the left neighbor (p1)
            p1 = (wavelengths[i-1], n_values[i-1])
            # This current point is the right neighbor (p2)
            p2 = (wavelengths[i], n_values[i])
            return p1, p2
