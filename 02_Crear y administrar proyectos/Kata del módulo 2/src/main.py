from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=10, weeks=-.3, hour=23)

print(now)

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process agregar esa línea de codigo antes de ingresar a la carpeta env