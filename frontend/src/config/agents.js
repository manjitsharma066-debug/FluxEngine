const agents = {
  ecommerce: [
    {
      id: "refund",
      name: "Refund & Policy Verification",
      available: true,
    },
    {
      id: "tracking",
      name: "Order Tracking",
      available: false,
    },
    {
      id: "product-search",
      name: "Product Search",
      available: false,
    },
    {
      id: "recommendation",
      name: "Product Recommendation",
      available: false,
    },
    {
      id: "support",
      name: "Customer Support",
      available: false,
    },
  ],

  bfsi: [
    {
      id: "fraud",
      name: "Fraud Detection",
      available: false,
    },
    {
      id: "kyc",
      name: "KYC Verification",
      available: false,
    },
  ],

  healthcare: [
    {
      id: "claims",
      name: "Insurance Claim Validation",
      available: false,
    },
  ],

  public: [
    {
      id: "citizen",
      name: "Citizen Service Automation",
      available: false,
    },
  ],
};

export default agents;