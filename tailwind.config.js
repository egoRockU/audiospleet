/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./main/templates/*.html", "./main/templates/validate_results/*.html"],
  theme: {
    extend: {},
  },
  daisyui: {
      themes: [
        {
          mytheme: {
            "primary": "#111827",
            "secondary": "#15803d",
            "accent": "#00ffff",
            "neutral": "#111827",
            "base-100": "#1f2937",
            "info": "#0000ff",
            "success": "#22c55e",
            "warning": "#facc15",
            "error": "#ef4444",
          },
        },
      ],
    },
  plugins: [require('daisyui'),],
};
