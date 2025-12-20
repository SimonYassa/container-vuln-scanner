const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000"; 

export async function getScans() {
  const response = await fetch(`${API_URL}/scans`);
  if (!response.ok) {
    throw new Error("Failed to fetch scans");
  }
  return response.json();
}
