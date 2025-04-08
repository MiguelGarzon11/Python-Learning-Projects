# 1. Inicialización y Representación. 

# __init__	Constructor (se ejecuta al crear el objeto)
# __del__	Destructor (se ejecuta al eliminar el objeto)
# __str__	Representación legible (print(obj))
# __repr__	Representación técnica (repr(obj))
# __format__	Personaliza format(obj)
# __bytes__	Devuelve bytes: bytes(obj)

# 2. Operadores Aritméticos.

# __add__	+
# __sub__	-
# __mul__	*
# __truediv__	/
# __floordiv__	//
# __mod__	%
# __pow__	**
# __neg__	-obj
# __pos__	+obj

# 3. Comparación

# __eq__	==
# __ne__	!=
# __lt__	<
# __le__	<=
# __gt__	>
# __ge__	>=

# 4. Tamaño y Contenido

# __len__	Longitud: len(obj)
# __getitem__	Acceder por índice: obj[i]
# __setitem__	Asignar por índice: obj[i] = x
# __delitem__	Eliminar por índice: del obj[i]
# __contains__	Usado por in: x in obj
# __iter__	Iterador: for x in obj
# __next__	Siguiente elemento en iteración
# __reversed__	reversed(obj)

# 5. Atributos y llamadas.

# __getattr__	Cuando accedes a un atributo que no existe
# __getattribute__	Se ejecuta siempre al acceder a cualquier atributo
# __setattr__	Al asignar atributos: obj.atrib = valor
# __delattr__	Al eliminar atributos: del obj.atrib
# __dir__	Personaliza dir(obj)
# __call__	Permite llamar al objeto como función: obj()