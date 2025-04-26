import React from 'react';

function DataTable({ data }) {
  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Recent Data</h2>
      <table className="w-full">
        <thead>
          <tr>
            <th className="text-left p-2">Time</th>
            <th className="text-left p-2">Alliance Avg</th>
            <th className="text-left p-2">Horde Avg</th>
          </tr>
        </thead>
        <tbody>
          {data.slice(-10).reverse().map((entry, index) => (
            <tr key={index}>
              <td className="p-2">{new Date(entry.timestamp).toLocaleString()}</td>
              <td className="p-2">{entry.alliance?.averagePrice || 'N/A'}</td>
              <td className="p-2">{entry.horde?.averagePrice || 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DataTable;
