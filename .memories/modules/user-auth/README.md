# 用户认证模块

## 概述

用户认证模块负责处理用户注册、登录、登出等身份验证功能。

## 功能文档

| 文档 | 说明 |
|------|------|
| [PRD.md](./PRD.md) | 产品需求文档 |
| [FUNCTION-REGISTER.md](./FUNCTION-REGISTER.md) | 注册功能 |
| [FUNCTION-LOGIN.md](./FUNCTION-LOGIN.md) | 登录功能 |

## 代码位置

| 层级 | 路径 |
|------|------|
| 后端视图 | `backend/apps/users/views.py` |
| 后端模型 | `backend/apps/users/models.py` |
| 后端路由 | `backend/apps/users/urls.py` |
| 前端API | `frontend/src/services/api.js` |

## 依赖

- Django 认证系统
- django-cors-headers（跨域支持）
