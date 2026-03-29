import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BarChart from './BarChart';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/genre-data')
      .then(res => setData(res.data.slice(0, 10))) // Show top 10
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ textAlign: 'center', backgroundColor: '#141414', color: 'white', minHeight: '100vh', padding: '20px' }}>
      <h1>Netflix Content Dashboard</h1>
      <h3>Top 10 Genres Globally</h3>
      <BarChart data={data} />
    </div>
  );
}

export default App;