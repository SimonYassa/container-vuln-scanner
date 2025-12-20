import { useEffect, useState } from "react";
import { PieChart, Pie, Cell, Tooltip } from 'recharts';
import { getScans } from "./api";
import './App.css';

function App() {
  const [scans, setScans] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState(""); // For search/filter

  useEffect(() => {
    getScans().then(data => {
      setScans(data || []);
      setLoading(false);
    });
  }, []);

  if (loading) return (
    <div className="spinner">
      <div className="bounce1"></div>
      <div className="bounce2"></div>
      <div className="bounce3"></div>
    </div>
  );

  // =========================
  // Prepare Pie Chart Data
  // =========================
  const severityCount = { LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0 };
  scans.forEach(scan => {
    scan.vulnerabilities.forEach(v => {
      const sev = v.severity?.toUpperCase() || "UNKNOWN";
      if (severityCount[sev] !== undefined) severityCount[sev]++;
    });
  });

  const chartData = Object.keys(severityCount).map(key => ({
    name: key,
    value: severityCount[key]
  }));

  const COLORS = {
    LOW: '#28a745',
    MEDIUM: '#ffc107',
    HIGH: '#dc3545',
    CRITICAL: '#721c24'
  };

  // =========================
  // Filter scans by search input
  // =========================
  const filteredScans = scans.filter(scan =>
    scan.image_name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="dashboard-container">
      <h1>Container Vulnerability Dashboard</h1>

      {/* =========================
          Search Input
      ========================= */}
      <div className="search-container">
        <input
          type="text"
          placeholder="Search by image name..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="search-input"
        />
      </div>

      {/* =========================
          Pie Chart
      ========================= */}
      <h2 style={{ textAlign: 'center' }}>Vulnerabilities by Severity</h2>
      <PieChart width={400} height={300}>
        <Pie
          data={chartData}
          dataKey="value"
          nameKey="name"
          cx="50%"
          cy="50%"
          outerRadius={100}
          label
        >
          {chartData.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[entry.name]} />
          ))}
        </Pie>
        <Tooltip />
      </PieChart>

      {/* =========================
          Table
      ========================= */}
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Image</th>
              <th>Scan Date</th>
              <th>CVE</th>
              <th>Severity</th>
            </tr>
          </thead>
          <tbody>
            {filteredScans.length === 0 && (
              <tr>
                <td colSpan="4" className="no-data">
                  No scans available or match your search.
                </td>
              </tr>
            )}

            {filteredScans.map(scan =>
              scan.vulnerabilities && scan.vulnerabilities.length > 0 ? (
                scan.vulnerabilities.map(vuln => (
                  <tr key={`${scan.image_name}-${vuln.cve}`}>
                    <td>{scan.image_name || "Unknown image"}</td>
                    <td>{scan.scan_date || "N/A"}</td>
                    <td>{vuln.cve || "N/A"}</td>
                    <td className={`severity ${vuln.severity?.toLowerCase() || ""}`}>
                      {vuln.severity || "UNKNOWN"}
                    </td>
                  </tr>
                ))
              ) : (
                <tr key={scan.image_name}>
                  <td>{scan.image_name}</td>
                  <td>{scan.scan_date}</td>
                  <td colSpan="2" style={{ textAlign: "center" }}>No vulnerabilities found 🎉</td>
                </tr>
              )
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
