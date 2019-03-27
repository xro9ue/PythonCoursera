# -*- coding: utf-8 -*-
import re #importing for regular expressions

fhand = open("regex_sum_105455.txt")

nums = [int(num) if num.isdigit() else 0 for num in re.findall("[0-9]+", fhand.read())]

print (sum(nums))    
    
