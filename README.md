# Chat Distribuido

Aplicación de chat cliente-servidor en tiempo real usando TCP sockets, SQLite y Docker.

## Tecnologías

- Python 3 (stdlib: `socket`, `threading`, `sqlite3`)
- SQLite para persistencia de usuarios y mensajes
- Docker / Docker Compose

## Estructura

```
chat-distribuido/
├── client/
│   └── client.py          # Cliente de terminal
├── server/
│   ├── server.py          # Servidor TCP multihilo
│   ├── db.py              # Capa de base de datos SQLite
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

## Cómo ejecutar

### Local (servidor)

```bash
cd server
pip install -r requirements.txt   # sin dependencias externas, opcional
python server.py
```

### Local (cliente)

```bash
cd client
python client.py
```

### Con Docker

```bash
cd docker
docker-compose up --build
```

> El cliente se conecta a `127.0.0.1:5000`. Si el servidor corre en otra máquina, cambia `HOST` en `client/client.py`.

## Usuarios por defecto

| Usuario | Contraseña |
|---------|-----------|
| sergio  | 1234      |
| admin   | admin     |

## Funcionalidades

- Autenticación de usuarios contra SQLite
- Broadcasting de mensajes a todos los clientes conectados
- Persistencia de mensajes en base de datos
- Manejo concurrente de múltiples clientes con hilos
