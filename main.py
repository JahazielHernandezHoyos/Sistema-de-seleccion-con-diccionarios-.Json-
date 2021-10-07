def Seleccion(info: dict):
    respuesta = []
    masAlto = 0
    listaCodigos = []
    for e in info:
        listaCodigos.append(e)

    for i in range(0, len(listaCodigos)):
        
        sumatoria = 0
        sumatoriaCreditos = 0
        for m in info[listaCodigos[i]]["materias"]:
            if m["retirada"] == "No":
                sumatoria = sumatoria + (m["nota"]* m["creditos"])
                sumatoriaCreditos = sumatoriaCreditos + m["creditos"]

        if sumatoriaCreditos > 0:
            promedio = sumatoria / sumatoriaCreditos
        else:
            promedio = 0

        if promedio > masAlto:
            masAlto = promedio
            codigoMasAlto = listaCodigos[i]
            estudianteMasAlto = info[listaCodigos[i]]
            
        elif promedio == masAlto:
                
            if str(codigoMasAlto) > str(listaCodigos[i]):
                    
                codigoMasAlto = listaCodigos[i]
                estudianteMasAlto = info[listaCodigos[i]]
        
    iniciales = estudianteMasAlto['nombres'][0] 
    for b in range (0,len(  estudianteMasAlto['nombres']      )):
        if estudianteMasAlto['nombres'][b]== " ":
           #print("si entre por aca")
           segundonombre=estudianteMasAlto['nombres'][b+1]
           iniciales = iniciales+segundonombre
    iniciales=iniciales.swapcase()

    for b in range (0,len(  estudianteMasAlto['apellidos']      )):
        if estudianteMasAlto['apellidos'][b]== ",":
           primer_apellido=estudianteMasAlto['apellidos'][0:b]
           primer_apellido=primer_apellido.lower()
    
    digitos_documento=estudianteMasAlto['documento']
    digitos_documento=str(digitos_documento)
    #print(digitos_documento[-1])
    
    correo=iniciales+"."+primer_apellido+digitos_documento[-2]+digitos_documento[-1]
                ######################################################
    nombres = estudianteMasAlto["nombres"]
    apellidos = estudianteMasAlto["apellidos"]
    listaNombres = nombres.split()
    listaApellidos = apellidos.split()
    documentoCadena = str(estudianteMasAlto["documento"])
    
    cantidadNombres = len(listaNombres)

    correo = correo.lower()
    correo = correo.replace("á", "a")
    correo = correo.replace("é", "e")
    correo = correo.replace("í", "i")
    correo = correo.replace("ó", "o")
    correo = correo.replace("ú", "u")
    correo = correo.replace(",", "")

    respuesta.append(codigoMasAlto)
    respuesta.append(estudianteMasAlto["nombres"])
    respuesta.append(estudianteMasAlto["apellidos"])
    respuesta.append(estudianteMasAlto["documento"])
    respuesta.append(estudianteMasAlto["programa"])
    respuesta.append(masAlto)
    respuesta.append(correo)

    return respuesta
    


diccionario={
    20170136837:{
    "nombres" : "Juan",
    "apellidos" : "Moreno, Herrera",
    "documento" : 88481595,
    "programa" : "ARQU",
    "materias" : [
    {
    "facultad" : "Arquitectura",
    "codigo" : "ARQU-8218",
    "nota" : 4.49,
    "creditos" : 3,
    "retirada" : "No",
    },
    {
    "facultad" : "Arquitectura",
    "codigo" : "ARQU-2113",
    "nota" : 2.97,
    "creditos" : 2,
    "retirada" : "Si",
    },
    {
    "facultad" : "Arquitectura",
    "codigo" : "ARQU-5048",
    "nota" : 4.26,
    "creditos" : 1,
    "retirada" : "No",
    },
    ]
    },
    20130225137:{
    "nombres" : "Sara Carolina",
    "apellidos" : "Gómez, Fernández",
    "documento" : 58770043,
    "programa" : "ARQD",
    "materias" : [
    {
    "facultad" : "Arquitectura",
    "codigo" : "ARQD-7738",
    "nota" : 3.36,
    "creditos" : 3,
    "retirada" : "No",
    },
    {
    "facultad" : "Arquitectura",
    "codigo" : "ARQD-9115",
    "nota" : 2.62,
    "creditos" : 1,
    "retirada" : "No",
    },
    {
    "facultad" : "Arquitectura",
    "codigo" : "ARQD-7698",
    "nota" : 1.59,
    "creditos" : 4,
    "retirada" : "Si",
    },
    ]
    },
    20110274333:{
    "nombres" : "Carolina Paula",
    "apellidos" : "Ochoa, López",
    "documento" : 82364435,
    "programa" : "DIMD",
    "materias" : [
    {
    "facultad" : "Diseño",
    "codigo" : "DIMD-7972",
    "nota" : 3.15,
    "creditos" : 1,
    "retirada" : "No",
    },
    ]
    },
    20160219974:{
    "nombres" : "Daniela Sara",
    "apellidos" : "Cuellar, Guitiérrez",
    "documento" : 80398132,
    "programa" : "IIND",
    "materias" : [
    {
    "facultad" : "Ingenieria",
    "codigo" : "IIND-3557",
    "nota" : 3.91,
    "creditos" : 1,
    "retirada" : "No",
    },
    {
    "facultad" : "Ingenieria",
    "codigo" : "IIND-5158",
    "nota" : 3.83,
    "creditos" : 3,
    "retirada" : "No",
    },
    {
    "facultad" : "Ingenieria",
    "codigo" : "IIND-7543",
    "nota" : 3.41,
    "creditos" : 3,
    "retirada" : "No",
    },
    ]
    },
                        20150264705:{
    "nombres" : "Julio",
    "apellidos" : "Fernández, Perez",
    "documento" :1123697671,
    "programa" : "DIIN",
    "materias" : [
    {
    "facultad" : "Diseño",
    "codigo" : "DIIN-7888",
    "nota" : 4.68,
    "creditos" : 2,
    "retirada" : "No",
    },
    {
    "facultad" : "Diseño",
    "codigo" : "DIMD-4014",
    "nota" : 3.15,
    "creditos" : 3,
    "retirada" : "No",
    },
    ]
    },
    20150222512:{
    "nombres" : "Mateo Gabriel",
    "apellidos" : "Niño, Romero",
    "documento" : 12964051,
    "programa" : "DIMD",
    "materias" : [
    {
    "facultad" : "Diseño",
    "codigo" : "DIMD-3683",
    "nota" : 3.6,
    "creditos" : 2,
    "retirada" : "No",
    },
    {
    "facultad" : "Diseño",
    "codigo" : "DIMD-4014",
    "nota" : 3.15,
    "creditos" : 3,
    "retirada" : "No",
    },
    {
    "facultad" : "Diseño",
    "codigo" : "DIMD-1670",
    "nota" : 4.75,
    "creditos" : 2,
    "retirada" : "No",},],},}

print(Seleccion(diccionario))
