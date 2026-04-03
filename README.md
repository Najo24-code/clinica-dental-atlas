# Gestion De Pacientes Para Clinica Dental Con Citas Y

![CI](https://github.com/Najo24-code/gestion-de-pacientes-para-clinica-dental-con-citas-y/workflows/CI/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

gestion de pacientes para clinica dental con citas y tratamientos

## ✨ Features

- ✅ API REST completa con FastAPI
- ✅ Autenticación JWT segura
- ✅ Frontend multi-entidad responsive
- ✅ Docker ready para deploy
- ✅ Tests automatizados
- ✅ CI/CD con GitHub Actions

## 🖼️ Screenshots

<div align="center">
  <img src="docs/screenshot-login.png" alt="Login" width="400">
  <img src="docs/screenshot-dashboard.png" alt="Dashboard" width="400">
</div>

## 🚀 Quick Start

### Con Docker (recomendado)
```bash
docker-compose up -d
```

Abre http://localhost:8000

### Manual
```bash
# Clonar
git clone https://github.com/Najo24-code/gestion-de-pacientes-para-clinica-dental-con-citas-y.git
cd gestion-de-pacientes-para-clinica-dental-con-citas-y

# Instalar dependencias
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Ejecutar
uvicorn main:app --reload
```

## 📁 Estructura del Proyecto
```
gestion-de-pacientes-para-clinica-dental-con-citas-y/
├── main.py              # Entry point FastAPI
├── auth.py              # Autenticación JWT
├── models.py            # Modelos SQLAlchemy
├── schemas.py           # Schemas Pydantic
├── database.py          # Configuración DB
├── routes/              # Endpoints API
├── frontend/
│   └── index.html       # Frontend SPA
├── tests/               # Tests unitarios
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🔌 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/auth/register` | Crear cuenta |
| POST | `/auth/login` | Iniciar sesión |
| GET | `/auth/me` | Usuario actual |
| GET | `/items/` | Listar items |
| POST | `/items/` | Crear item |
| GET | `/items/{id}` | Obtener item |
| PUT | `/items/{id}` | Actualizar item |
| DELETE | `/items/{id}` | Eliminar item |

## 🧪 Tests
```bash
pytest tests/ -v
```

## 🐳 Docker
```bash
# Build
docker build -t gestion-de-pacientes-para-clinica-dental-con-citas-y .

# Run
docker run -p 8000:8000 gestion-de-pacientes-para-clinica-dental-con-citas-y
```

## 📝 Variables de Entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `DATABASE_URL` | URL de la base de datos | `sqlite:///./data/app.db` |
| `JWT_SECRET` | Secreto para tokens JWT | (requerido) |
| `JWT_ALGORITHM` | Algoritmo JWT | `HS256` |

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu branch (`git checkout -b feature/nueva-feature`)
3. Commit tus cambios (`git commit -m 'Add nueva feature'`)
4. Push al branch (`git push origin feature/nueva-feature`)
5. Abre un Pull Request

## 📄 License

MIT © 2026 [Najo24-code](https://github.com/Najo24-code)

---

<div align="center">
  <sub>Built with ❤️ using FastAPI + Python</sub>
</div>
