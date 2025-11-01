// JWT API Helper - Include this in any page that needs to make authenticated requests
// Usage: <script src="/static/js/api-helper.js"></script>

// Function to get the JWT token from localStorage
function getAuthToken() {
    return localStorage.getItem('access_token');
}

// Function to get user role
function getUserRole() {
    return localStorage.getItem('user_role');
}

// Function to check if user is logged in
function isLoggedIn() {
    return !!getAuthToken();
}

// Function to logout
function logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user_role');
    window.location.href = '/login';
}

// Function to make authenticated API calls
async function authenticatedFetch(url, options = {}) {
    const token = getAuthToken();
    
    if (!token) {
        console.error('No auth token found');
        window.location.href = '/login';
        return;
    }

    // Merge headers with authorization
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
        ...options.headers
    };

    try {
        const response = await fetch(url, {
            ...options,
            headers
        });

        // If unauthorized, redirect to login
        if (response.status === 401) {
            logout();
            return;
        }

        return response;
    } catch (error) {
        console.error('API call failed:', error);
        throw error;
    }
}

// Example usage function for GET request
async function getProtectedData(endpoint) {
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'GET'
        });
        
        if (response.ok) {
            return await response.json();
        } else {
            const error = await response.json();
            throw new Error(error.msg || 'Request failed');
        }
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Example usage function for POST request
async function postProtectedData(endpoint, data) {
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            return await response.json();
        } else {
            const error = await response.json();
            throw new Error(error.msg || 'Request failed');
        }
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Example usage function for PUT request
async function updateProtectedData(endpoint, data) {
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            return await response.json();
        } else {
            const error = await response.json();
            throw new Error(error.msg || 'Request failed');
        }
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Example usage function for DELETE request
async function deleteProtectedData(endpoint) {
    try {
        const response = await authenticatedFetch(endpoint, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            return await response.json();
        } else {
            const error = await response.json();
            throw new Error(error.msg || 'Request failed');
        }
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Protect pages that require authentication
function requireAuth() {
    if (!isLoggedIn()) {
        window.location.href = '/login';
    }
}

// Check user role and redirect if not authorized
function requireRole(allowedRoles) {
    const userRole = getUserRole();
    if (!allowedRoles.includes(userRole)) {
        alert('You do not have permission to access this page');
        window.location.href = '/dashboard';
    }
}