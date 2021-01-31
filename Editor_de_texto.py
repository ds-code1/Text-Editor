#ecoding:UTF-8
try:
	import PySimpleGUI as sg
except:
	print('nescessario a instalação de PySimpleGUI')

#theme
sg.theme('Dark Brown 1')

#layouts
layout = [[
	sg.Button('Novo Arquivo',key='resetar',font=('ubuntu mono',12),pad=(0,0,0,0)),
	sg.Button('Abrir Arquivo',key='abrir',font=('ubuntu mono',12),pad=(0,0,0,0)),
	sg.Button('Salvar Arquivo',key='save',font=('ubuntu mono',12),pad=(0,0,0,0)),
	sg.Button('Salvar como',key='salvar_como',font=('ubuntu mono',12),pad=(0,0,0,0)),
	sg.Button('Sair',key='sair',font=('ubuntu mono',12),pad=(0,0,0,0))],
	[sg.Text('::::Path::::',key='name',font=('ubuntu mono',17),size=(60,1))],
	[sg.Multiline(font=('ubuntu mono',12),size=(90,25),key='text')]	
]
window = sg.Window('Text Editor',layout=layout,resizable=True,margins=(0,0))

window.read(timeout=1)
window['text'].expand(expand_x=True, expand_y=True)

def open_file():
	try:
		filename = sg.popup_get_file('Abrir Arquivo', no_window=True)
		Arquivo = open(filename,'r')
		window['text'].update(Arquivo.read())
		window['name'].update(filename)
		return filename
	except:
		pass

def novo_arquivo():
	window['name'].update('::::Path::::')
	window['text'].update('')
	filename = '::::Path::::'
	return filename

def save_as():
	try:
		filename = sg.popup_get_file('Salvar como',save_as=True, no_window=True)
	
		Arquivo = open(filename,'w')
		Arquivo.write(values.get('text'))
		Arquivo.close()
		window['name'].update(filename)
		return filename
	except:
		pass

def save(filename):
	if filename != '::::Path::::':
		Arquivo = open(filename,'w')
		Arquivo.write(values.get('text'))
		window['name'].update(filename)
		Arquivo.close()
		return filename
	else:
		filename = save_as()
		return filename

events = ''
values = ''
filename = '::::Path::::'

while True:
	events, values = window.read()
	if events == sg.WINDOW_CLOSED or events in 'sair':
		quit()

	elif events in 'resetar':
		filename = novo_arquivo()

	elif events in 'salvar_como':
		filename = save_as()

	elif events in 'abrir':
		filename = open_file()

	elif events in 'save':
		filename = save(filename)

	else:
		sg.popup('input invalido')