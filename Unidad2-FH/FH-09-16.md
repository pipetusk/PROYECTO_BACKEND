## Unidad 2

Para migrar los datos de la base de datos, usar el siguiente comando:

```
python manage.py migrate
```

- **¿Para qué sirve?** Hay muchos tipos de comandos sobre permisos disponibles en el archivo `db.sqlite3`.

### Modelo de datos

Según el modelo de datos (diagrama de base de datos):

1. Dentro de `models.py` hay que crear las clases, en este caso se usará la tabla "Categoría" como ejemplo:

```
class Categoria(models.Model):
    categoria = models.CharField(max_length=20,null=False)
    descripcion = models.CharField(max_length=100,null=True)
```

2. Cuando esté listo, se crea la migración:

```
python manage.py makemigrations
```

3. Luego hay que aplicar la migración:

```
python manage.py migrate
```

> [!NOTE] 
> Idealmente las migraciones se hacen cuando se termina de trabajar en las clases (Lo de abajo &darr; &darr; &darr;).

4. Ahora se sigue el código anterior para aplicar otras tablas de la base de datos:

```
class Categoria(models.Model):
    categoria = models.CharField(max_length=20,null=False)
    descripcion = models.CharField(max_length=100,null=True)

class Pais(model.Model):
    nombre = models.CharField(max_length=60,null=False)
    nacionalidad = models.CharField(max_length=20,null=False)
    iso_2 = models.CharField(max_length=2,null=False)
    iso_3 = models.CharField(max_length=3,null=False)


class Autor(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    seudonimo = models.CharField(max_length=50,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=False)
```

> [!NOTE] 
> - **Siempre** se hereda desde `models.Model`.
> - Si quiero que el campo sea obligatorio, tiene que estar `null=False`.
> - `on_delete=models.CASCADE` sirve para verificar si existe un dato siendo usado en una *Foreign Key*, si es el caso, la tabla original no se eliminará. (En resumen, *verificar si un dato se está utilizando.*).

> [!NOTE]
> - `CharField` es como un `String`.
> - `ForeignKey` es para las llaves foráneas.
> - `DateField` es para las fechas.
