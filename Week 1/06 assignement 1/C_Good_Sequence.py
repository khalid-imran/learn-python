from collections import Counter

def good_sequence(val, int_list):
    
    frq = Counter(int_list)
    rm = 0
    
    for i, count in frq.items():
        if count > i:
            rm = rm + count - i
        elif count < i:
            rm = rm + count
    
    return rm

val = int(input())
int_list = list(map(int, input().split()))   

print(good_sequence(val, int_list))

    
    
    