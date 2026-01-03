# 班级日志系统 - 产品需求文档 (PRD)

## 1. 文档信息

| 项目 | 内容 |
|------|------|
| 产品名称 | 班级日志系统 |
| 版本 | v1.0 |
| 创建日期 | 2026-01-03 |
| 状态 | 初稿 |

---

## 2. 产品概述

### 2.1 产品背景
班级日志系统是一个面向中学班级的日常管理工具，用于记录班级的值日情况、出勤情况、纪律情况和作业完成情况。系统支持多角色协作，让班长、纪律委员、课代表各司其职，共同维护班级日志。

### 2.2 产品目标
- 规范班级日志的记录流程
- 提高班级管理效率
- 方便老师了解班级日常情况
- 促进班级成员之间的沟通

### 2.3 目标用户
- 学生（普通学生、班长、纪律委员、课代表）
- 老师

---

## 3. 技术架构

| 层级 | 技术选型 |
|------|----------|
| 前端 | HTML + CSS + JavaScript + React + Vite + Ant Design |
| 后端 | Django + Django REST Framework |
| 数据库 | PostgreSQL |
| API风格 | RESTful API |

---

## 4. 用户角色与权限

### 4.1 角色定义

| 角色 | 说明 |
|------|------|
| 学生 | 普通学生，只能查看日志 |
| 班长 | 负责记录值日、出勤、整体情况 |
| 纪律委员 | 负责记录课堂纪律情况 |
| 课代表 | 负责记录本科目作业情况（6科：语文、数学、英语、物理、化学、生物） |
| 老师 | 管理用户、审批补填申请、查看所有日志 |

### 4.2 权限矩阵

| 功能 | 学生 | 班长 | 纪律委员 | 课代表 | 老师 |
|------|------|------|----------|--------|------|
| 查看日志 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 写班长日志 | ❌ | ✅ | ❌ | ❌ | ❌ |
| 写纪律日志 | ❌ | ❌ | ✅ | ❌ | ❌ |
| 写作业日志 | ❌ | ❌ | ❌ | ✅(本科目) | ❌ |
| 发表评论 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 点赞 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 管理用户 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 分配角色 | ❌ | ❌ | ❌ | ❌ | ✅ |
| 审批补填申请 | ❌ | ❌ | ❌ | ❌ | ✅ |

### 4.3 角色说明
- 一人可拥有多个角色（如：某学生同时是班长+数学课代表）
- 系统支持多个老师，权限相同
- 课代表科目：语文、数学、英语、物理、化学、生物（共6科）

---

## 5. 功能模块

### 5.1 用户管理模块

#### 5.1.1 用户注册
- **学生注册**：学生可自行注册账号，注册后即可使用，无需审核
- **老师账号**：由系统预设或管理员创建，不开放注册

#### 5.1.2 用户登录
- 支持用户名/密码登录
- 登录后根据角色显示对应功能

#### 5.1.3 角色管理（老师功能）
- 查看所有学生列表
- 为学生分配/取消角色
- 支持一人多角色

### 5.2 日志模块

#### 5.2.1 班长日志
**填写权限**：班长

**字段说明**：
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| 日期 | Date | 是 | 日志对应日期 |
| 值日生名单 | 多选学生 | 是 | 当天值日的学生 |
| 值日评分 | 数字(1-10) | 是 | 值日情况评分 |
| 值日评价 | 文本 | 否 | 值日情况描述 |
| 迟到学生 | 多选学生 | 否 | 当天迟到的学生 |
| 缺勤学生 | 多选学生 | 否 | 当天缺勤的学生 |
| 整体情况 | 长文本 | 否 | 班级整体情况描述 |

#### 5.2.2 纪律日志
**填写权限**：纪律委员

**字段说明**：
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| 日期 | Date | 是 | 日志对应日期 |
| 课节 | 数字 | 是 | 第几节课 |
| 科目 | 单选 | 是 | 课程科目 |
| 违纪学生 | 多选学生 | 否 | 违纪的学生 |
| 违纪类型 | 多选 | 否 | 说话、睡觉、玩手机等 |
| 违纪描述 | 文本 | 否 | 具体违纪情况 |
| 衣着情况 | 文本 | 否 | 班级衣着情况描述 |
| 整体纪律评分 | 数字(1-10) | 是 | 本节课纪律评分 |

#### 5.2.3 作业日志
**填写权限**：对应科目的课代表

**字段说明**：
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| 日期 | Date | 是 | 日志对应日期 |
| 科目 | 单选 | 是 | 语文/数学/英语/物理/化学/生物 |
| 作业内容 | 长文本 | 是 | 作业具体内容描述 |
| 应交人数 | 数字 | 是 | 应该提交作业的人数 |
| 实交人数 | 数字 | 是 | 实际提交作业的人数 |
| 未交学生 | 多选学生 | 否 | 未提交作业的学生 |

#### 5.2.4 日志操作规则

**编辑与删除**：
- 日志提交后可修改
- 日志提交后可删除
- 只有日志创建者可以编辑/删除自己的日志

**日期限制**：
- 当天日志：可直接填写
- 历史日志补填：需提交补填申请，老师审批通过后才能填写

### 5.3 补填申请模块

#### 5.3.1 申请流程
1. 用户选择需要补填的日期和日志类型
2. 填写补填原因
3. 提交申请
4. 老师审批（通过/拒绝）
5. 审批通过后，用户可填写该日期的日志

#### 5.3.2 申请字段
| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| 补填日期 | Date | 是 | 需要补填的日期 |
| 日志类型 | 单选 | 是 | 班长日志/纪律日志/作业日志 |
| 补填原因 | 文本 | 是 | 说明为何需要补填 |
| 申请状态 | 枚举 | 自动 | 待审批/已通过/已拒绝 |

### 5.4 评论区模块

#### 5.4.1 功能说明
- 位于首页底部
- 所有用户可发表评论
- 所有用户可点赞评论
- 只显示当天的评论（每天自动清空显示）
- 用户可删除自己发的评论，不能删除他人评论

#### 5.4.2 评论字段
| 字段 | 类型 | 说明 |
|------|------|------|
| 内容 | 文本 | 评论内容 |
| 发布者 | 用户 | 评论发布人 |
| 发布时间 | DateTime | 评论时间 |
| 点赞数 | 数字 | 获得的点赞数量 |

### 5.5 消息通知模块

#### 5.5.1 通知方式
- 站内消息通知

#### 5.5.2 通知场景
| 场景 | 接收者 | 说明 |
|------|--------|------|
| 新日志提交 | 老师 | 有新日志提交时通知老师 |
| 填写提醒 | 班长/纪律委员/课代表 | 提醒相关角色填写日志 |
| 违纪通知 | 被记违纪的学生 | 学生被记录违纪时通知该学生 |
| 补填申请结果 | 申请人 | 补填申请审批结果通知 |

---

## 6. 页面设计

### 6.1 页面列表

| 页面 | 访问权限 | 说明 |
|------|----------|------|
| 登录页 | 所有人 | 用户登录 |
| 注册页 | 未登录用户 | 学生注册 |
| 首页/仪表盘 | 已登录用户 | 系统主页 |
| 消息通知页 | 已登录用户 | 查看通知消息 |
| 班长日志列表 | 已登录用户 | 查看班长日志列表 |
| 班长日志详情 | 已登录用户 | 查看单条日志详情 |
| 班长日志编辑 | 班长 | 新建/编辑日志 |
| 纪律日志列表 | 已登录用户 | 查看纪律日志列表 |
| 纪律日志详情 | 已登录用户 | 查看单条日志详情 |
| 纪律日志编辑 | 纪律委员 | 新建/编辑日志 |
| 作业日志列表 | 已登录用户 | 查看作业日志列表 |
| 作业日志详情 | 已登录用户 | 查看单条日志详情 |
| 作业日志编辑 | 课代表 | 新建/编辑日志 |
| 补填申请页 | 班长/纪律委员/课代表 | 提交补填申请 |
| 学生管理页 | 老师 | 管理学生、分配角色 |
| 补填审批页 | 老师 | 审批补填申请 |

### 6.2 首页布局

首页从上到下分为四个区域：

**1. 欢迎区**
- 显示 "Welcome [用户名]"
- 显示用户当前角色/职位

**2. 近期班级日志**
- 展示最近几天的日志列表
- 可快速跳转到日志详情

**3. 待办提醒**
- 显示当前用户需要完成的任务
- 如：今日日志未填写提醒

**4. 当日评论区**
- 显示当天的评论列表
- 支持发表评论和点赞

---

## 7. 数据模型

### 7.1 用户表 (User)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| username | String | 用户名 |
| password | String | 密码(加密) |
| name | String | 真实姓名 |
| user_type | Enum | student/teacher |
| created_at | DateTime | 创建时间 |

### 7.2 角色表 (Role)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| user_id | FK(User) | 用户ID |
| role_type | Enum | monitor/discipline/representative |
| subject | String | 科目(仅课代表需要) |

### 7.3 班长日志表 (MonitorLog)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| date | Date | 日志日期 |
| author_id | FK(User) | 创建者 |
| duty_score | Integer | 值日评分(1-10) |
| duty_comment | Text | 值日评价 |
| overall_situation | Text | 整体情况 |
| created_at | DateTime | 创建时间 |
| updated_at | DateTime | 更新时间 |

### 7.4 班长日志关联表
**值日生关联 (MonitorLogDutyStudent)**
| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | FK(MonitorLog) | 日志ID |
| student_id | FK(User) | 学生ID |

**迟到学生关联 (MonitorLogLateStudent)**
| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | FK(MonitorLog) | 日志ID |
| student_id | FK(User) | 学生ID |

**缺勤学生关联 (MonitorLogAbsentStudent)**
| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | FK(MonitorLog) | 日志ID |
| student_id | FK(User) | 学生ID |

### 7.5 纪律日志表 (DisciplineLog)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| date | Date | 日志日期 |
| period | Integer | 第几节课 |
| subject | String | 科目 |
| author_id | FK(User) | 创建者 |
| violation_desc | Text | 违纪描述 |
| dress_situation | Text | 衣着情况 |
| discipline_score | Integer | 纪律评分(1-10) |
| created_at | DateTime | 创建时间 |
| updated_at | DateTime | 更新时间 |

### 7.6 纪律日志关联表
**违纪学生关联 (DisciplineLogViolationStudent)**
| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | FK(DisciplineLog) | 日志ID |
| student_id | FK(User) | 学生ID |
| violation_type | String | 违纪类型(说话/睡觉/玩手机等) |

### 7.7 作业日志表 (HomeworkLog)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| date | Date | 日志日期 |
| subject | String | 科目 |
| author_id | FK(User) | 创建者 |
| homework_content | Text | 作业内容 |
| expected_count | Integer | 应交人数 |
| actual_count | Integer | 实交人数 |
| created_at | DateTime | 创建时间 |
| updated_at | DateTime | 更新时间 |

### 7.8 作业日志关联表
**未交作业学生关联 (HomeworkLogMissingStudent)**
| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | FK(HomeworkLog) | 日志ID |
| student_id | FK(User) | 学生ID |

### 7.9 补填申请表 (BackfillRequest)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| applicant_id | FK(User) | 申请人 |
| backfill_date | Date | 补填日期 |
| log_type | Enum | 日志类型 |
| reason | Text | 补填原因 |
| status | Enum | pending/approved/rejected |
| reviewer_id | FK(User) | 审批人 |
| reviewed_at | DateTime | 审批时间 |
| created_at | DateTime | 创建时间 |

### 7.10 评论表 (Comment)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| content | Text | 评论内容 |
| author_id | FK(User) | 发布者 |
| like_count | Integer | 点赞数 |
| created_at | DateTime | 发布时间 |

### 7.11 点赞表 (CommentLike)
| 字段 | 类型 | 说明 |
|------|------|------|
| comment_id | FK(Comment) | 评论ID |
| user_id | FK(User) | 点赞用户 |
| created_at | DateTime | 点赞时间 |

### 7.12 通知表 (Notification)
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer | 主键 |
| user_id | FK(User) | 接收用户 |
| title | String | 通知标题 |
| content | Text | 通知内容 |
| is_read | Boolean | 是否已读 |
| created_at | DateTime | 创建时间 |

---

## 8. API设计

### 8.1 认证相关
| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/auth/register | 学生注册 |
| POST | /api/auth/login | 用户登录 |
| POST | /api/auth/logout | 用户登出 |
| GET | /api/auth/me | 获取当前用户信息 |

### 8.2 用户管理（老师）
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/users | 获取学生列表 |
| GET | /api/users/{id} | 获取学生详情 |
| PUT | /api/users/{id}/roles | 更新学生角色 |
| DELETE | /api/users/{id} | 删除学生 |

### 8.3 班长日志
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/monitor-logs | 获取日志列表 |
| GET | /api/monitor-logs/{id} | 获取日志详情 |
| POST | /api/monitor-logs | 创建日志 |
| PUT | /api/monitor-logs/{id} | 更新日志 |
| DELETE | /api/monitor-logs/{id} | 删除日志 |

### 8.4 纪律日志
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/discipline-logs | 获取日志列表 |
| GET | /api/discipline-logs/{id} | 获取日志详情 |
| POST | /api/discipline-logs | 创建日志 |
| PUT | /api/discipline-logs/{id} | 更新日志 |
| DELETE | /api/discipline-logs/{id} | 删除日志 |

### 8.5 作业日志
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/homework-logs | 获取日志列表 |
| GET | /api/homework-logs/{id} | 获取日志详情 |
| POST | /api/homework-logs | 创建日志 |
| PUT | /api/homework-logs/{id} | 更新日志 |
| DELETE | /api/homework-logs/{id} | 删除日志 |

### 8.6 补填申请
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/backfill-requests | 获取申请列表 |
| POST | /api/backfill-requests | 提交申请 |
| PUT | /api/backfill-requests/{id}/approve | 审批通过 |
| PUT | /api/backfill-requests/{id}/reject | 审批拒绝 |

### 8.7 评论
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/comments/today | 获取今日评论 |
| POST | /api/comments | 发表评论 |
| DELETE | /api/comments/{id} | 删除评论 |
| POST | /api/comments/{id}/like | 点赞 |
| DELETE | /api/comments/{id}/like | 取消点赞 |

### 8.8 通知
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/notifications | 获取通知列表 |
| PUT | /api/notifications/{id}/read | 标记已读 |
| PUT | /api/notifications/read-all | 全部标记已读 |

### 8.9 首页
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/dashboard | 获取首页数据 |
| GET | /api/dashboard/recent-logs | 获取近期日志 |
| GET | /api/dashboard/todos | 获取待办事项 |

---

## 9. 非功能性需求

### 9.1 安全性
- 密码加密存储
- API接口需要身份认证
- 权限校验（用户只能操作自己有权限的资源）

### 9.2 性能
- 页面加载时间 < 3秒
- API响应时间 < 500ms

### 9.3 兼容性
- 支持主流浏览器（Chrome、Firefox、Edge、Safari）
- 支持移动端浏览器访问

---

## 10. 附录

### 10.1 枚举值定义

**用户类型 (user_type)**
- student: 学生
- teacher: 老师

**角色类型 (role_type)**
- monitor: 班长
- discipline: 纪律委员
- representative: 课代表

**科目 (subject)**
- chinese: 语文
- math: 数学
- english: 英语
- physics: 物理
- chemistry: 化学
- biology: 生物

**日志类型 (log_type)**
- monitor: 班长日志
- discipline: 纪律日志
- homework: 作业日志

**申请状态 (status)**
- pending: 待审批
- approved: 已通过
- rejected: 已拒绝

**违纪类型**
- talking: 说话
- sleeping: 睡觉
- phone: 玩手机
- other: 其他

---

## 11. 版本历史

| 版本 | 日期 | 修改内容 | 作者 |
|------|------|----------|------|
| v1.0 | 2026-01-03 | 初稿 | - |
