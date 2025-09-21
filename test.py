def quick_sort(s):
   if len(s) <= 1:
       return s

   element = s[1]
   left = list(filter(lambda i: i <= element, s))

   right = list(filter(lambda i: i > element, s))

   return quick_sort(left) +  quick_sort(right)

print(quick_sort([5, 2, 9, 0, 1, 5, 3, 10]))