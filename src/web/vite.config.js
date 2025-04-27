import { defineConfig } from 'vite'

export default defineConfig({
  root: 'public',  // Tell Vite: start from ./public
  publicDir: '../static', // Optional: if you have *other* public assets (not important here)
  build: {
    outDir: '../build',  // Where to output final site
    emptyOutDir: true,   // Clean the build folder first
  }
})
