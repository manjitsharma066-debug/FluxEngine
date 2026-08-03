import { useState } from "react";
import axios from "axios";
import "./App.css";

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
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🚀 FluxEngine</h1>

      <input
        placeholder="Order ID"
        value={orderId}
        onChange={(e) => setOrderId(e.target.value)}
      />

      <select
        value={reason}
        onChange={(e) => setReason(e.target.value)}
      >
        <option>Damaged Product</option>
        <option>Wrong Item</option>
        <option>Late Delivery</option>
      </select>

      <button onClick={checkRefund}>
        {loading ? "Checking..." : "Check Refund"}
      </button>

      {result && (
        <div className="card">
          <h2>Refund Result</h2>

          <p><b>Status:</b> {result.status}</p>
          <p><b>Refund:</b> ₹{result.refund_amount}</p>
          <p><b>Policy:</b> {result.policy}</p>
          <p><b>Customer:</b> {result.customer}</p>
          <p><b>Product:</b> {result.product}</p>

          <hr />

          <h3>Knowledge Source</h3>

          <p><b>Provider:</b> {result.knowledge_source.provider}</p>

          <p><b>Mode:</b> {result.knowledge_source.mode}</p>

          <p>
            <b>Future:</b>{" "}
            {result.knowledge_source.future_provider}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;