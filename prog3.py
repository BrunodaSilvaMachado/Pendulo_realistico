import numpy as np
import matplotlib.pyplot as plt
import getopt,sys

# @globals
# standard values 
_fileName = "output.dat"
# end

def grafics(_tlist,_dlist,_imagName,_title,_legend,_xLabel,_yLabel):
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
	plt.plot(_tlist,_dlist,'k-',linewidth = 2,label = _legend)
	plt.legend(loc = 'upper right')
	plt.savefig(_fileName.replace('.dat','_')+_imagName+'.png',dpi=96)

def main():
	x = []
	v = []
	t = []
	e = []
	
	arq1 = open(_fileName,'r')
	
	for line in arq1:
		a,b,c,d = line.split()
		x.append(float(b))
		v.append(float(c))
		e.append(float(d))
		t.append(float(a))
	arq1.close()
	
	grafics(t,x,'image1',r'Pendulo',r"posi\c{c}\~{a}o",r'\textit{tempo}(s)',r'\textit{posi\c{c}\~{a}o} (m)')
	grafics(t,v,'image2',r'Pendulo',"velocidade",r'\textit{tempo}(s)',r'\textit{velocidade}(m/s)')
	grafics(x,v,'image3',r'Espa\c{c}o de fases',r"X/V",r'\raggedright{\textit{posi\c{c}\~{a}o} (m)}',r'\raggedleft{\textit{velocidade}(m/s)}')
	grafics(t,e,'image4',r'Pendulo',"Energia",r'\textit{tempo}(s)',r'\textit{Energia} (j)')
		
opcao,valor = getopt.getopt(sys.argv[1:],'f: ')

for opcao,valor in opcao:
	if opcao == '-f':
		_fileName = str(valor)
	
main()

print 'concluido'