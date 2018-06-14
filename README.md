# ThermalComfortDjango
Proyecto implementado en python utilizando el framework ágil **Django v1.11**. Incluye dos (2) aplicaciones que consisten en servicios REST de persistencia, el primero utilizando una base de datos relacional (PostgreSQL) y el segundo una base de datos no relacional (MongoDB).

Todos los componentes están desplegados en contenedores **Docker**.

## Actualizar paquetes del Sistema Operativo
```sudo apt-get update```

## Instalar Docker
```
sudo apt-get install -y docker.io
sudo systemctl enable docker.service
```

## Instalar Docker-Compose
```
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Instalar GIT
```
sudo apt-get install -y git
```

## Descargar código fuente del repositorio de curso
```
git clone https://github.com/ISIS2503/ThermalComfortDjango.git
cd ThermalComfortDjango/
```

## Crear archivo .env para almacenar las variables de entorno requeridas
```
nano .env
```

## Colocar el siguiente contenido en el archivo .env y guardar
```
#Environment Variables
SECRET_KEY=51kj1#$3456*2@a%lo3a(4bh5&p0esi%3+f5hlp%g)9khykxuh

POSTGRES_DB=thermalcomfort
POSTGRES_USER=postgres
POSTGRES_PASSWORD=Isis2503*
POSTGRES_HOST=postgresdb
POSTGRES_PORT=5432
PGDATA=/var/lib/postgresql/data/pgdata

MONGODB_HOST=mongodb
MONGODB_PORT=27017
MONGODB_DB=thermalcomfort
```

## Iniciar contenedores
```
sudo docker-compose up
```

## Detener contenedores
```
Ctrl+C
```

## Crear tablas en base de datos relacional (PostgreSQL) y disponer estáticos (JS, CSS, etc.)
```
sudo make migrate
sudo make statics
```

## Iniciar contenedores
```
sudo docker-compose up
```

## Consultar documentación de las APIs
- [API relacional](http://<<DIRECCION_IP>>/sql/docs/).
- [API no relacional](http://<<DIRECCION_IP>>/nosql/docs/).
