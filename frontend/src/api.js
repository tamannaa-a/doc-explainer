// frontend/src/api.js
import axios from "axios";

const BACKEND_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000/api";

export async function analyzeFile(file) {
  const form = new FormData();
  form.append("file", file, file.name);
  const res = await axios.post(`${BACKEND_BASE}/analyze`, form, {
    headers: { "Content-Type": "multipart/form-data" },
    timeout: 120000
  });
  return res.data;
}
