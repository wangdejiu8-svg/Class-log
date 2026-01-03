# CLAUDE.md - 班级日志系统项目指南

## 项目概述

班级日志系统是一个面向中学班级的日常管理工具，用于记录班级的值日、出勤、纪律和作业情况。

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | React + Vite + Ant Design |
| 后端 | Django + Django REST Framework |
| 数据库 | PostgreSQL |
| API | RESTful |

## 项目结构（规划）

```
Class-log/
├── frontend/          # React 前端项目
│   ├── src/
│   │   ├── components/   # 通用组件
│   │   ├── pages/        # 页面组件
│   │   ├── services/     # API 服务
│   │   ├── stores/       # 状态管理
│   │   └── utils/        # 工具函数
│   └── package.json
├── backend/           # Django 后端项目
│   ├── apps/
│   │   ├── users/        # 用户管理
│   │   ├── logs/         # 日志管理
│   │   ├── comments/     # 评论功能
│   │   └── notifications/# 通知功能
│   ├── config/           # 项目配置
│   └── requirements.txt
├── PRD.md             # 产品需求文档
├── 需求讨论记录.md      # 需求讨论记录
└── CLAUDE.md          # 本文件
```

## 用户角色

| 角色 | 说明 |
|------|------|
| 学生 | 只能查看日志、发评论 |
| 班长 | 填写值日、出勤、整体情况日志 |
| 纪律委员 | 填写纪律日志 |
| 课代表 | 填写本科目作业日志（6科） |
| 老师 | 管理用户、审批补填申请 |

**注意**: 一人可多角色

## 核心功能模块

### 1. 日志模块
- **班长日志**: 值日生、值日评分、迟到/缺勤学生、整体情况
- **纪律日志**: 课节、科目、违纪学生、违纪类型、纪律评分
- **作业日志**: 科目、作业内容、应交/实交人数、未交学生

### 2. 日志规则
- 当天日志可直接填写
- 历史日志需申请补填，老师审批后才能填写
- 日志可修改、可删除

### 3. 评论区
- 位于首页底部
- 所有用户可发评论、点赞
- 只显示当天评论
- 只能删除自己的评论

### 4. 用户管理
- 学生自行注册，注册即可用
- 老师账号由管理员创建
- 老师可为学生分配角色

### 5. 消息通知
- 站内消息通知
- 新日志提交通知老师
- 违纪通知学生
- 补填申请结果通知

## 开发命令

### 前端 (frontend/)
```bash
npm install          # 安装依赖
npm run dev          # 启动开发服务器
npm run build        # 构建生产版本
npm run lint         # 代码检查
```

### 后端 (backend/)
```bash
pip install -r requirements.txt   # 安装依赖
python manage.py runserver        # 启动开发服务器
python manage.py migrate          # 数据库迁移
python manage.py createsuperuser  # 创建管理员
```

## API 端点概览

| 模块 | 路径前缀 |
|------|----------|
| 认证 | /api/auth/ |
| 用户 | /api/users/ |
| 班长日志 | /api/monitor-logs/ |
| 纪律日志 | /api/discipline-logs/ |
| 作业日志 | /api/homework-logs/ |
| 补填申请 | /api/backfill-requests/ |
| 评论 | /api/comments/ |
| 通知 | /api/notifications/ |
| 首页 | /api/dashboard/ |

## 数据模型

主要数据表：
- `User` - 用户表
- `Role` - 角色表（多对多）
- `MonitorLog` - 班长日志
- `DisciplineLog` - 纪律日志
- `HomeworkLog` - 作业日志
- `BackfillRequest` - 补填申请
- `Comment` - 评论
- `CommentLike` - 点赞
- `Notification` - 通知

## 开发规范

### 前端
- 组件使用 PascalCase 命名
- 使用 Ant Design 组件库
- API 请求统一放在 services/ 目录

### 后端
- 使用 Django REST Framework 序列化器
- API 视图使用 ViewSet
- 权限控制使用 DRF permissions

## 相关文档

- [PRD.md](./PRD.md) - 完整产品需求文档
- [需求讨论记录.md](./需求讨论记录.md) - 需求讨论历史
