# .venv/bin/python -m pyflowchart main.py -o ./pyflowchart/flowchart.html

def min2so(a,b):
  min = a
  if a >= b:
    min = b
    i=122  # add code to force drawing diamond in flowchart
  return min

print( min2so(a=1,b=22) )
