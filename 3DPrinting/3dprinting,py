import numpy as np

#number of cases
T = int(input())

for k in range(1, T+1):
    # C M Y K
    # printers
    colors = []
    for h in range(3):
      colors.append(list(map(int, input().split())))

    #select the minimum ink level over all printers per color
    cmin=np.amin(colors, axis=0) 

    #if not enough tint, impossible
    if sum(cmin)<1e6:
      print(f"Case #{k}: "+"IMPOSSIBLE")
      continue

    #Add up to 1e6 tint units
    csum=0  
    for i in range(len(cmin)):
      csum = csum+cmin[i]
      #Once 1e6 tint units reached, fill with 0's
      if csum>=1e6:
        rest = csum-1e6
        cmin[i] = cmin[i]-rest 
        cmin = np.pad(cmin[:i+1], (0, len(cmin)-(i+1)), 'constant', constant_values=(-1, 0))      
        break
        
    print(f"Case #{k}: "+' '.join(map(str, cmin)))
