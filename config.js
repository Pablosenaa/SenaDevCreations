const themeToggle = document.getElementById('theme-button');
const languageToggle = document.getElementById('language-button');
const languageSelect = document.getElementById('idioma');

function applyTheme(theme) {
    document.body.className = theme;
    localStorage.setItem('theme', theme);
}

const savedTheme = localStorage.getItem('theme') || 'light';
applyTheme(savedTheme);

function toggleThemeMenu() {
    const menu = document.getElementById('theme-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

function setTheme(theme) {
    applyTheme(theme);
    document.getElementById('theme-menu').style.display = 'none'; // Fecha o menu após a seleção
}

function toggleLanguageMenu() {
    const menu = document.getElementById('language-menu');
    menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
}

function setLanguage(language) {
    localStorage.setItem('language', language);
    // Aqui você pode adicionar a lógica de tradução se necessário
    document.getElementById('language-menu').style.display = 'none'; // Fecha o menu após a seleção
}

const savedLanguage = localStorage.getItem('language') || 'pt-BR';
setLanguage(savedLanguage); // Aplica o idioma salvo ao carregar
