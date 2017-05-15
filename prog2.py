import numpy as np
import getopt,sys

# @globals
# standard values
w2 = 1
y = 0.5
filename = "output.dat"
# end

def aceleracao(x,v):
	return -w2*np.sin(x)-y*v
	
def verlet(x,v,e,dt):
	a = aceleracao(x,v)
	x = x + v*dt +0.5*a*dt**2
	a_t = aceleracao(x,v)
	v_t = v+0.5*(a+a_t)*dt
	a_t = aceleracao(x,v_t)
	v=v+0.5*(a+a_t)*dt
	e = 0.5*v**2 + (w2/9.8)*np.cos(x)
	return x,v,e
		
def main():
	
	#variables
	x = 1
	v = 0
	e = 0
	t = 0
	dt = 0.01
	
	arq1 = open(filename,"w+")
	while( t < 10):
		arq1.write(str(t)+" "+str(x)+" "+str(v)+" "+str(e)+"\n")
		t = t + dt
		x,v,e = verlet(x,v,e,dt)
		
	arq1.close()

opcao,valor = getopt.getopt(sys.argv[1:],'w2:y:f: ')

for opcao,valor in opcao:
	if opcao == '-w2':
		w2 = float(valor)
	if opcao == '-y':
		y = float(valor)
	if opcao == '-f':
		filename = str(valor)
main()
	
print 'concluido'
