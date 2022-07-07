import tkinter as tk

from tkinter import messagebox

from clasePaciente import Paciente

class PacienteList(tk.Frame):

    def __init__(self, master,**kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self,**kwargs)
        scroll = tk.Scrollbar(self,command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, unPaciente, index=tk.END):
        text = "{}, {}".format(unPaciente.getApellido(), unPaciente.getNombre())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, unPaciente, index):
        self.borrar(index)
        self.insertar(unPaciente, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class PacienteForm(tk.LabelFrame):
    fields = ("Apellido","Nombre","Teléfono","Altura","Peso")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
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

    def mostrarEstadoPacienteEnFormulario(self, unPaciente):
        # a partir de un paciente, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (unPaciente.getApellido(), unPaciente.getNombre(),unPaciente.getTelefono(),unPaciente.getAltura(),unPaciente.getPeso())
        for entry, value in zip(self.entries,values):
            entry.delete(0,tk.END)
            entry.insert(0,value)

    def crearPacienteDesdeFormulario(self):
        #obtiene los valores de los campos del formulario
        #para crear un nuevo paciente
        values = [e.get() for e in self.entries]
        unPaciente=None
        try:
            unPaciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return unPaciente

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NewPaciente(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.form = PacienteForm(self)
        self.title('Nuevo Paciente')
        self.geometry('300x260')
        self.resizable(0,0)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.paciente = self.form.crearPacienteDesdeFormulario()
        if self.paciente:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente


class UpdatePacienteForm(PacienteForm):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_imc = tk.Button(self, text='Ver IMC')
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_imc.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

    def bind_imc(self,callback):
        self.btn_imc.config(command=callback)


class PacientesView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = PacienteList(self, height=15)
        self.form = UpdatePacienteForm(self)
        self.btn_new = tk.Button(self, text="Agregar Paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_imc(ctrl.mostrarImc)

    def agregarPaciente(self,unPaciente):
        self.list.insertar(unPaciente)

    def modificarPaciente(self,unPaciente, index):
        self.list.modificar(unPaciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    #obtiene los valores del formulario y crea un nuevo paciente
    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()

    #Ver estado de paciente en formulario de pacientes
    def verPacienteEnForm(self,unPaciente):
        self.form.mostrarEstadoPacienteEnFormulario(unPaciente)


class Imc(tk.Toplevel):
    fields = ('IMC', 'Composición Corporal')

    def __init__(self, parent):
        super().__init__(parent)
        self.imc = None
        self.title('IMC')
        self.geometry('300x100')#ajustar
        self.resizable(0,0)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
        
        self.btn_back = tk.Button(self, text = 'Volver', command = self.volver)
        self.btn_back.pack(side = tk.BOTTOM, pady = 5)

    def volver(self):
        self.destroy()

    def mostrarEstadoPacienteEnFormulario(self, imc, comp):
        values = (imc, comp)
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def resolver_imc(self, paciente):
        resultado = int(paciente.getPeso()) / (int(paciente.getAltura()) / 100)**2
        if resultado < 18.5:
            composicion_corporal = 'Peso inferior al normal'
        elif 18.5 <= resultado <= 24.9:
            composicion_corporal = 'Peso normal'
        elif 25 <= resultado <= 29.9:
            composicion_corporal = 'Peso superior al normal'
        elif resultado >= 30:
            composicion_corporal = 'Obesidad'
        self.mostrarEstadoPacienteEnFormulario(f'{resultado:.2f}', composicion_corporal)

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text = text)
        entry = tk.Entry(self.frame, width = 25)
        label.grid(row = position, column = 0, pady = 5)
        entry.grid(row = position, column = 1, pady = 5)
        return entry

    def show(self):
        self.grab_set()
        self.wait_window()