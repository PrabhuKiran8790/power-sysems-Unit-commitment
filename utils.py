def active_units(df):
    units = len(df) // 3
    def active_gens(row):
        return [i for i in range(len(row)) if row[i] == 1]
    return [active_gens(df.iloc[i, 0:units+1].tolist()) for i in range(len(df))]

def pgens_cost(index, load, df, cost_functions):
    units = len(cost_functions)
    active_units_at_i = active_units(df)[index]
    l, num, den = 0, 0, 0
    for v in active_units_at_i:
        num += (cost_functions[v][1]) / (2 * cost_functions[v][2])
        den += 1 / (2 * cost_functions[v][2])
    l = round((num+load)/(den), 3)
    
    pgens = [0 for _ in range(units)]
    for v in active_units_at_i:
        pgens[v] = round((l - cost_functions[v][1]) / (2 * cost_functions[v][2]), 3)
    # print(pgens)
    
    costs = [0 for _ in range(units)]
    for v in active_units_at_i:
        costs[v] = round(cost_functions[v][0] + cost_functions[v][1] * pgens[v] + cost_functions[v][2] * pgens[v]**2, 3)
    costs.append(sum(costs))
    # print(costs)
    
    df.iloc[index, units:units*2] = pgens
    df.iloc[index, 2*units:(3*units)+1] = costs
    
    # return pgens, costs

# pgens_cost(2, 700, df, cost_functions)


def sort_combinations(combinations_):
    n = len(combinations_)
    for _ in range(n):
        swapped = False
        for j in range(1, n-1):
            if combinations_[j].count(1) < combinations_[j - 1].count(1):
                combinations_[j], combinations_[j - 1] = combinations_[j - 1], combinations_[j]
                swapped = True
        if not swapped:
            break
    return combinations_