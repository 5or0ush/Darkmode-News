// static/js/theme.js
(function () {
  const THEME_KEY = "cybernews-theme";

  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    // ajută browserul să aleagă paleta corectă pt controale native
    document.documentElement.style.colorScheme = t === "dark" ? "dark" : "light";
    const btn = document.getElementById("themeToggle");
    if (btn) btn.textContent = t === "dark" ? "🌞 Light" : "🌙 Dark";
  }

  function getPreferredTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved === "light" || saved === "dark") return saved;
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme") || "light";
    const next = current === "dark" ? "light" : "dark";
    localStorage.setItem(THEME_KEY, next);
    applyTheme(next);
  }

  // init
  document.addEventListener("DOMContentLoaded", () => {
    applyTheme(getPreferredTheme());
    const btn = document.getElementById("themeToggle");
    if (btn) btn.addEventListener("click", toggleTheme);
  });
})();
