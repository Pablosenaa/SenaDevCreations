const themeToggle = document.getElementById('theme-switch');

function applyTheme(theme) {
    document.body.className = theme;
}

const savedTheme = localStorage.getItem('theme') || 'light';
applyTheme(savedTheme);

if (themeToggle) {
    themeToggle.value = savedTheme;
    themeToggle.addEventListener('change', (event) => {
        applyTheme(event.target.value);
        localStorage.setItem('theme', event.target.value);
    });
}
