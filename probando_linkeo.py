import ctypes as C
libp = C.CDLL('./src/libprueba.so')

tres_i=C.c_int(3)
cuatro_i=C.c_int(4)
res_i=C.c_int()

tres_f=C.c_float(3)
cuatro_f=C.c_float(4)
res_f=C.c_float()

libp.add_int_ref(C.byref(tres_i), C.byref(cuatro_i),C.byref(res_i))
print(res_i)
libp.add_float_ref(C.byref(tres_f),C.byref(cuatro_f),C.byref(res_f))
print(res_f)
#pruebo vectores

in1=(C.c_int*3)(1,3,4)
in2=(C.c_int*3)(0,-1,3)
out=(C.c_int*3)(0,0,0)

libp.add_int_array(C.byref(in1),C.byref(in2),C.byref(out),C.c_int(3))

