"""
Es una solución que apenas voy a probar. La neta, yo creo que va a tirar TLE, pero 
esto es con fé y confiando en el corazón de las cartas.
No es mucho, pero es trabajo honesto.
"""

def get_max_fun_factor(module_chain : dict, current_module : int, roots : list):
    module = module_chain[current_module]
    max_fun_factor = module["fun_factor"]

    if not module["children"]: 
        module["max_fun_factor"] = max_fun_factor
        return max_fun_factor

    for child in module["children"]:
        child_fun_factor = get_max_fun_factor(module_chain, child, roots)
        max_fun_factor = max(max_fun_factor, child_fun_factor)

    module["max_fun_factor"] = max(max_fun_factor, module["max_fun_factor"])

    if current_module in roots:
        smallest_fun_factor = module["fun_factor"]
        max_fun_factor = 0
        for child in module["children"]:
            child_fun_factor = module_chain[child]["max_fun_factor"]
            smallest_fun_factor = min(smallest_fun_factor, child_fun_factor)
            max_fun_factor += child_fun_factor

        if smallest_fun_factor < module["fun_factor"]: max_fun_factor += module["fun_factor"] - smallest_fun_factor

    return max_fun_factor
        

if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        modules = int(input())

        fun_factors = [int(x) for x in input().split()]
        pointing = [int(x) for x in input().split()]
        module_chain = {}
        roots = set()

        for module in range(modules):
            module_chain[module + 1] = {
                "fun_factor" : fun_factors[module],
                "children" : [], 
                "max_fun_factor" : 0,
            }

            if pointing[module] == 0: roots.add(module + 1)
            else: module_chain[pointing[module]]["children"].append(module  + 1)
        
        max_fun_factor = 0
        
        for root in roots:
            max_fun_factor += get_max_fun_factor(module_chain, root, roots)

        print(f"Case #{_ + 1} : {max_fun_factor}")