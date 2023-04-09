acl = input("Ingrese el número de ACL IPv4: ")

if int(acl) >= 1 and int(acl) <= 99:
    print("La ACL " + acl + " es una ACL Estándar")
elif int(acl) >= 100 and int(acl) <= 199:
    print("La ACL " + acl + " es una ACL Extendida")
else:
    print("El número " + acl + " no corresponde a una lista de acceso")
