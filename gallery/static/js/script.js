// Set initial theme based on user preference or default to light
const currentTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-bs-theme', currentTheme);

// Update the toggle button text
const themeToggleButton = document.getElementById('themeToggle');
themeToggleButton.textContent = currentTheme === 'light' ? 'Switch to Dark Mode' : 'Switch to Light Mode';

themeToggleButton.addEventListener('click', () => {
    // Toggle between light and dark
    const newTheme = document.documentElement.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-bs-theme', newTheme);

    // Save preference to localStorage
    localStorage.setItem('theme', newTheme);

    // Update button text
    themeToggleButton.textContent = newTheme === 'light' ? 'Switch to Dark Mode' : 'Switch to Light Mode';
});