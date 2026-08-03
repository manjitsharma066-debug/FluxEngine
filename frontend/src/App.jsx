import { useState } from "react";
import axios from "axios";
import "./App.css";

// Sidebar ko abhi use nahi karna
// import Sidebar from "./components/Sidebar";

function App() {

  const [orderId, setOrderId] = useState("");
  const [reason, setReason] = useState("Damaged Product");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const checkRefund = async () => {

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/refund/check",
        {
          order_id: orderId,
          reason: reason,
        }
      );

      setResult(response.data);

    } catch (error) {

      alert("API Error");
      console.error(error);

    } finally {

      setLoading(false);

    }

  };

  const getStatusClass = (status) => {

    if (status === "Approved") return "approved";

    if (status === "Rejected") return "rejected";

    return "pending";

  };

  return (
    <>
       {/* <Sidebar /> */}

      <div className="page">

        <div className="dashboard">

        {/* ===========================
             HEADER
        =========================== */}

        <div className="header">

          <div>

            <h1>🚀 FluxEngine</h1>

            <p>
              Domain Adaptive Agent Mesh (DAAM)
            </p>

          </div>

          <div className="engine-status">

            <span className="online-dot"></span>

            AI Engine Online

          </div>

        </div>

        {/* ===========================
             DASHBOARD CARDS
        =========================== */}

        <div className="stats-grid">

          <div className="stat-card">

            <h4>Total Requests</h4>

            <h2>128</h2>

          </div>

          <div className="stat-card">

            <h4>Approved</h4>

            <h2>96</h2>

          </div>

          <div className="stat-card">

            <h4>Pending</h4>

            <h2>18</h2>

          </div>

          <div className="stat-card">

            <h4>Knowledge Base</h4>

            <h2>JSON</h2>

          </div>

        </div>

        {/* ===========================
             FORM
        =========================== */}

        <div className="form-section">

          <label>Order ID</label>

          <input
            placeholder="Enter Order ID"
            value={orderId}
            onChange={(e) => setOrderId(e.target.value)}
          />

          <label>Refund Reason</label>

          <select
            value={reason}
            onChange={(e) => setReason(e.target.value)}
          >
            <option>Damaged Product</option>
            <option>Wrong Item</option>
            <option>Late Delivery</option>
          </select>

          <button onClick={checkRefund}>

            {loading
              ? "Checking..."
              : "🔍 Analyze Refund"}

          </button>

        </div>

        {/* ===========================
             RESULT
        =========================== */}

        {result && (

          <div className="result-card">

            <div
              className={`status ${getStatusClass(result.status)}`}
            >

              {result.status === "Approved"
                ? "✅ APPROVED"
                : result.status === "Rejected"
                ? "❌ REJECTED"
                : "🟡 PENDING"}

            </div>

            <div className="info-grid">

              <div className="info-box">

                <h4>💰 Refund</h4>

                <p>

                  ₹{result.refund_amount}

                </p>

              </div>

              <div className="info-box">

                <h4>👤 Customer</h4>

                <p>

                  {result.customer}

                </p>

              </div>

              <div className="info-box">

                <h4>📦 Product</h4>

                <p>

                  {result.product}

                </p>

              </div>

              <div className="info-box">

                <h4>📋 Policy</h4>

                <p>

                  {result.policy}

                </p>

              </div>

            </div>
	            <div className="knowledge">

              <h3>📚 Knowledge Source</h3>

              <p>
                <strong>Provider :</strong>{" "}
                {result.knowledge_source.provider}
              </p>

              <p>
                <strong>Mode :</strong>{" "}
                {result.knowledge_source.mode}
              </p>

              <p>
                <strong>Future :</strong>{" "}
                {result.knowledge_source.future_provider}
              </p>

            </div>

            <div className="knowledge">

              <h3>🧠 AI Decision</h3>

              <p>✅ Customer verified successfully</p>

              <p>✅ Refund policy matched</p>

              <p>✅ Order eligible under policy</p>

              <div className="confidence">

                <div className="confidence-text">

                  <span>Confidence Score</span>

                  <span>98%</span>

                </div>

                <div className="progress">

                  <div
                    className="progress-fill"
                    style={{ width: "98%" }}
                  ></div>

                </div>

              </div>

            </div>

            <div className="timeline">

              <h3>⏱ Workflow Timeline</h3>

              <ul>

                <li>📥 Refund Request Received</li>

                <li>📚 Knowledge Base Search</li>

                <li>📋 Policy Validation</li>

                <li>🤖 AI Decision Generated</li>

                <li>📝 Audit Log Saved</li>

              </ul>

            </div>

          </div>

        )}

                <div className="footer">

          <p>
            FluxEngine v1.0 • Domain Adaptive Agent Mesh (DAAM)
          </p>

        </div>

      </div>

    </div>

  </>

  );

}

export default App;