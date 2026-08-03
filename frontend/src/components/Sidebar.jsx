import "./Sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">

      <div className="logo">

        <h2>🚀 FluxEngine</h2>

        <p>DAAM Platform</p>

      </div>

      <nav>

        <ul>

          <li className="active">
            🏠 Dashboard
          </li>

          <li>
            🤖 AI Agents
          </li>

          <li>
            📚 Knowledge
          </li>

          <li>
            📊 Analytics
          </li>

          <li>
            📜 Audit Logs
          </li>

          <li>
            ⚙️ Settings
          </li>

        </ul>

      </nav>

    </aside>
  );
}

export default Sidebar;