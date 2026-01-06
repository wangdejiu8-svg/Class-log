# 登录功能

## 接口

- **URL**: `/api/auth/login`
- **方法**: POST
- **Content-Type**: application/json

## 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 用户名 |
| password | string | 是 | 密码 |

## 响应

```json
{
  "success": true,
  "message": "登录成功",
  "data": {
    "username": "xxx",
    "name": "xxx",
    "user_type": "student"
  }
}
```

## 代码位置

- 后端: `backend/apps/users/views.py:17` - `login_view`
