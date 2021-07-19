#B083040012
z="print({*z})";characterUsed="print({*z})"; 
exec(characterUsed)
#{'n', '*', 'i' ,'r', 'z', '}', '(', ')', 't', '{', 'p'}

x="hello"
d={}
z="d[[*x*5][5]]=d"
exec(z); print(d)
#{'h': {...}}
exec(characterUsed)
#{'d','*',']','[','5','x','='}

z="d['h'] is d"  
exec("print("+z+")")
#True
print(eval(z))
#True
exec(characterUsed)
#{'d',']','h','[','i','s',' ',"'"]}