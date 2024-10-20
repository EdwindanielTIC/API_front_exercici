# Projecte-activitat1
Hemos creado en primer lugar la base de datos con heidiSQL, he creado la base de datos llamada alumnat, y despues he creado alumne y aula.
Cabe destacar que idAlumne PKI y idaula FRK. Asi esta relacionado con la aula.
Captura de los datos que tengo en alumne,

![image](https://github.com/user-attachments/assets/e3bc194e-310f-4636-a860-24923fd19b20)
Como podemos ver, esos datos que nos aparecen son agreados manualmente desde heidiSQl.

Los datos que le di a cada apartado son los siguientes: 
Los puntos que he de destacar son el createDat y Updatead que les he puesto TIMESTAMP PARA QUE SE ME ACTUALIZE LA FECHA,  TAMBIEN HE PUESTO CURRENT_TIMESTAMPS.


![image](https://github.com/user-attachments/assets/acb9d51b-a04f-4df9-b6ff-a688395bf47b)

*MIS DATOS DE AULA SON LOS SIGUIENTE:*

como se puede observar, la llave primaria es idAula
![image](https://github.com/user-attachments/assets/b60409f6-6708-4992-9372-8516494af9d2)

## CAPTURA DE FUNCIONAMENTO DE FATAPI

###alumne/list
tengo la siguinete imagen, pero esta no me funciona bien, lo he intendado arreglar, pero no se donde esta mi problema. Auqne cabe destacar que la informacion que tengo en el codigo es correcta.
![image](https://github.com/user-attachments/assets/0df3368d-e989-4ba6-b88d-c4ebf68ffe2d)

### alumne /show 
Este punto no funciona correctamente. Los he estado probanco con postman tambien y no se donde esta el error. 
![image](https://github.com/user-attachments/assets/bc4679b5-101d-44ec-bc19-a6b8b37261c6)

### POST /alumne/add
vemos que funciona al perfeccion. 
captura de como añado los campos : 
![image](https://github.com/user-attachments/assets/53919ef4-09b6-49fd-b405-4efbeb820e62)
El programa me lanza un mensaje confome a que se añadio correctamente 
![image](https://github.com/user-attachments/assets/db041afc-0eb6-4839-a6e7-eac7bd44a098)
En heidiSql me aparece lo siguiente sin actualizar
![image](https://github.com/user-attachments/assets/057eb5d2-e4f3-4e88-9f53-cf425a4e39f4)
una vez actualizado me aparece el alumno 
![image](https://github.com/user-attachments/assets/c8902e47-3cc9-45d0-b36b-fd0c8e48536b)



### PUT ALUMNE/UPDATE/
FUNCIONA PERFECTO 
![image](https://github.com/user-attachments/assets/519423e7-30d6-4522-a838-c46c043cd8da)
![image](https://github.com/user-attachments/assets/23672f9c-4c28-45c2-87e5-660f4e55971b)


#### FUNCION DELETE 
Podemos ver a continuacion la funcion funciona a la perfeccion
![image](https://github.com/user-attachments/assets/bd2b7f6f-2aae-4963-951e-d035de6d04c5)
***Antes de ser elimnado*** 
![image](https://github.com/user-attachments/assets/6ca39909-6f24-4571-b19f-347c4a983913)
***Despues de ser elimnado***
![image](https://github.com/user-attachments/assets/98aaffbd-ca8b-4199-857f-ed2ef1555b30)

### GET ALUMNE/LISTALL FUNCIONA CORRECTAMENTE, ADJUNTO CAPTURA 
![image](https://github.com/user-attachments/assets/dd4b8441-0468-4c47-9812-6ac4ebc75cdc)
![image](https://github.com/user-attachments/assets/492e86bd-6dda-4351-9a50-cef2faa348e2)






