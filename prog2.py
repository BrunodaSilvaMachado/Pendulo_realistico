import getopt,sys

# @globals
# standard values
w2 = 1
y = 0.5
filename = "output.dat"
# end

def aceleracao(x,v):
	return -w2*np.sin(x)-y*v
	
def verlet(x,v,dt):
	a = aceleracao(x,v)
	x = x + v*dt +0.5*a*dt**2
	a_t = aceleracao(x,v)
	v_t = v+0.5*(a+a_t)*dt
	a_t = aceleracao(x,v_t)
	v=v+0.5*(a+a_t)*dt
	return x,v
		
def main():
	
	#variables
	x = 1
	v = 0
	t = 0
	dt = 0.01
	
	arq1 = open(filename,"w+")
	while( t < 10):
		arq1.write(str(t)+" "+str(x)+" "+str(v)+"\n")
		t = t + dt
		x,v = verlet(x,v,dt)
		
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
