# 🧭 Project: Smart Task Manager "ZenTask" with Analytics Dashboard

## 1️⃣ Project Overview
**Goal:**  
Build a modern web-based task management system that helps individuals and teams manage tasks, set priorities, track progress, and analyze productivity through visual analytics.

**Purpose:**  
To provide a user-friendly productivity tool with **real-time task tracking**, **progress analytics**, and **team collaboration features**, all accessible via a clean React + TypeScript interface backed by FastAPI.

---

## 2️⃣ Target Users
1. **Individual Professionals** — freelancers or remote workers managing personal tasks.  
2. **Small Teams** — groups of 2–10 people managing shared projects.  
3. **Managers/Leads** — who want to view productivity analytics and team performance.

---

## 3️⃣ Core Functionalities (MVP)

### 🟢 **1. User Authentication & Authorization**
- Register, login, logout with **JWT authentication**.  
- Role-based access:  
  - **Admin:** Manage team, view all tasks.  
  - **Member:** Create, edit, and complete own tasks.  
- Password reset via email (optional for MVP).  

---

### 🟢 **2. Task Management**
- Create, edit, and delete tasks.  
- Tasks include:  
  - Title  
  - Description  
  - Priority (Low, Medium, High)  
  - Status (To Do, In Progress, Completed)  
  - Due date  
  - Assignee (for team mode)  
- Filter/sort tasks by status, priority, or due date.  
- Drag-and-drop task status (Kanban board view).  

---

### 🟢 **3. Project & Team Management**
- Create multiple projects.  
- Invite members to a project via email.  
- Each project has its own task board.  
- Assign tasks to specific members.  

---

### 🟢 **4. Analytics Dashboard**
- **Visualize productivity trends** using charts (e.g., Recharts / Chart.js).  
- Metrics include:  
  - Tasks completed per week/month.  
  - Overdue tasks count.  
  - Task completion rate (%) per user.  
  - Average completion time per task.  
- Filter analytics by user, project, and date range.  

---

### 🟢 **5. Notifications & Activity Log**
- Real-time notification when a task is assigned or updated.  
- Activity feed (e.g., “John marked task ‘API Integration’ as Completed”).  
- Optional push/email notification for updates.

---

## 4️⃣ Future Enhancements (Phase 2+)
- Google Calendar or Slack integration.  
- Dark mode toggle.  
- AI-based productivity tips (“You completed most tasks in the morning — keep that routine!”).  
- Time tracking (start/stop timer for each task).  
- Export analytics as PDF reports.

---

## 5️⃣ Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | React + TypeScript + TailwindCSS + Zustand/Redux |
| **Backend** | FastAPI + PostgreSQL + SQLAlchemy |
| **Authentication** | JWT (PyJWT or FastAPI Users) |
| **DevOps** | Docker, Nginx, GitHub Actions CI/CD, AWS EC2 or ECS |
| **Analytics** | Chart.js / Recharts |
| **Database ORM** | SQLAlchemy / Tortoise ORM |
| **API Documentation** | FastAPI Swagger / Redoc |
| **Testing** | Pytest + Jest |
| **Deployment** | Docker Compose + AWS (or Render for MVP) |

---

## 7️⃣ User Stories (Agile Format)

| ID | User Story | Acceptance Criteria |
|----|-------------|---------------------|
| US-01 | As a user, I want to register and log in securely so that I can access my dashboard. | User can register, log in, and receive JWT tokens. |
| US-02 | As a user, I want to create and edit tasks so that I can manage my work. | Tasks are saved and editable in the database. |
| US-03 | As a manager, I want to assign tasks to members so that everyone knows their responsibilities. | Task has an assigned user field. |
| US-04 | As a user, I want to view analytics of completed tasks. | Dashboard shows graphs for completed vs pending tasks. |
| US-05 | As a team member, I want to receive notifications when tasks are updated. | Notification triggered on task update. |

---

## 8️⃣ DevOps Requirements
- **Version Control:** GitHub repository with separate frontend/backend folders.  
- **CI/CD Pipeline:** GitHub Actions for:
  - Lint + test → build → deploy pipeline.  
- **Containerization:** Each service in Docker (frontend, backend, db, nginx).  
- **Deployment:** AWS EC2 or ECS with load balancing.  
- **Monitoring:** Optional Prometheus + Grafana (later phase).  
- **Logs:** Structured logging using `loguru` in FastAPI and `winston` in React.

---

## 9️⃣ Deliverables
- ✅ Fully functional web app (MVP)  
- ✅ RESTful API documentation (Swagger UI)  
- ✅ Docker Compose setup for local development  
- ✅ CI/CD pipeline YAML  
- ✅ ReadMe file with architecture diagram and setup instructions  
