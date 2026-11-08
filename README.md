# ChatOps Discord

Bot de Discord con comandos de estado e información del servidor y entorno Docker Compose con Prometheus y Grafana.

## Funciones

- Comandos !ping, !estado e !info.
- Registro de eventos del bot.
- Servicios Prometheus y Grafana incluidos en Docker Compose.

## Tecnologías

Python, discord.py, Docker Compose, Prometheus y Grafana.

## Inicio local

```bash
cp .env.example .env
# Configura tu token de Discord en .env
docker compose up --build
```

Grafana: http://localhost:3000 · Prometheus: http://localhost:9090

## Configuración y alcance

Crear una aplicación/bot en Discord, habilitar Message Content Intent y Server Members Intent e invitarlo al servidor con permisos adecuados. !info requiere permisos de administrador. Prometheus y Grafana se incluyen como servicios; no se ha implementado un exportador de métricas del bot. Configurar las credenciales de Grafana mediante .env.

## Estado de validación

Se preparó el código para su revisión como proyecto de portafolio. La validación estática no sustituye las pruebas de instalación ni las pruebas funcionales en cada equipo.

## Autor y perfil

Portafolio de [mrx117w](https://github.com/mrx117w). Las bibliotecas y herramientas utilizadas pertenecen a sus respectivos autores.
