import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => {
    const storedState = localStorage.getItem('authState');
    return storedState
      ? JSON.parse(storedState)
      : {
          user: null,
          isAuthenticated: false,
        };
  },
  actions: {
    async setCsrfToken() {
      try {
        await fetch('http://localhost:8000/api/set-csrf-token/', {
          method: 'GET',
          mode: 'cors',
          credentials: 'include',
        });
      } catch (error) {
        console.error('Failed to set CSRF token', error);
      }
      console.log("CSRF Token: ", getCSRFToken());
    },

    async login(email, password) {
      try {
        await this.setCsrfToken();
        const csrfToken = getCSRFToken();
        console.log("CSRF Token: ", csrfToken); // This will log the CSRF token to the console
        const response = await fetch('/api/login/', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
          body: JSON.stringify({ email, password }),
          credentials: 'include',
        });
        // rest of the code
      } catch (error) {
        console.error('Login error:', error);
        throw error; // Propagate error to be caught in the Vue component
      }
    },

    async register(email, password) {
      try {
        await this.setCsrfToken();
        console.log("CSRF Token: ", getCSRFToken());
        const response = await fetch('/api/register/', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
          },
          body: JSON.stringify({ email, password }),
          credentials: 'include',
        });

        const data = await response.json();

        if (response.ok) {
          return { success: true, message: 'Registration successful' };
        } else {
          throw new Error(data.error || 'Registration failed');
        }
      } catch (error) {
        console.error('Registration error:', error);
        throw error;
      }
    },

    async logout() {
      try {
        const response = await fetch('/api/logout/', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'X-CSRFToken': getCSRFToken(),
          },
          credentials: 'include',
        });

        if (response.ok) {
          this.user = null;
          this.isAuthenticated = false;
          this.saveState();
          // Redirect to login page after logout
          window.location.href = "/login"; // Replace with your login page's Django URL
        } else {
          throw new Error('Logout failed');
        }
      } catch (error) {
        console.error('Logout failed', error);
        throw error; // Propagate error to be handled
      }
    },

    async fetchUser() {
      try {
        await this.setCsrfToken();
        const response = await fetch('/api/user/', {
          credentials: 'include',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
          },
        });

        if (response.ok) {
          const data = await response.json();
          this.user = data;
          this.isAuthenticated = true;
        } else {
          this.user = null;
          this.isAuthenticated = false;
        }
      } catch (error) {
        console.error('Failed to fetch user', error);
        this.user = null;
        this.isAuthenticated = false;
      }
      this.saveState();
    },

    saveState() {
      localStorage.setItem('authState', JSON.stringify({
        user: this.user,
        isAuthenticated: this.isAuthenticated,
      }));
    },
  },
});

// Utility function to retrieve CSRF token from the cookie
export function getCSRFToken() {
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log("CSRF Token: ", cookieValue); // This will log the CSRF token to the console
    return cookieValue;
}