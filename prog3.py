import numpy as np
import matplotlib.pyplot as plt
import getopt,sys

# @globals
# standard values 
_fileName = "output.dat"
# end

def grafics(_tlist,_dlist,_imagName,_title,_xLabel,_yLabel):
	print 'processando...'
	plt.figure(figsize=(5,4),dpi=96)
	
	ax = plt.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.spines['bottom'].set_position(('data',0))
	ax.yaxis.set_ticks_position('left')
	ax.spines['left'].set_position(('data',0))
	ax.autoscale()
	
	plt.rc('text',usetex = True)
	plt.rc('font',**{'sans-serif':'Arial','family':'sans-serif'})
	plt.xlabel(_xLabel)
	plt.ylabel(_yLabel)
	
	plt.grid()
	plt.title(_title,fontsize = 14)
	plt.plot(_tlist,_dlist,'k-',linewidth = 2)
	plt.savefig(_fileName+"."+_imagName+'.png',dpi=96)

def main():
	x = []
	v = []
	t = []
	
	arq1 = open(_fileName,'r')
	
	for line in arq1:
		a,b,c = line.split()
		x.append(float(b))
		v.append(float(c))
		t.append(float(a))
	arq1.close()
	
	grafics(t,x,'image1',r'Pendulo-posi\c{c}\~{a}o',r'\textit{tempo}(s)',r'\textit{posi\c{c}\~{a}o} (m)')
	grafics(t,v,'image2',r'Pendulo-velocidade',r'\textit{tempo}(s)',r'\textit{velocidade}(m/s)')
	grafics(x,v,'image3',r'Espa\c{c}o de fases',r'\raggedright{\textit{posi\c{c}\~{a}o} (m)}',r'\raggedleft{\textit{velocidade}(m/s)}')
		
opcao,valor = getopt.getopt(sys.argv[1:],'f: ')

for opcao,valor in opcao:
	if opcao == '-f':
		_fileName = str(valor)
	
main()

print 'concluido'