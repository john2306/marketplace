from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, correo, nombre, password):
        """Creacion de un usuario sin el comando createsuperuser"""
        if not correo:
            raise ValueError(
                'El usuario debe tener obligatoriamente un correo')
        # normalizo el correo > aparte de validar que sea un correo valido removera los espacios innecesarios
        correo = self.normalize_email(correo)
       
        nuevoUsuario = self.model(correo=correo, nombre=nombre)
        
        nuevoUsuario.set_password(password)
        # sirve para referencia a la base de datos x default en el caso que tengamos varias conexiones a diferentes bases de datos
        nuevoUsuario.save(using=self._db)

        return nuevoUsuario

    def create_superuser(self, correo, nombre, password):
        """Creacion de un super usuario por consola, este metodo se mandara a llamar cuando se haga el uso del comando por la consola"""
        usuario = self.create_user(correo, nombre, password)
        # is_superuser > indicara que usuarios son super usuarios y podra acceder a todas las funcionalidades del panel administrativo
        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.save(using=self._db)
