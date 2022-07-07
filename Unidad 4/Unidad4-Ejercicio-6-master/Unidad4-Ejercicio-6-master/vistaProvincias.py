import tkinter as tk

from tkinter import messagebox

from claseProvincia import Provincia

import requests

class ProvinciaList(tk.Frame):
    
    def __init__(self, master,**kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self,**kwargs)
        scroll = tk.Scrollbar(self,command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, unaProvincia, index=tk.END):
        text = "{}".format(unaProvincia.getNombre())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)


class ProvinciaForm(tk.LabelFrame):
    fields = ("Nombre","Capital","Cantidad de Habitantes","Cantidad de Departamentos/partidos","Temperatura","Sensación Térmica","Humedad")
   
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincias", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, unaProvincia):
        # a partir de un provincia, obtiene el estado
        # y establece en los valores en el formulario de entrada
        provincias=['Buenos Aires','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos',
        'Formosa','Jujuy','La Pampa','La Rioja','Mendoza','Misiones','Neuquén','Río Negro','Salta',
        'San Juan','San Luis','Santa Cruz','Santa Fe','Santiago del Estero','Tierra del Fuego','Tucumán']

        prov = unaProvincia.getNombre()
        
        if prov in provincias:
            #estas provincias no son reconocidas por Open Weather
            if prov=='Chaco':
                prov='Resistencia'
            elif prov=='Jujuy':
                prov='San Salvador de Jujuy'
            elif prov=='Chubut':
                prov='Rawson'
            elif prov=='Tierra del Fuego':
                prov='Ushuaia'

            url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=626c94c3aec2f15e4d9219ba3e2e4940' % (prov)
            r = requests.get(url)
            re = r.json()

            temperatura = str(re['main']['temp'])
            sensacio_termica = str(re['main']['feels_like'])
            humedad = str(re['main']['humidity'])
            values = (unaProvincia.getNombre(),unaProvincia.getCapital(),unaProvincia.getCantidadHabitantes(),unaProvincia.getCantidadDepartamentos(),temperatura+' °',sensacio_termica+' °',humedad+' %')
        else:
            self.limpiar() # se limpian los entry, para que no muestre la temperatura, sensación térmica ni la humedad de otra provincia anterior
            values = (unaProvincia.getNombre(),unaProvincia.getCapital(),unaProvincia.getCantidadHabitantes(),unaProvincia.getCantidadDepartamentos())

        for entry, value in zip(self.entries,values):
            entry.delete(0,tk.END)
            entry.insert(0,value)

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class FormularioNuevaProvincia(tk.LabelFrame):
    fields = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos')
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text = 'Provincia', padx = 10, pady = 10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text = text)
        entry = tk.Entry(self.frame, width = 25)
        label.grid(row = position, column = 0, pady = 5)
        entry.grid(row = position, column = 1, pady = 5)
        return entry

    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror('Error de Validación', str(e), parent = self)
        return provincia


class NewProvincia(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = FormularioNuevaProvincia(self)
        self.title('Nuevo Provincia')
        self.geometry('400x220')
        self.resizable(0,0)
        self.iconbitmap(r'C:\programacion\Ejercicios\Unidad 4\static\argentina.ico')
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

class ProvinciasView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Tiempo de Provincias")
        self.iconbitmap(r'C:\programacion\Ejercicios\Unidad 4\static\tiempo.ico')
        self.list = ProvinciaList(self, height=15)
        self.form = ProvinciaForm(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
        #self.form.bind_save(ctrl.modificarProvincia)
       

    def agregarProvincia(self,unaProvincia):
        self.list.insertar(unaProvincia)

    def modificarProvincia(self,unaProvincia, index):
        self.list.modificar(unaProvincia, index)

   
    #obtiene los valores del formulario y crea un nuevo provincia
    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()

    #Ver estado de provincia en formulario de provincias
    def verProvinciaEnForm(self,unaProvincia):
        self.form.mostrarEstadoProvinciaEnFormulario(unaProvincia)