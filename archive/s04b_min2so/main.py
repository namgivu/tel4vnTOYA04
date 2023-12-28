# .venv/bin/python -m pyflowchart main.py -o ./pyflowchart/flowchart.html

def min2so(a,b):
  min = a
  if a >= b:
    min = b
    i=122  # add code to force drawing diamond in flowchart
  return min

def min2so_(a,b):
  if a<b: return a
  else:   return b

def min2so__(a,b):
  min = a if a<b else b
  return min

print( min2so(a=1,b=22) )
