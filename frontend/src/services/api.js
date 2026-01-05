const API_BASE_URL = '/api'

const request = async (url, options = {}) => {
  const config = {
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    ...options,
  }

  const response = await fetch(`${API_BASE_URL}${url}`, config)
  const data = await response.json()

  if (!response.ok) {
    throw new Error(data.message || '请求失败')
  }
  return data
}

const api = {
  login: async (username, password) => {
    const response = await request('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    })
    if (response.success) {
      localStorage.setItem('username', username)
      localStorage.setItem('isLoggedIn', 'true')
    }
    return response
  },

  logout: async () => {
    localStorage.removeItem('username')
    localStorage.removeItem('isLoggedIn')
    return { success: true, message: '退出登录成功' }
  },

  register: async (userData) => {
    return await request('/auth/register', {
      method: 'POST',
      body: JSON.stringify(userData),
    })
  },

  getCurrentUser: async () => {
    return await request('/auth/me')
  }
}

export default api
