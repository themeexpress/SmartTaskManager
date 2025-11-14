smart-task-manager/
│
├── backend/                     # FastAPI backend
│   ├── app/
│   │   ├── api/                 # All API routes
│   │   │   ├── v1/              # Versioned API
│   │   │   │   ├── tasks.py
│   │   │   │   ├── projects.py
│   │   │   │   ├── users.py
│   │   │   │   └── analytics.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── core/                # Core configurations
│   │   │   ├── config.py        # Settings (env vars)
│   │   │   ├── security.py      # JWT & auth
│   │   │   └── logging.py
│   │   │
│   │   ├── models/              # ORM models (SQLAlchemy)
│   │   │   ├── task.py
│   │   │   ├── project.py
│   │   │   └── user.py
│   │   │
│   │   ├── schemas/             # Pydantic request/response schemas
│   │   │   ├── task.py
│   │   │   ├── project.py
│   │   │   └── user.py
│   │   │
│   │   ├── services/            # Business logic layer
│   │   │   ├── task_service.py
│   │   │   ├── project_service.py
│   │   │   └── analytics_service.py
│   │   │
│   │   ├── db/                  # Database configuration
│   │   │   ├── base.py          # Base ORM model
│   │   │   └── session.py       # Database session
│   │   │
│   │   ├── main.py              # FastAPI app entrypoint
│   │   └── __init__.py
│   │
│   ├── tests/                   # Backend tests (pytest)
│   │   ├── test_tasks.py
│   │   ├── test_projects.py
│   │   └── test_users.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env                      # Environment variables
│
├── frontend/                     # React + TypeScript frontend
│   ├── public/
│   │   └── index.html
│   │
│   ├── src/
│   │   ├── assets/               # Images, icons, fonts
│   │   ├── components/           # Reusable components
│   │   │   ├── TaskCard.tsx
│   │   │   ├── ProjectCard.tsx
│   │   │   ├── DashboardChart.tsx
│   │   │   └── Notification.tsx
│   │   │
│   │   ├── pages/                # Page components
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Projects.tsx
│   │   │   └── Analytics.tsx
│   │   │
│   │   ├── services/             # API calls (axios/fetch)
│   │   │   ├── taskService.ts
│   │   │   ├── projectService.ts
│   │   │   ├── userService.ts
│   │   │   └── analyticsService.ts
│   │   │
│   │   ├── store/                # State management (Zustand or Redux)
│   │   │   ├── taskStore.ts
│   │   │   └── userStore.ts
│   │   │
│   │   ├── utils/                # Helper functions
│   │   │   └── dateUtils.ts
│   │   │
│   │   ├── App.tsx               # App entrypoint
│   │   ├── index.tsx
│   │   └── routes.tsx
│   │
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
│
├── docker-compose.yml            # Compose for backend + frontend + db
├── .gitignore
└── README.md
