# 注册功能

## 接口

- **URL**: `/api/auth/register`
- **方法**: POST
- **Content-Type**: application/json

## 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 用户名，至少3字符 |
| password | string | 是 | 密码，至少6字符 |
| name | string | 是 | 真实姓名 |

## 响应

```json
{
  "success": true,
  "message": "注册成功",
  "data": {
    "username": "xxx",
    "name": "xxx"
  }
}
```

## 代码位置

- 后端: `backend/apps/users/views.py:45` - `register_view`
