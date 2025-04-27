import os
students = [] # 👈🏼 Creando una lista vacia que contendra los datos de los estudiantes
while True:
    count = 1
    opcion = input('\nOpciones:   (1) Listado de estudiantes   (2) Registrar estudiantes    (3) Eliminar estudiantes  (4) Salir\n\nOpcion: ')
    
    if opcion == '1':
        total_students = '✅ Solo hay un estudiante registrado' if len(students) == 1 else f'✅ Hay un total de {len(students)} registrados'
        if len(students) == 0:
            print('❌ No hay estudiantes registrados')
        else: 
            print(f'\n{total_students}')
            for student in students:
                for key, value in student.items():
                    print(f'\n Nombre: {value['nombre'].capitalize()} {value['apellido'].capitalize()}\n',
                          f'Cedula: {key}\n Primera nota: {value["nota_1"]}\n Segunda nota: {value["nota_2"]}\n',
                          f'Tercera nota: {value["nota_3"]}\n Promedio: {value["promedio"]}\n','_' * 16
                          )
                    count += 1
            
    elif opcion == '2':
        while True: 
            
            cedula = input('Ingrese el numero de cedula del estudiante: ')
            valid_cedula = True
            if cedula.isdigit() and 7 <= len(cedula) <= 8:
                for student in students:
                    if cedula in student.keys():
                        valid_cedula = False
                        break
                if not valid_cedula:
                    print('\n El estudiante ya se encuentra registrado\n')
                    break
                notas = []
                while True:
                    name = input('Ingrese el nombre del estudiante: ').strip()
                    valid_name = all(not char.isdigit() for char in name)
                    if len(name) >= 3 and valid_name:
                        while True:
                            last_name = input('Ingrese el apellido del estudiante: ')
                            valid_last_name = all(not char.isdigit() for char in last_name)
                            if len(last_name) >= 3 and valid_last_name:
                                break
                            elif not valid_last_name:
                                print('\n❌ El apellido no puede contener numeros\n')
                            else:
                                print('\n❌ El apellido es demasiado corto\n')
                        break
                    elif not valid_name:
                        print('\n❌ El nombre no puede contener numeros\n')
                    else:
                        print('\n❌ El nombre es demasiado corto\n')
                while len(notas) < 3:
                    nota = input(f'Ingrese la nota {count} del estudiante: ')
                    if nota.isdigit():
                        nota = int(nota)
                        if nota >= 0 and nota <=20:
                            nota = int(nota)
                            notas.append(nota)
                            count += 1
                        else:
                            print('\n❌ Ingrese una nota en un rango del 0 al 20\n')
                    else:
                        print('\n❌ ha ocurrido un error, intente ingresar la nota de nuevo\n')
                        
                promedio = (notas[0] + notas[1] + notas[2]) / 3
                print(promedio)
                student = {f'{cedula}':{'nombre': name,'apellido': last_name, 'nota_1': notas[0], 'nota_2': notas[1], 'nota_3': notas[2], 'promedio': round(promedio, 1)}}
                students.append(student)
                os.system('cls')
                print('✅ Estudiante agregado con exito!!!\n')
                break
            else:
                if cedula.isdigit():
                    print('❌ El numero de cedula debe contener minimo 7 caracteres y maximo 8 caracteres')
                else:
                    print('❌ Solo puede contener datos numericos')
        
    
    elif opcion == '3':
        count = 0
        while True:
            target_student = input('\nIndique la cedula del estudiante que desea eliminar: ')
            valid_cedula = True
            if target_student.isdigit() and 7 <= len(target_student) <= 8:
                for student in students:
                    if target_student in student.keys():
                        print('Estudiante eliminado ✅\n')
                        students.pop(count)
                        break
                    count += 1
                if valid_cedula:
                    print('\nEl estudiante no se encuentra registrado\n')
                    break
            else:
                if target_student.isdigit():
                    print('❌ El numero de cedula debe contener minimo 7 caracteres y maximo 8 caracteres')
                else:
                    print('❌ Solo puede contener datos numericos')
        
    elif opcion == '4':
        os.system('cls')
        break