import React, { useState, useEffect } from 'react';
import PriceChart from './components/PriceChart';
import DataTable from './components/DataTable';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/pricing_data.json')
      .then(response => response.json())
      .then(setData)
      .catch(console.error);
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">TSM Price Monitor</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <PriceChart data={data} />
        <DataTable data={data} />
      </div>
    </div>
  );
}

export default App;
