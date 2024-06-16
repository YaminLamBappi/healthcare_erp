/** @type {import('tailwindcss').Config} */
// tailwind.config.js

module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html",
    "./**/*.js",
    "./**/*.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
