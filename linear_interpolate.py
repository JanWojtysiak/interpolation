import data_gold
def linear_interpolate(x_new, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    # Handle the case where the points are the same to avoid division by zero
    if x1 == x2:
        return y1

    proportion = (x_new - x1) / (x2 - x1)
    y_new = y1 + (y2 - y1) * proportion    
    return y_new

def find_nearest_neighbor(x_new):

    wavelengths = data_gold.WAVELENGTHS_UM
    n_values = data_gold.N_VALUES

    min_distance = float('inf')
    nearest_n_value = None

    for i in range(len(wavelengths)):
        distance = abs(x_new - wavelengths[i])

        if distance < min_distance:
            min_distance = distance
            nearest_n_value = n_values[i] 

    return nearest_n_value
